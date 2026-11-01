#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Orquestrador Declarativo do Pipeline de Build

Uso:
    python build.py                    # Pipeline completo (padrão)
    python build.py --step design      # Só design system
    python build.py --step template    # Só template (requer design system já gerado)
    python build.py --step validate    # Só validação
    python build.py --step deploy      # Deploy Surge (requer template válido)
    python build.py --step all --parallel  # Paraleliza etapas independentes
    python build.py --list-steps       # Lista passos disponíveis
    python build.py --help             # Ajuda

Pipeline completo (ordem declarativa):
    1. design       - Concatena/minifica design-system CSS+JS
    2. template     - Injeta no template-thin -> template-sumario.html
    3. validate     - check-html.py no template gerado
    4. index        - build-search-index.py (busca full-text)
    5. changelog    - build-changelog.py (pagina "O que mudou")
    6. deploy       - npx surge + HTTP 200 check

Etapas independentes (podem rodar em paralelo): index + changelog
"""

import argparse
import os
import re
import sys
import time
import subprocess
import concurrent.futures
from pathlib import Path
from dataclasses import dataclass, field
from typing import Callable, Optional, List, Dict, Any
from enum import Enum

try:
    import cssmin
except ImportError:
    cssmin = None

try:
    import jsmin
except ImportError:
    jsmin = None

ROOT = Path(__file__).parent
DESIGN_SYSTEM = ROOT / "design-system"
TEMPLATE_THIN = ROOT / "template-thin.html"
TEMPLATE_OUT = ROOT / "Resumo_estudos" / "templates" / "template-sumario.html"
RESUMOS_DIR = ROOT / "Resumo_estudos"
SEARCH_INDEX = RESUMOS_DIR / "search-index.json"
CHANGELOG = RESUMOS_DIR / "mudancas.html"

# ============================================================
# DEFINIÇÃO DECLARATIVA DOS PASSOS
# ============================================================

class StepStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"

@dataclass
class BuildStep:
    name: str
    description: str
    function: Callable[["BuildContext"], bool]
    depends_on: List[str] = field(default_factory=list)
    parallel_group: Optional[str] = None  # Etapas no mesmo grupo rodam em paralelo
    required: bool = True  # Se False, falha não para o pipeline

@dataclass
class BuildContext:
    root: Path
    design_system: Path
    template_thin: Path
    template_out: Path
    resumos_dir: Path
    search_index: Path
    changelog: Path
    verbose: bool = False
    parallel: bool = False
    step_results: Dict[str, StepStatus] = field(default_factory=dict)
    start_time: float = field(default_factory=time.time)

    def log(self, msg: str, level: str = "INFO"):
        prefix = {"INFO": "  [OK]", "WARN": "  [WARN]", "ERROR": "  [ERROR]", "DEBUG": "  [DEBUG]"}.get(level, "  [LOG]")
        elapsed = time.time() - self.start_time
        print(f"[{elapsed:6.2f}s] {prefix} {msg}")

    def step_done(self, step_name: str, success: bool):
        self.step_results[step_name] = StepStatus.SUCCESS if success else StepStatus.FAILED

# ============================================================
# IMPLEMENTAÇÃO DOS PASSOS
# ============================================================

# --- CSS/JS Files ---
CSS_FILES = [
    "css/tokens.css", "css/base.css",
    "css/components/sidebar.css", "css/components/layout.css", "css/components/card.css",
    "css/components/callout.css", "css/components/table.css", "css/components/button.css",
    "css/components/tag.css", "css/components/gotcha.css", "css/components/mnemonic.css",
    "css/components/header.css", "css/components/highlight.css", "css/components/flow.css",
    "css/components/question.css", "css/components/landing.css",
    "css/addons/dark-mode.css", "css/addons/print.css", "css/addons/toolbar.css",
    "css/addons/navigation.css", "css/addons/review-mode.css", "css/addons/marks-mode.css",
    "css/addons/search.css", "css/addons/practice.css", "css/addons/legal-block.css",
]

JS_FILES = [
    "js/modules/theme-init.js", "js/modules/toolbar.js", "js/modules/review-mode.js",
    "js/modules/marks-mode.js", "js/modules/search-v2.js", "js/modules/practice-mode.js",
    "js/modules/pwa.js", "js/main.js",
]

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def minify_css(css: str) -> str:
    if cssmin: return cssmin.cssmin(css)
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>+~])\s*", r"\1", css)
    return css.strip()

def minify_js(js: str) -> str:
    if jsmin: return jsmin.jsmin(js)
    js = re.sub(r"/\*.*?\*/", "", js, flags=re.DOTALL)
    js = re.sub(r"//.*$", "", js, flags=re.MULTILINE)
    js = re.sub(r"\s+", " ", js)
    return js.strip()

# --- Step 1: Design System ---
def step_design(ctx: BuildContext) -> bool:
    ctx.log("Concatenando CSS...")
    css_parts = []
    for rel in CSS_FILES:
        path = ctx.design_system / rel
        if path.exists():
            css_parts.append(f"/* {rel} */\n{read_file(path)}")
        else:
            ctx.log(f"{rel} não encontrado", "WARN")
    css = "\n\n".join(css_parts)
    ctx.log(f"CSS bruto: {len(css):,} chars")
    css = minify_css(css)
    ctx.log(f"CSS minificado: {len(css):,} chars")

    ctx.log("Concatenando JS...")
    js_parts = []
    for rel in JS_FILES:
        path = ctx.design_system / rel
        if path.exists():
            content = read_file(path)
            if rel == "js/main.js":
                content = content.replace("export const DesignSystem", "window.DesignSystem")
            js_parts.append(f"// {rel}\n{content}")
        else:
            ctx.log(f"{rel} não encontrado", "WARN")
    js = "\n\n".join(js_parts)
    ctx.log(f"JS bruto: {len(js):,} chars")
    js = minify_js(js)
    ctx.log(f"JS minificado: {len(js):,} chars")

    # Cache para próximos passos
    ctx.design_css = css
    ctx.design_js = js
    return True

# --- Step 2: Template ---
def step_template(ctx: BuildContext) -> bool:
    if not hasattr(ctx, 'design_css') or not hasattr(ctx, 'design_js'):
        ctx.log("Design system não gerado (execute step 'design' antes)", "ERROR")
        return False

    ctx.log("Injetando no template...")
    template = read_file(ctx.template_thin)
    css_block = f"<style>\n{ctx.design_css}\n</style>"
    js_block = f"<script type=\"module\">\n{ctx.design_js}\n</script>"
    html = template.replace("{{CSS}}", css_block).replace("{{JS}}", js_block)

    ctx.template_out.parent.mkdir(parents=True, exist_ok=True)
    ctx.template_out.write_text(html, encoding="utf-8")
    ctx.log(f"Template gerado: {ctx.template_out.relative_to(ctx.root)} ({len(html):,} chars)")
    return True

# --- Step 3: Validate ---
def step_validate(ctx: BuildContext) -> bool:
    ctx.log("Validando HTML...")
    result = subprocess.run(
        [sys.executable, "tools/check-html.py", str(ctx.template_out)],
        capture_output=True, text=True, cwd=ctx.root
    )
    if result.returncode != 0:
        ctx.log("HTML inválido:", "ERROR")
        print(result.stdout)
        return False
    ctx.log("HTML válido!")
    return True

# --- Step 4: Search Index ---
def step_index(ctx: BuildContext) -> bool:
    ctx.log("Gerando search-index.json...")
    result = subprocess.run(
        [sys.executable, "build-search-index.py"],
        capture_output=True, text=True, cwd=ctx.root
    )
    if result.returncode != 0:
        ctx.log("Falha ao gerar índice:", "ERROR")
        print(result.stdout)
        print(result.stderr)
        return False
    ctx.log("Índice gerado!")
    if ctx.verbose:
        print(result.stdout.strip())
    return True

# --- Step 5: Changelog ---
def step_changelog(ctx: BuildContext) -> bool:
    ctx.log("Gerando changelog...")
    result = subprocess.run(
        [sys.executable, "build-changelog.py"],
        capture_output=True, text=True, cwd=ctx.root
    )
    if result.returncode != 0:
        ctx.log("Falha ao gerar changelog:", "ERROR")
        print(result.stdout)
        print(result.stderr)
        return False
    ctx.log("Changelog gerado!")
    if ctx.verbose:
        print(result.stdout.strip())
    return True

# --- Step 6: Deploy ---
def step_deploy(ctx: BuildContext) -> bool:
    ctx.log("Fazendo deploy no Surge...")
    # Verifica se surge está disponível
    try:
        subprocess.run(["npx", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        ctx.log("npx não encontrado. Instale Node.js.", "ERROR")
        return False

    cmd = ["npx", "surge", str(ctx.resumos_dir), "resumos-hermes.surge.sh"]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ctx.root, timeout=120)
    if result.returncode != 0:
        ctx.log("Deploy falhou:", "ERROR")
        print(result.stdout)
        print(result.stderr)
        return False

    ctx.log("Deploy feito! Verificando HTTP 200...")
    # Extrai URL do output do surge
    url_match = re.search(r'https?://[^\s]+', result.stdout)
    if url_match:
        url = url_match.group(0)
        ctx.log(f"URL: {url}")
        # Verifica HTTP 200
        try:
            import urllib.request
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req, timeout=10) as resp:
                if resp.status == 200:
                    ctx.log("HTTP 200 OK!")
                else:
                    ctx.log(f"HTTP {resp.status} (esperado 200)", "WARN")
        except Exception as e:
            ctx.log(f"Não pôde verificar HTTP 200: {e}", "WARN")
    else:
        ctx.log("URL não detectada no output do surge", "WARN")

    ctx.log("Deploy completo!")
    return True

# ============================================================
# REGISTRO DE PASSOS (ordem declarativa)
# ============================================================

STEPS: List[BuildStep] = [
    BuildStep(
        name="design",
        description="Concatena e minifica design-system CSS + JS",
        function=step_design,
    ),
    BuildStep(
        name="template",
        description="Injeta design system no template-thin -> template-sumario.html",
        function=step_template,
        depends_on=["design"],
    ),
    BuildStep(
        name="validate",
        description="Valida HTML gerado com check-html.py",
        function=step_validate,
        depends_on=["template"],
    ),
    BuildStep(
        name="index",
        description="Gera search-index.json (busca full-text)",
        function=step_index,
        depends_on=["validate"],
        parallel_group="post-validate",
    ),
    BuildStep(
        name="changelog",
        description="Gera mudancas.html (changelog via git log)",
        function=step_changelog,
        depends_on=["validate"],
        parallel_group="post-validate",
    ),
    BuildStep(
        name="deploy",
        description="Deploy no Surge + verificação HTTP 200",
        function=step_deploy,
        depends_on=["index", "changelog"],
        required=False,  # Deploy falha não para pipeline (pode rodar manual depois)
    ),
]

STEP_MAP = {s.name: s for s in STEPS}

# ============================================================
# EXECUÇÃO DO PIPELINE
# ============================================================

def topological_sort(steps: List[BuildStep], selected: List[str]) -> List[List[BuildStep]]:
    """Retorna lista de 'ondas' de passos que podem rodar em paralelo."""
    selected_steps = [s for s in steps if s.name in selected]
    name_to_step = {s.name: s for s in selected_steps}
    remaining = set(name_to_step.keys())
    completed = set()
    waves = []

    while remaining:
        # Passos cujas dependências já foram completadas (estão em 'completed')
        ready = [name_to_step[n] for n in remaining
                 if all(dep in completed for dep in name_to_step[n].depends_on)]
        if not ready:
            # Dependência circular ou missing
            missing = [n for n in remaining if n not in name_to_step]
            if missing:
                raise ValueError(f"Passos dependem de passos não selecionados: {missing}")
            raise ValueError("Dependência circular detectada")

        waves.append(ready)
        for s in ready:
            remaining.remove(s.name)
            completed.add(s.name)

    return waves

def run_pipeline(ctx: BuildContext, steps_to_run: List[str], parallel: bool = False) -> int:
    waves = topological_sort(STEPS, steps_to_run)

    for wave_idx, wave in enumerate(waves):
        ctx.log(f"=== Onda {wave_idx + 1}/{len(waves)}: {[s.name for s in wave]} ===")

        if parallel and len(wave) > 1 and wave[0].parallel_group:
            # Executa em paralelo
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(wave)) as executor:
                futures = {executor.submit(s.function, ctx): s for s in wave}
                for future in concurrent.futures.as_completed(futures):
                    step = futures[future]
                    try:
                        success = future.result()
                        ctx.step_done(step.name, success)
                        if not success and step.required:
                            ctx.log(f"Passo obrigatório '{step.name}' falhou. Parando pipeline.", "ERROR")
                            return 1
                    except Exception as e:
                        ctx.log(f"Exceção no passo '{step.name}': {e}", "ERROR")
                        ctx.step_done(step.name, False)
                        if step.required:
                            return 1
        else:
            # Executa sequencial
            for step in wave:
                ctx.log(f"Executando passo: {step.name} — {step.description}")
                try:
                    success = step.function(ctx)
                    ctx.step_done(step.name, success)
                    if not success and step.required:
                        ctx.log(f"Passo obrigatório '{step.name}' falhou. Parando pipeline.", "ERROR")
                        return 1
                except Exception as e:
                    ctx.log(f"Exceção no passo '{step.name}': {e}", "ERROR")
                    ctx.step_done(step.name, False)
                    if step.required:
                        return 1

    # Resumo final
    ctx.log("=== Resumo do Pipeline ===")
    for step_name, status in ctx.step_results.items():
        icon = {"success": "[OK]", "failed": "[FAIL]", "skipped": "[SKIP]"}.get(status.value, "[?]")
        # Marca passos opcionais
        step_obj = STEP_MAP.get(step_name)
        optional_tag = " [opcional]" if step_obj and not step_obj.required else ""
        ctx.log(f"  {icon} {step_name}{optional_tag}")

    # Só conta falhas em passos obrigatórios
    failed_required = [
        n for n, s in ctx.step_results.items()
        if s == StepStatus.FAILED and STEP_MAP.get(n, BuildStep("", "", lambda _: True, required=True)).required
    ]
    if failed_required:
        ctx.log(f"Falhas obrigatorias: {', '.join(failed_required)}", "ERROR")
        return 1

    # Loga falhas opcionais mas não falha o pipeline
    failed_optional = [
        n for n, s in ctx.step_results.items()
        if s == StepStatus.FAILED and not STEP_MAP.get(n, BuildStep("", "", lambda _: True, required=True)).required
    ]
    if failed_optional:
        ctx.log(f"Falhas opcionais (ignoradas): {', '.join(failed_optional)}", "WARN")

    ctx.log("Pipeline concluído com sucesso!")
    return 0

# ============================================================
# CLI
# ============================================================

def list_steps():
    print("Passos disponiveis (ordem de execucao):")
    for i, step in enumerate(STEPS, 1):
        deps = f" (deps: {', '.join(step.depends_on)})" if step.depends_on else ""
        parallel = f" [paralelo: {step.parallel_group}]" if step.parallel_group else ""
        required = "" if step.required else " [opcional]"
        print(f"  {i}. {step.name}{deps}{parallel}{required} - {step.description}")

def main():
    parser = argparse.ArgumentParser(description="Orquestrador de Build - Resumos Hermes")
    parser.add_argument("steps", nargs="*", default=["all"],
                        help="Passos a executar (padrão: all = pipeline completo)")
    parser.add_argument("--list-steps", action="store_true", help="Lista passos disponíveis")
    parser.add_argument("--parallel", action="store_true", help="Executa passos independentes em paralelo")
    parser.add_argument("--verbose", "-v", action="store_true", help="Output verboso dos subprocessos")
    parser.add_argument("--dry-run", action="store_true", help="Mostra ordem de execução sem executar")

    args = parser.parse_args()

    if args.list_steps:
        list_steps()
        return 0

    # Resolve "all" para todos os passos
    if "all" in args.steps:
        steps_to_run = [s.name for s in STEPS]
    else:
        steps_to_run = args.steps

    # Auto-inclui dependências transitivas
    expanded = set(steps_to_run)
    changed = True
    while changed:
        changed = False
        for step in STEPS:
            if step.name in expanded:
                for dep in step.depends_on:
                    if dep not in expanded:
                        expanded.add(dep)
                        changed = True
    steps_to_run = list(expanded)

    # Valida passos
    invalid = [s for s in steps_to_run if s not in STEP_MAP]
    if invalid:
        print(f"Passos inválidos: {', '.join(invalid)}")
        print("Use --list-steps para ver disponíveis.")
        return 1

    if args.dry_run:
        waves = topological_sort(STEPS, steps_to_run)
        print("Ordem de execução (ondas paralelas):")
        for i, wave in enumerate(waves, 1):
            names = ", ".join(s.name for s in wave)
            print(f"  Onda {i}: {names}")
        return 0

    ctx = BuildContext(
        root=ROOT,
        design_system=DESIGN_SYSTEM,
        template_thin=TEMPLATE_THIN,
        template_out=TEMPLATE_OUT,
        resumos_dir=RESUMOS_DIR,
        search_index=SEARCH_INDEX,
        changelog=CHANGELOG,
        verbose=args.verbose,
        parallel=args.parallel,
    )

    return run_pipeline(ctx, steps_to_run, parallel=args.parallel)


if __name__ == "__main__":
    sys.exit(main())