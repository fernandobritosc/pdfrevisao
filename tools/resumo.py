#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resumo.py — CLI unificado para operações nos resumos de estudo.

Substitui scripts soltos: list_secs*.py, find_sec*.py, fix_nav.py, fix_next.py,
add_next.py, scripts/download_imgs.py

Uso:
    python tools/resumo.py sections <arquivo.html>           # lista secoes
    python tools/resumo.py find <termo> <arquivo.html>       # acha secao do termo
    python tools/resumo.py fix-nav <arquivo.html>            # corrige link "proxima -> indice geral"
    python tools/resumo.py add-next <arquivo.html>           # adiciona card "Proxima aula"
    python tools/resumo.py download-imgs <urls.txt>          # baixa imagens de URLs (uma por linha)
    python tools/resumo.py validate [--dir Resumo_estudos]   # validacao completa (alias p/ validate-all.py)
"""
import sys
import re
import argparse
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple
import subprocess


REPO_ROOT = Path(__file__).parent.parent
RESUMOS_ROOT = REPO_ROOT / 'Resumo_estudos'
TEMPLATES_DIR = RESUMOS_ROOT / 'templates'
TOOLS_DIR = REPO_ROOT / 'tools'


# ===================== COMANDOS =====================

def cmd_sections(args: argparse.Namespace) -> int:
    """Lista títulos das seções (<div class="sec-title">) de um arquivo."""
    path = Path(args.file)
    if not path.exists():
        print(f"Arquivo não encontrado: {path}")
        return 1

    content = path.read_text(encoding='utf-8', errors='ignore')
    # Procura tanto sec-title (novo) quanto section-title (antigo)
    titles = re.findall(r'<div class="sec-title">([^<]+)</div>', content)
    if not titles:
        titles = re.findall(r'<div class="section-title"><span class="tag tag-(?:blue|amber|green|red)">\d+</span> ([^<]+)</div>', content)

    if not titles:
        print("Nenhuma seção encontrada")
        return 0

    for i, t in enumerate(titles, 1):
        print(f"  {i}. {t.strip()}")
    return 0


def cmd_find(args: argparse.Namespace) -> int:
    """Encontra a seção onde um termo aparece (busca apenas no conteúdo principal)."""
    path = Path(args.file)
    if not path.exists():
        print(f"Arquivo não encontrado: {path}")
        return 1

    content = path.read_text(encoding='utf-8', errors='ignore')
    term = args.term.lower()

    # Busca apenas no conteúdo principal (após <div class="main">)
    main_start = content.find('<div class="main">')
    if main_start == -1:
        main_start = 0

    main_content = content[main_start:]
    idx = main_content.lower().find(term)
    if idx == -1:
        print(f"Termo '{args.term}' não encontrado no conteúdo principal")
        return 1

    # Ajusta índice para o conteúdo completo
    idx = main_start + idx

    # Procura sec-title anterior (novo padrão)
    prev = content.rfind('<div class="sec-title">', 0, idx)
    if prev != -1:
        start = content.find('>', prev) + 1
        end = content.find('</div>', start)
        sec = content[start:end].strip()
        print(f"Secao (novo padrao): {sec}")
        return 0

    # Procura section-title anterior (padrão antigo)
    prev = content.rfind('<div class="section-title">', 0, idx)
    if prev != -1:
        # Extrai o texto após o span da tag
        tag_end = content.find('</span>', prev)
        if tag_end != -1:
            start = content.find('>', tag_end)
            if start != -1:
                start += 1
                end = content.find('</div>', start)
                sec = content[start:end].strip()
                print(f"Secao (padrao antigo): {sec}")
                return 0

    print("Secao não identificada")
    return 1


def cmd_fix_nav(args: argparse.Namespace) -> int:
    """Corrige link 'Próxima -> Índice geral' para apontar para aula seguinte."""
    path = Path(args.file)
    if not path.exists():
        print(f"Arquivo não encontrado: {path}")
        return 1

    content = path.read_text(encoding='utf-8', errors='ignore')

    # Padrões conhecidos do link errado
    old_patterns = [
        r'<a class="next" href="\.\./\.\./index\.html" rel="next"><span class="aula-nav-dir">próxima →</span><span class="aula-nav-label">Índice geral</span></a>',
        r'<a class="next" href="\.\./\.\./index\.html" rel="next"><span class="aula-nav-dir">[^<]+</span><span class="aula-nav-label">Índice geral</span></a>',
        r'<a href="[^"]*">Próxima[^<]*Índice geral</a>',
    ]

    # Tenta determinar a próxima aula baseada no nome do arquivo
    # Ex: resumo-aula-05-...html -> procura Aula 06 na mesma matéria
    match = re.search(r'resumo-aula-(\d+)-', path.name)
    next_link = None
    next_label = None

    if match:
        current_num = int(match.group(1))
        next_num = current_num + 1
        # Procura arquivo da próxima aula no mesmo diretório
        for f in sorted(path.parent.glob(f'resumo-aula-{next_num:02d}-*.html')):
            next_link = f.relative_to(path.parent)
            # Extrai tema do nome do arquivo
            theme_match = re.search(r'resumo-aula-\d+-(.+)\.html', f.name)
            if theme_match:
                theme = theme_match.group(1).replace('-', ' ').title()
                next_label = f'Aula {next_num:02d} — {theme}'
            else:
                next_label = f'Aula {next_num:02d}'
            break

    if not next_link:
        # Fallback: usa índice geral
        next_link = Path('../../index.html')
        next_label = 'Índice geral'

    new_html = f'<a class="next" href="{next_link}" rel="next"><span class="aula-nav-dir">próxima →</span><span class="aula-nav-label">{next_label}</span></a>'

    replaced = False
    for pattern in old_patterns:
        new_content, count = re.subn(pattern, new_html, content, count=1, flags=re.IGNORECASE)
        if count > 0:
            content = new_content
            replaced = True
            break

    if replaced:
        path.write_text(content, encoding='utf-8')
        print(f"Corrigido: {path.name} -> {next_label} ({next_link})")
        return 0
    else:
        print("Padrão de link 'Índice geral' não encontrado")
        return 1


def cmd_add_next(args: argparse.Namespace) -> int:
    """Adiciona card 'Próxima aula' antes do </body>."""
    path = Path(args.file)
    if not path.exists():
        print(f"Arquivo não encontrado: {path}")
        return 1

    content = path.read_text(encoding='utf-8', errors='ignore')

    # Determina próxima aula
    match = re.search(r'resumo-aula-(\d+)-', path.name)
    next_link = None
    next_label = None

    if match:
        current_num = int(match.group(1))
        next_num = current_num + 1
        for f in sorted(path.parent.glob(f'resumo-aula-{next_num:02d}-*.html')):
            next_link = f.relative_to(path.parent)
            theme_match = re.search(r'resumo-aula-\d+-(.+)\.html', f.name)
            if theme_match:
                theme = theme_match.group(1).replace('-', ' ').title()
                next_label = f'Aula {next_num:02d} — {theme}'
            else:
                next_label = f'Aula {next_num:02d}'
            break

    if not next_link:
        next_link = Path('../../index.html')
        next_label = 'Índice geral'

    insert = f'<div class="card" id="rh-next"><div class="card-title">Próxima aula</div><div class="card-text">→ <a href="{next_link}">{next_label}</a></div></div>\n'

    if '</body>' in content:
        content = content.replace('</body>', insert + '</body>')
        path.write_text(content, encoding='utf-8')
        print(f"Card 'Próxima aula' adicionado: {next_label} ({next_link})")
        return 0
    else:
        print("Tag </body> não encontrada")
        return 1


def cmd_download_imgs(args: argparse.Namespace) -> int:
    """Baixa imagens de URLs (arquivo com uma URL por linha ou URLs como argumentos)."""
    urls: List[str] = []

    if args.urls_file:
        path = Path(args.urls_file)
        if not path.exists():
            print(f"Arquivo não encontrado: {path}")
            return 1
        urls = [line.strip() for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

    urls.extend(args.urls)

    if not urls:
        print("Nenhuma URL fornecida. Use --urls-file ou passe URLs como argumentos.")
        return 1

    out_dir = Path(args.output) if args.output else REPO_ROOT / 'temp_imgs'
    out_dir.mkdir(parents=True, exist_ok=True)

    for i, url in enumerate(urls):
        try:
            # Tenta extrair extensão da URL
            ext = '.png'
            if '.' in url.split('/')[-1]:
                ext = '.' + url.split('/')[-1].split('.')[-1].split('?')[0]
                if len(ext) > 5:  # extensão muito longa = provavelmente não é extensão
                    ext = '.png'

            out_path = out_dir / f"img{i+1}{ext}"
            print(f"Baixando {url} -> {out_path}...")
            urllib.request.urlretrieve(url, out_path)
            print(f"  OK {out_path} ({out_path.stat().st_size} bytes)")
        except Exception as e:
            print(f"  Erro ao baixar {url}: {e}")

    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    """Executa validação completa (delegate para validate-all.py)."""
    validate_all = TOOLS_DIR / 'validate-all.py'
    if not validate_all.exists():
        print("validate-all.py não encontrado")
        return 1

    cmd = [sys.executable, str(validate_all)]
    if args.dir:
        cmd.extend(['--dir', args.dir])
    if args.json:
        cmd.append('--json')
    if args.verbose:
        cmd.append('--verbose')
    if args.only_html:
        cmd.append('--only-html')

    return subprocess.run(cmd).returncode


# ===================== MAIN =====================

def main():
    parser = argparse.ArgumentParser(
        description='CLI unificado para operações nos resumos de estudo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # sections
    p_sec = subparsers.add_parser('sections', help='Lista secoes de um resumo')
    p_sec.add_argument('file', help='Arquivo HTML do resumo')
    p_sec.set_defaults(func=cmd_sections)

    # find
    p_find = subparsers.add_parser('find', help='Encontra secao onde termo aparece')
    p_find.add_argument('term', help='Termo a buscar')
    p_find.add_argument('file', help='Arquivo HTML do resumo')
    p_find.set_defaults(func=cmd_find)

    # fix-nav
    p_fix = subparsers.add_parser('fix-nav', help='Corrige link "proxima -> indice geral"')
    p_fix.add_argument('file', help='Arquivo HTML do resumo')
    p_fix.set_defaults(func=cmd_fix_nav)

    # add-next
    p_add = subparsers.add_parser('add-next', help='Adiciona card "Proxima aula"')
    p_add.add_argument('file', help='Arquivo HTML do resumo')
    p_add.set_defaults(func=cmd_add_next)

    # download-imgs
    p_dl = subparsers.add_parser('download-imgs', help='Baixa imagens de URLs')
    p_dl.add_argument('urls', nargs='*', help='URLs das imagens')
    p_dl.add_argument('--urls-file', '-f', help='Arquivo com uma URL por linha')
    p_dl.add_argument('--output', '-o', help='Diretório de saída (padrão: temp_imgs/)')
    p_dl.set_defaults(func=cmd_download_imgs)

    # validate
    p_val = subparsers.add_parser('validate', help='Validacao completa (gate de deploy)')
    p_val.add_argument('--dir', help='Diretório raiz dos resumos')
    p_val.add_argument('--json', action='store_true', help='Saída JSON')
    p_val.add_argument('--verbose', '-v', action='store_true', help='Detalhes')
    p_val.add_argument('--only-html', action='store_true', help='Só validação HTML')
    p_val.set_defaults(func=cmd_validate)

    args = parser.parse_args()
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())