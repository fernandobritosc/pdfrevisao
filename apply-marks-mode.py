# -*- coding: utf-8 -*-
"""Aplica a marcação pessoal (vacilo) nos resumos: botão 🏷 no toolbar,
marca cards/blocos em vermelho com persistência em localStorage,
export/import de backup JSON.

Uso: python apply-marks-mode.py
Idempotente: arquivos com id="rhMarks" são pulados.

Refatorado para usar apply_shared.HtmlInjectionEngine + MARKS_CONFIG.
"""
import glob
import os
import sys

# Adiciona tools ao path para importar apply_shared
TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from apply_shared import HtmlInjectionEngine, MARKS_CONFIG, TOOLBAR_CSS, ensure_rev_button

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [
    os.path.join(ROOT, "*", "Aula *", "resumo-*.html"),
    os.path.join(ROOT, "templates", "template-sumario.html"),
]

engine = HtmlInjectionEngine(verbose=True)


def apply(path: str) -> bool:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    new_content = engine.apply(content, MARKS_CONFIG)
    if new_content is None:
        return False

    # Reparo extra: garante toolbar CSS + botão 🧠 se não existirem
    if "rh-toolbar" not in new_content and "rh-toolbar" not in content:
        idx = new_content.rfind("</style>")
        if idx != -1:
            new_content = new_content[:idx] + TOOLBAR_CSS + new_content[idx:]
    new_content = ensure_rev_button(new_content)

    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_content)
    return True


def main():
    total = 0
    for pattern in GLOBS:
        for path in sorted(glob.glob(pattern)):
            if apply(path):
                total += 1
                print("aplicado:", os.path.relpath(path, ROOT))
    print("total aplicados:", total)


if __name__ == "__main__":
    sys.exit(main())