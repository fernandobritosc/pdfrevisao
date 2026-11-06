# -*- coding: utf-8 -*-
"""
apply-a11y.py — pacote de acessibilidade e navegação mobile nos resumos.

Injeta (idempotente, marcador id="rh-nav-mobile"):
  - skip link "Pular para o conteúdo" (primeiro focável do body);
  - botão ☰ fixo no canto inferior esquerdo em <=900px, que abre o sidebar
    como gaveta (o CSS das páginas esconde o sidebar nesse breakpoint);
  - backdrop, fechamento por Esc/backdrop/link, foco devolvido ao botão;
  - scroll spy marcando a seção visível (`.rh-current` + aria-current="location").

Patch estático (também idempotente):
  - id="conteudo" + tabindex="-1" no container principal (alvo do skip link);
  - scope="col" em todos os <th> (todos vivem dentro de <thead>);
  - role="status" + aria-live="polite" nos contadores de busca e de prática;
  - fallback de cor antes do color-mix nas tiras .tldr (iOS < 16.2).

Uso: python apply-a11y.py            (todos os resumo-aula-*.html + templates)
     python apply-a11y.py ARQUIVO    (um arquivo específico)

Roda depois de regenerar resumos pelo template (padrão dos demais apply-*.py).
"""
import glob
import io
import os
import re
import sys

# Adiciona tools ao path para importar apply_shared
TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from apply_shared import A11Y_CONFIG, A11Y_SKIP_CONFIG, HtmlInjectionEngine

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
EXTRA_TARGETS = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "template-thin.html"),
    os.path.join(ROOT, "templates", "template-sumario.html"),
    os.path.join(ROOT, "index.html"),
    os.path.join(ROOT, "tce-go-trilha.html"),
    os.path.join(ROOT, "mudancas.html"),
]

engine = HtmlInjectionEngine(verbose=True)

TH_RE = re.compile(r"<th(?=[\s>])(?![^>]*\bscope=)")
TLDR_RE = re.compile(r"\.tldr\{[^}]*\}")
CM_RE = re.compile(r"background:\s*(color-mix\([^;}]*\))")
TLDR_FALLBACK = {
    "var(--purple)": "rgba(124,58,237,.1)",
    "var(--mat)": "var(--mat-soft,rgba(31,39,51,.05))",
}
HOVER_FALLBACK = "rgba(31,39,51,.035)"


def _with_fallback(scope: str, fallback_for) -> str:
    out, last = [], 0
    for match in CM_RE.finditer(scope):
        before = scope[last:match.start()]
        if re.search(r"background\s*:[^;]+;\s*$", before):
            out.append(before + match.group(0))
        else:
            var = re.search(r"var\(--[a-z-]+\)", match.group(1))
            out.append(before + "background:" + fallback_for(var.group(0) if var else "") + ";" + match.group(0))
        last = match.end()
    out.append(scope[last:])
    return "".join(out)


def _color_mix_fallback(html: str) -> str:
    # 1) tiras .tldr: mantém o tom da matéria no fallback
    html = TLDR_RE.sub(
        lambda m: _with_fallback(m.group(0), lambda v: TLDR_FALLBACK.get(v, "rgba(31,39,51,.05)")),
        html,
    )
    # 2) demais (hover de tabela): fallback neutro discreto
    return _with_fallback(html, lambda v: HOVER_FALLBACK)


def static_patches(html: str) -> str:
    if 'id="conteudo"' not in html:
        html = html.replace('<div class="main">', '<div class="main" id="conteudo" tabindex="-1">')
        html = html.replace('<div class="container">', '<div class="container" id="conteudo" tabindex="-1">')
        html = re.sub(r'<(div|main)(\s+class="sheet")', r'<\1\2 id="conteudo" tabindex="-1"', html, count=1)
    html = TH_RE.sub('<th scope="col"', html)
    html = html.replace('<span id="sr-count">', '<span id="sr-count" role="status" aria-live="polite">')
    html = html.replace('<span class="rhpp-score" id="rhPracticeScore">',
                        '<span class="rhpp-score" id="rhPracticeScore" role="status" aria-live="polite">')
    # explicação do quiz (blocos de prática injetados antes do aria-live no gerador)
    if "why.setAttribute('role', 'status')" not in html:
        html = html.replace(
            "var why = document.createElement('div'); why.className = 'rhpp-why';",
            "var why = document.createElement('div'); why.className = 'rhpp-why';\n"
            "          why.setAttribute('role', 'status'); why.setAttribute('aria-live', 'polite');",
        )
    return _color_mix_fallback(html)


def apply(path: str) -> str:
    """Retorna 'updated', 'skip' ou 'error'."""
    with io.open(path, encoding="utf-8") as fh:
        content = fh.read()

    # Páginas sem sidebar (sketchnotes, index, trilha, mudanças) recebem só
    # skip link + patches estáticos — o botão ☰ não teria o que abrir.
    config = A11Y_CONFIG if 'class="sidebar"' in content else A11Y_SKIP_CONFIG
    marker = 'id="rh-nav-mobile"' if config is A11Y_CONFIG else 'class="rh-skip"'

    new_content = content
    if marker not in content:
        injected = engine.apply(content, config)
        if injected is None:
            print("FALHA (âncora de injeção não encontrada):", os.path.relpath(path, ROOT))
            return "error"
        new_content = injected
    new_content = static_patches(new_content)

    if new_content == content:
        return "skip"
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_content)
    return "updated"


def main():
    targets = sys.argv[1:] or sorted(
        glob.glob(os.path.join(ROOT, "**", "resumo-aula-*.html"), recursive=True)
        + glob.glob(os.path.join(ROOT, "**", "sketchnote-*.html"), recursive=True)
        + glob.glob(os.path.join(ROOT, "**", "mapa-mental-*.html"), recursive=True)
        + glob.glob(os.path.join(ROOT, "*", "index.html"))
    ) + [t for t in EXTRA_TARGETS if os.path.exists(t)]

    updated = skipped = errors = 0
    for f in targets:
        result = apply(f)
        if result == "updated":
            updated += 1
            print("atualizado:", os.path.relpath(f, ROOT))
        elif result == "skip":
            skipped += 1
        else:
            errors += 1
    print("---")
    print("atualizados:", updated, "| já atualizados:", skipped, "| falhas:", errors)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
