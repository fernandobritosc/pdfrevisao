#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check-links.py — Verificador de links locais dos HTML do site.

Uso:
    python tools/check-links.py              # valida Resumo_estudos/
    python tools/check-links.py --dir <dir>  # outro diretório raiz do site

O que faz:
  - Percorre todos os *.html do diretório do site (raiz = diretório passado).
  - Extrai atributos href="..." e src="..." (aspas simples ou duplas).
  - Ignora links externos (http/https/mailto/tel/javascript/data/# puro tratado localmente),
    e resolve caminhos:
      "/caminho"        -> relativo à RAIZ do site (o que o Surge publica)
      "relativo/x.html" -> relativo ao arquivo que contém o link
  - Verifica existência do arquivo-alvo (com decodificação de %XX).
  - Verifica fragmentos (#sec-n): procura id="..." no arquivo-alvo (e na mesma página).
  - Contadores no final; exit code 1 se houver quebras (modo --check).
"""
import argparse
import html
import re
import sys
import urllib.parse
from pathlib import Path

SITE_ROOT_DEFAULT = Path(__file__).resolve().parent.parent / "Resumo_estudos"
ATTR_RE = re.compile(r"\b(?:href|src)\s*=\s*(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
ID_RE = re.compile(r"\bid\s*=\s*(['\"])(.*?)\1", re.IGNORECASE)

def is_external(ref: str) -> bool:
    r = ref.strip().lower()
    return (r.startswith(("http://", "https://", "mailto:", "tel:", "javascript:",
                          "data:", "ftp:", "//")))

def strip_fragment(ref: str):
    if "#" in ref:
        path, frag = ref.split("#", 1)
        return path, urllib.parse.unquote(frag)
    return ref, ""

def collect_ids(path: Path) -> set:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return set()
    return {html.unescape(m.group(2)) for m in ID_RE.finditer(text)}

def check_dir(site_dir: Path):
    html_files = sorted(site_dir.rglob("*.html"))
    ids_cache = {}
    problems = []
    checked = 0
    for f in html_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        for m in ATTR_RE.finditer(text):
            raw = html.unescape(m.group(2)).strip()
            if not raw or is_external(raw):
                continue
            # ignora refs dinâmicas geradas por JS (template de busca etc.)
            if any(ch in raw for ch in ("'", '+', '${', '}', '{{', '<%', '\n')) or raw.startswith("("):
                continue
            path_part, frag = strip_fragment(raw)
            checked += 1
            if path_part == "":
                target = f  # mesmo arquivo
            else:
                path_part = urllib.parse.unquote(path_part.split("?", 1)[0])
                p = Path(path_part)
                target = (site_dir / p.relative_to("/")) if p.is_absolute() else (f.parent / p).resolve()
            try:
                target.relative_to(site_dir.resolve())
            except ValueError:
                problems.append((f, raw, "aponta para fora da raiz do site"))
                continue
            if not target.exists():
                problems.append((f, raw, "arquivo não encontrado"))
                continue
            if frag:
                if target.suffix.lower() == ".html" or target == f:
                    ids = ids_cache.setdefault(target, collect_ids(target))
                    if frag not in ids:
                        problems.append((f, raw, f"fragmento #{frag} não encontrado"))
    return html_files, checked, problems

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(SITE_ROOT_DEFAULT))
    args = ap.parse_args()
    site_dir = Path(args.dir).resolve()
    if not site_dir.is_dir():
        print(f"ERRO: diretório não encontrado: {site_dir}", file=sys.stderr)
        return 2
    html_files, checked, problems = check_dir(site_dir)
    print(f"arquivos HTML: {len(html_files)} | links locais verificados: {checked} | quebras: {len(problems)}")
    for f, ref, reason in problems:
        print(f"  QUEBRA: {f.relative_to(site_dir)} -> {ref} ({reason})")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
