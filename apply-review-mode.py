# -*- coding: utf-8 -*-
"""Aplica o modo revisão (active recall) nos resumos: botão 🧠 no toolbar,
CSS que oculta conteúdo de estudo e JS que revela por clique.

Uso: python apply-review-mode.py
Idempotente: arquivos com id="rhRev" são pulados.

Refatorado para usar apply_shared.HtmlInjectionEngine + REV_CONFIG.
"""
import glob
import os
import sys

# Adiciona tools ao path para importar apply_shared
TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from apply_shared import HtmlInjectionEngine, REV_CONFIG, TOOLBAR_CSS

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [
    os.path.join(ROOT, "*", "Aula *", "resumo-*.html"),
    os.path.join(ROOT, "templates", "template-sumario.html"),
]

engine = HtmlInjectionEngine(verbose=True)


def apply(path: str) -> bool:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    new_content = engine.apply(content, REV_CONFIG)
    if new_content is None:
        return False

    # Reparo extra: garante toolbar CSS se não existir (para arquivos antigos sem rh-addons)
    if "rh-toolbar" not in new_content and "rh-toolbar" not in content:
        # Injeta CSS do toolbar antes de </style>
        idx = new_content.rfind("</style>")
        if idx != -1:
            new_content = new_content[:idx] + TOOLBAR_CSS + new_content[idx:]

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