#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check-glossary.py - Valida uso de vocabulário oficial do GLOSSARY.md em arquivos de review/ADR.

Uso:
    python tools/check-glossary.py [arquivo.md ...]
    python tools/check-glossary.py --all    # Verifica todos .md em docs/adr/ e reviews
"""

import re
import sys
from pathlib import Path
from typing import Set, List, Tuple

ROOT = Path(__file__).parent.parent
GLOSSARY = ROOT / "GLOSSARY.md"
ADR_DIR = ROOT / "docs" / "adr"

# Termos oficiais do dominio (extraidos do GLOSSARY.md)
OFFICIAL_TERMS: Set[str] = {
    # Entidades principais
    "resumo", "aula", "secao", "card", "callout", "gotcha",
    "tag", "incidencia", "trilha", "sketchnote", "quiz",
    "materia",
    # Conceitos de arquitetura
    "modulo", "interface", "profundidade", "costura", "adapter",
    "alavancagem", "localidade", "teste da delecao",
}

# Termos proibidos (devem ser substituidos pelos oficiais)
FORBIDDEN_TERMS: dict[str, str] = {
    "componente": "modulo",
    "servico": "modulo / adapter",
    "api": "interface",
    "boundary": "costura",
    "feature": "modulo / funcionalidade",
    "service": "modulo / adapter",
    "component": "modulo",
}

# Padroes para encontrar termos no texto (case-insensitive, word boundaries)
TERM_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(t) for t in OFFICIAL_TERMS) + r')\b', re.IGNORECASE)
FORBIDDEN_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(t) for t in FORBIDDEN_TERMS.keys()) + r')\b', re.IGNORECASE)


def check_file(path: Path):
    """Retorna (termos_oficiais_encontrados, termos_proibidos_encontrados)."""
    content = path.read_text(encoding="utf-8", errors="replace")

    found_official = set()
    for match in TERM_PATTERN.finditer(content):
        found_official.add(match.group(1).lower())

    found_forbidden = []
    for match in FORBIDDEN_PATTERN.finditer(content):
        forbidden = match.group(1).lower()
        suggested = FORBIDDEN_TERMS.get(forbidden, "?")
        found_forbidden.append(f"{forbidden} -> use '{suggested}'")

    return (sorted(found_official), found_forbidden)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Valida vocabulario do GLOSSARY.md")
    parser.add_argument("files", nargs="*", help="Arquivos para verificar")
    parser.add_argument("--all", action="store_true", help="Verifica todos .md em docs/adr/")
    parser.add_argument("--strict", action="store_true", help="Falha se termos proibidos encontrados")
    args = parser.parse_args()

    targets = []
    if args.all:
        targets.extend(ADR_DIR.glob("*.md"))
        targets.extend(ROOT.glob("*review*.md"))
        targets.extend(ROOT.glob("*architecture*.md"))
    else:
        targets = [Path(f) for f in args.files]

    if not targets:
        print("Nenhum arquivo para verificar. Use --all ou passe arquivos.")
        return 1

    all_ok = True
    for path in sorted(targets):
        if not path.exists():
            print(f"[SKIP] {path} (nao existe)")
            continue

        official, forbidden = check_file(path)
        rel = path.relative_to(ROOT)

        if official:
            print(f"[OK] {rel}: termos oficiais - {', '.join(official)}")
        else:
            print(f"[WARN] {rel}: nenhum termo oficial do GLOSSARY encontrado")

        if forbidden:
            print(f"[FORBIDDEN] {rel}:")
            for f in forbidden:
                print(f"  - {f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())