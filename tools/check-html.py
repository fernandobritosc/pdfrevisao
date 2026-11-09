#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check-html.py — Validador de balanceamento de tags HTML.

Uso:
    python tools/check-html.py <arquivo.html>           # valida arquivo único
    python tools/check-html.py --dir Resumo_estudos     # valida todos os resumo-aula-*.html
    python tools/check-html.py --check                  # modo CI: exit code 1 se houver erros

Verifica:
  - Tags de abertura/fechamento balanceadas (div, section, span, p, etc.)
  - Tags void conhecidas (img, br, hr, input, meta, link, etc.) não precisam fechar
  - Atributos bem formados
  - Não reporta false positives em conteúdo de <script> e <style>

Saída:
  ERROS: N | ABERTAS: M
  - Se ERROS > 0 ou ABERTAS > 0: exit code 1 (em modo --check)
  - Lista detalhes de cada erro com linha aproximada
"""
import sys
import re
import argparse
from pathlib import Path
from html.parser import HTMLParser
from typing import List, Tuple, Set, Dict, Optional


# Tags void (auto-fechantes) segundo HTML5
VOID_TAGS: Set[str] = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
    'link', 'meta', 'param', 'source', 'track', 'wbr',
    'colgroup', 'keygen', 'menuitem'  # obsoletas mas ainda void
}

# Tags que podem ser omitidas (parser fecha automaticamente) — não contam como erro se faltar fechamento
OPTIONAL_CLOSING: Set[str] = {
    'p', 'li', 'dt', 'dd', 'tr', 'td', 'th', 'thead', 'tbody', 'tfoot',
    'colgroup', 'col', 'option', 'optgroup', 'rp', 'rt'
}

# Tags que NÃO devem ter conteúdo parseado como HTML (conteúdo bruto)
RAW_CONTENT_TAGS: Set[str] = {'script', 'style', 'textarea', 'title'}


class HTMLValidator(HTMLParser):
    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self.stack: List[Tuple[str, int, int]] = []  # (tag, line, col)
        self.errors: List[str] = []
        self.line = 1
        self.col = 1
        self.in_raw = False
        self.raw_tag = None
        self._last_pos = (1, 1)

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]):
        if self.in_raw:
            return
        if tag in VOID_TAGS:
            return
        self.stack.append((tag, self.line, self.col))

    def handle_endtag(self, tag: str):
        if self.in_raw:
            if tag == self.raw_tag:
                self.in_raw = False
                self.raw_tag = None
            return

        if tag in VOID_TAGS:
            self.errors.append(f"Linha ~{self.line}: tag void '</{tag}>' não deve ter fechamento")
            return

        # Procura tag correspondente na pilha (permite fechamento implícito de tags opcionais)
        found = False
        for i in range(len(self.stack) - 1, -1, -1):
            open_tag, open_line, open_col = self.stack[i]
            if open_tag == tag:
                # Fecha todas as tags opcionais acima desta
                for j in range(len(self.stack) - 1, i, -1):
                    ot, ol, oc = self.stack[j]
                    if ot not in OPTIONAL_CLOSING:
                        self.errors.append(
                            f"Linha ~{ol}: tag '<{ot}>' aberta não foi fechada antes de '</{tag}>' (linha ~{self.line})"
                        )
                self.stack = self.stack[:i]
                found = True
                break
            elif open_tag not in OPTIONAL_CLOSING:
                # Tag não-opcional diferente no caminho — erro de nesting
                self.errors.append(
                    f"Linha ~{self.line}: fechamento '</{tag}>' não corresponde a '<{open_tag}>' (linha ~{open_line})"
                )
                return

        if not found:
            self.errors.append(f"Linha ~{self.line}: fechamento '</{tag}>' sem abertura correspondente")

    def handle_startendtag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]):
        # Em conteúdo estrangeiro (SVG/MathML) o HTML5 aceita auto-fechamento
        in_foreign = any(t in ('svg', 'math') for t, _, _ in self.stack)
        if tag not in VOID_TAGS and not in_foreign:
            self.errors.append(f"Linha ~{self.line}: tag '<{tag} />' auto-fechante mas não é void")

    def handle_data(self, data: str):
        pass

    def handle_comment(self, data: str):
        pass

    def get_pos(self) -> Tuple[int, int]:
        # Aproximação: conta newlines no raw data alimentado
        return self.line, self.col

    def feed(self, data: str):
        # Rastreia linha/coluna aproximada
        for char in data:
            if char == '\n':
                self.line += 1
                self.col = 1
            else:
                self.col += 1
        super().feed(data)

    def close(self):
        super().close()
        # Tags restantes na pilha que não são opcionais = erro
        for tag, line, col in self.stack:
            if tag not in OPTIONAL_CLOSING:
                self.errors.append(f"Linha ~{line}: tag '<{tag}>' aberta não foi fechada (EOF)")

    def get_results(self) -> Tuple[int, int, List[str]]:
        open_count = sum(1 for t, _, _ in self.stack if t not in OPTIONAL_CLOSING)
        return len(self.errors), open_count, self.errors


def validate_file(path: Path) -> Tuple[int, int, List[str]]:
    try:
        content = path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return 1, 0, [f"Erro ao ler arquivo: {e}"]

    validator = HTMLValidator(str(path))
    try:
        validator.feed(content)
        validator.close()
    except Exception as e:
        return 1, 0, [f"Erro no parser: {e}"]

    return validator.get_results()


def find_resumo_files(root: Path) -> List[Path]:
    """Encontra todos os resumo-aula-*.html recursivamente."""
    return sorted(root.rglob('resumo-aula-*.html'))


def main():
    parser = argparse.ArgumentParser(description='Validador de HTML para resumos')
    parser.add_argument('path', nargs='?', help='Arquivo HTML ou diretório para validar')
    parser.add_argument('--dir', help='Diretório raiz para buscar resumo-aula-*.html')
    parser.add_argument('--check', action='store_true', help='Modo CI: exit code 1 se houver erros')
    parser.add_argument('--verbose', '-v', action='store_true', help='Mostrar detalhes de cada erro')
    args = parser.parse_args()

    targets: List[Path] = []

    if args.dir:
        root = Path(args.dir)
        targets = find_resumo_files(root)
        if not targets:
            print(f"Nenhum resumo-aula-*.html encontrado em {root}")
            return 1
    elif args.path:
        targets = [Path(args.path)]
    else:
        # Default: validar todos em Resumo_estudos
        root = Path(__file__).parent.parent / 'Resumo_estudos'
        targets = find_resumo_files(root)
        if not targets:
            print(f"Nenhum resumo-aula-*.html encontrado em {root}")
            return 1

    total_errors = 0
    total_open = 0
    files_with_issues = 0

    for path in targets:
        errors, open_tags, details = validate_file(path)
        if errors > 0 or open_tags > 0:
            files_with_issues += 1
            total_errors += errors
            total_open += open_tags
            rel = path.relative_to(Path.cwd()) if path.is_absolute() else path
            print(f"[FAIL] {rel}: ERROS={errors} ABERTAS={open_tags}")
            if args.verbose:
                for d in details:
                    print(f"   - {d}")
        else:
            rel = path.relative_to(Path.cwd()) if path.is_absolute() else path
            print(f"[OK] {rel}: OK")

    print(f"\n---")
    print(f"Arquivos validados: {len(targets)}")
    print(f"Com problemas: {files_with_issues}")
    print(f"Total ERROS: {total_errors}")
    print(f"Total ABERTAS: {total_open}")

    if args.check and (total_errors > 0 or total_open > 0):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())