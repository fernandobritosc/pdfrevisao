#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate-all.py — Gate de qualidade completo antes de deploy.

Executa:
  1. check-html.py em TODOS os resumo-aula-*.html (balanceamento de tags)
  2. Verifica se todos têm os add-ons injetados (versões corretas)
  3. Verifica se search-index.json e mudancas.html estão atualizados (mtime > resumos)
  4. Verifica resíduos de padrões antigos (Archivo, card-header, section-title, grid-2, <main class="main">)

Uso:
    python tools/validate-all.py              # validação completa, exit code 1 se falhar
    python tools/validate-all.py --fix        # tenta corrigir problemas auto-corrigíveis (futuro)
    python tools/validate-all.py --json       # saída JSON para CI
"""
import sys
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple
from datetime import datetime


REPO_ROOT = Path(__file__).parent.parent
RESUMOS_ROOT = REPO_ROOT / 'Resumo_estudos'
TEMPLATES_DIR = RESUMOS_ROOT / 'templates'
CHECK_HTML = REPO_ROOT / 'tools' / 'check-html.py'


# Padrões que NÃO devem mais existir (resíduos de migração)
FORBIDDEN_PATTERNS = [
    ('family=Archivo', 'Fonte Archivo ainda presente (deve ser Space Grotesk)'),
    ('<div class="card-header">', 'card-header antigo (deve ser card-title direto)'),
    ('class="section-title"', 'section-title antigo (deve ser sec-header + sec-num + sec-title)'),
    ('grid grid-2', 'grid-2 proibido (cards devem ser coluna única)'),
    ('grid grid-3', 'grid-3 proibido (cards devem ser coluna única)'),
    ('<main class="main">', 'main class="main" antigo (deve ser <div class="main">)'),
    ('class="section-subtitle"', 'section-subtitle antigo (deve ser sec-subtitle)'),
    ('font-family:Archivo', 'font-family:Archivo em CSS (deve ser Space Grotesk)'),
    ('Permanent Marker', 'Fonte Permanent Marker em sketchnote (deve ser Space Grotesk)'),
    ('Patrick Hand', 'Fonte Patrick Hand em sketchnote (deve ser IBM Plex Sans)'),
]

# Add-ons obrigatórios e seus marcadores de versão
REQUIRED_ADDONS = [
    ('review', 'id="rhRev"', 'Modo revisao (cerebro)'),
    ('marks', 'id="rhMarks"', 'Marcacao pessoal (tag)'),
    ('search', 'data-sr-v="2"', 'Busca v2 (navegacao + multi-palavra)'),
    ('pwa', 'rel="manifest"', 'PWA offline'),
    # practice é condicional: só se quiz.json existir
]

# Arquivos de build que devem estar atualizados
BUILD_FILES = [
    ('search-index.json', RESUMOS_ROOT / 'search-index.json', 'build-search-index.py'),
    ('mudancas.html', RESUMOS_ROOT / 'mudancas.html', 'build-changelog.py'),
]


def run_check_html(targets: List[Path], verbose: bool = False) -> Tuple[int, int, Dict[str, List[str]]]:
    """Roda check-html.py em todos os arquivos alvo."""
    all_errors = 0
    all_open = 0
    details: Dict[str, List[str]] = {}

    for path in targets:
        result = subprocess.run(
            [sys.executable, str(CHECK_HTML), str(path)],
            capture_output=True, text=True, encoding='utf-8', errors='replace'
        )
        # Parse output: "[FAIL] rel: ERROS=X ABERTAS=Y" ou "[OK] rel: OK"
        output = (result.stdout or '').strip()
        if 'ERROS=' in output:
            # Extrai números
            import re
            m = re.search(r'ERROS=(\d+)\s+ABERTAS=(\d+)', output)
            if m:
                e = int(m.group(1))
                o = int(m.group(2))
                all_errors += e
                all_open += o
                if verbose or e > 0 or o > 0:
                    details[str(path)] = output.split('\n')
        elif 'OK' not in output and output:
            details[str(path)] = [output]

    return all_errors, all_open, details


def check_addons(filepath: Path) -> Dict[str, bool]:
    """Verifica quais add-ons estão presentes no arquivo."""
    try:
        content = filepath.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return {}

    results = {}
    for key, marker, desc in REQUIRED_ADDONS:
        results[key] = marker in content

    # Practice mode: verifica se quiz.json existe na mesma pasta
    quiz_path = filepath.parent / 'quiz.json'
    has_quiz = quiz_path.exists()
    has_practice = 'id="rh-practice"' in content or '<!--rh:practice:start-->' in content
    results['practice'] = (not has_quiz) or has_practice  # True se não precisa ou já tem
    results['_has_quiz'] = has_quiz

    return results


def check_forbidden_patterns(filepath: Path) -> List[str]:
    """Verifica padrões proibidos (resíduos de migração)."""
    try:
        content = filepath.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return ['Erro ao ler arquivo']

    found = []
    for pattern, desc in FORBIDDEN_PATTERNS:
        if pattern in content:
            found.append(f"{desc}: '{pattern}'")
    return found


def check_build_freshness() -> List[str]:
    """Verifica se arquivos de build estão mais novos que os resumos."""
    warnings = []

    # Encontra o mtime mais recente entre todos os resumos
    resumo_files = list(RESUMOS_ROOT.rglob('resumo-aula-*.html'))
    if not resumo_files:
        return ['Nenhum resumo encontrado']

    latest_resumo_mtime = max(f.stat().st_mtime for f in resumo_files)

    for name, build_path, script in BUILD_FILES:
        if not build_path.exists():
            warnings.append(f"{name}: não existe (rodar {script})")
            continue
        build_mtime = build_path.stat().st_mtime
        if build_mtime < latest_resumo_mtime:
            dt_resumo = datetime.fromtimestamp(latest_resumo_mtime).strftime('%d/%m/%Y %H:%M')
            dt_build = datetime.fromtimestamp(build_mtime).strftime('%d/%m/%Y %H:%M')
            warnings.append(f"{name}: desatualizado (build: {dt_build} < último resumo: {dt_resumo}) — rodar {script}")

    return warnings


def find_all_resumos() -> List[Path]:
    return sorted(RESUMOS_ROOT.rglob('resumo-aula-*.html'))


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Gate de qualidade completo para deploy')
    parser.add_argument('--json', action='store_true', help='Saída JSON')
    parser.add_argument('--verbose', '-v', action='store_true', help='Detalhes')
    parser.add_argument('--only-html', action='store_true', help='Só validação HTML')
    args = parser.parse_args()

    resumos = find_all_resumos()
    if not resumos:
        print("[FAIL] Nenhum resumo-aula-*.html encontrado")
        return 1

    report: Dict[str, Any] = {
        'total_files': len(resumos),
        'html_validation': {'errors': 0, 'open_tags': 0, 'details': {}},
        'addons': {},
        'forbidden_patterns': {},
        'build_freshness': [],
        'passed': True
    }

    # 1. Validacao HTML
    if not args.json:
        print(f"[INFO] Validando HTML em {len(resumos)} arquivos...")
    errors, open_tags, html_details = run_check_html(resumos, args.verbose)
    report['html_validation']['errors'] = errors
    report['html_validation']['open_tags'] = open_tags
    report['html_validation']['details'] = html_details

    if errors > 0 or open_tags > 0:
        report['passed'] = False
        if not args.json:
            print(f"   [FAIL] HTML: {errors} erros, {open_tags} tags abertas")
    elif not args.json:
        print(f"   [OK] HTML: OK")

    # 2. Add-ons
    if not args.json:
        print("[INFO] Verificando add-ons...")
    missing_addons: Dict[str, List[str]] = {}
    for path in resumos:
        addon_status = check_addons(path)
        rel = path.relative_to(REPO_ROOT)
        report['addons'][str(rel)] = addon_status
        for key, present in addon_status.items():
            if key.startswith('_'):
                continue
            if not present:
                desc = next((d for k, _, d in REQUIRED_ADDONS if k == key), key)
                missing_addons.setdefault(key, []).append(str(rel))

    if missing_addons:
        report['passed'] = False
        if not args.json:
            for key, files in missing_addons.items():
                desc = next((d for k, _, d in REQUIRED_ADDONS if k == key), key)
                print(f"   [FAIL] {desc}: ausente em {len(files)} arquivo(s)")
                if args.verbose:
                    for f in files[:5]:
                        print(f"      - {f}")
                    if len(files) > 5:
                        print(f"      ... e mais {len(files) - 5}")
    elif not args.json:
        print("   [OK] Add-ons: todos presentes")

    # 3. Practice mode condicional
    practice_missing = []
    for path in resumos:
        addon_status = check_addons(path)
        if addon_status.get('_has_quiz') and not addon_status.get('practice'):
            practice_missing.append(str(path.relative_to(REPO_ROOT)))
    if practice_missing:
        report['passed'] = False
        if not args.json:
            print(f"   [FAIL] Modo pratica (alvo): quiz.json existe mas add-on nao injetado em {len(practice_missing)} arquivo(s)")

    # 4. Padroes proibidos
    if not args.json:
        print("[INFO] Verificando residuos de migracao...")
    forbidden_found: Dict[str, List[str]] = {}
    for path in resumos:
        found = check_forbidden_patterns(path)
        if found:
            rel = str(path.relative_to(REPO_ROOT))
            forbidden_found[rel] = found
            report['passed'] = False

    report['forbidden_patterns'] = forbidden_found
    if forbidden_found and not args.json:
        for file, issues in forbidden_found.items():
            print(f"   [FAIL] {file}:")
            for issue in issues:
                print(f"      - {issue}")
    elif not args.json:
        print("   [OK] Residuos: nenhum")

    # 4. Build freshness
    if not args.only_html:
        if not args.json:
            print("[INFO] Verificando freshness de build...")
        freshness_warnings = check_build_freshness()
        report['build_freshness'] = freshness_warnings
        if freshness_warnings:
            report['passed'] = False
            if not args.json:
                for w in freshness_warnings:
                    print(f"   [WARN] {w}")
        elif not args.json:
            print("   [OK] Build files: atualizados")

    # Summary
    if not args.json:
        print("\n" + "=" * 50)
        if report['passed']:
            print("[OK] TODAS AS VALIDACOES PASSARAM -- deploy liberado")
        else:
            print("[FAIL] VALIDACAO FALHOU -- corrigir antes de deploy")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))

    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())