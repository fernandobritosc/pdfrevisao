# -*- coding: utf-8 -*-
"""Gera search-index.json com o texto de todos os resumos (busca full-text no index).

Uso: python build-search-index.py
Saida: Resumo_estudos/search-index.json
Rodar sempre que um resumo for criado/atualizado (fluxo /nova-aula).
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
OUT = os.path.join(ROOT, "search-index.json")

SKIP_TAGS = {"script", "style", "nav", "aside", "header", "footer"}
SECTION_RE = re.compile(r"<section\b[^>]*>", re.I)
SEC_ID_RE = re.compile(r'id="(sec[^"]*)"', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)


class TextExtractor(HTMLParser):
    def __init__(self, skip_ids=None):
        super().__init__()
        self.skip_ids = skip_ids or set()
        self.depth = 0
        self.in_skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS or (tag == "div" and dict(attrs).get("id") in self.skip_ids):
            self.in_skip += 1
        self.depth += 1

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS or tag == "div":
            if self.in_skip > 0:
                self.in_skip -= 1
        self.depth -= 1

    def handle_data(self, data):
        if self.in_skip == 0:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\s+", " ", html.unescape("".join(self.parts))).strip()


def extract_sections(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    title = TITLE_RE.search(raw)
    title = title.group(1).strip() if title else os.path.basename(path)
    out = []
    for m in SECTION_RE.finditer(raw):
        sec_tag = m.group(0)
        sec_id = (SEC_ID_RE.search(sec_tag) or [None, ""])[1]
        sec_raw = raw[m.end():]
        nxt = SECTION_RE.search(sec_raw)
        body = sec_raw if not nxt else sec_raw[:nxt.start()]
        parser = TextExtractor()
        parser.feed(body)
        txt = parser.text()
        if len(txt) < 30:
            continue
        sec_title = ""
        tm = re.search(r'<div class="sec-title">(.*?)</div>', body, re.I | re.S)
        if tm:
            sec_title = re.sub(r"<[^>]+>", "", tm.group(1)).strip()
        out.append({"s": sec_id, "t": sec_title, "x": txt})
    return title, out


def main():
    items = []
    n_files = 0
    for mat in sorted(os.listdir(ROOT)):
        mat_path = os.path.join(ROOT, mat)
        if not os.path.isdir(mat_path):
            continue
        for aula in sorted(os.listdir(mat_path)):
            aula_path = os.path.join(mat_path, aula)
            if not os.path.isdir(aula_path):
                continue
            for fname in sorted(os.listdir(aula_path)):
                if not fname.startswith("resumo-") or not fname.endswith(".html"):
                    continue
                path = os.path.join(aula_path, fname)
                title, secs = extract_sections(path)
                if not secs:
                    continue
                rel = os.path.join(mat, aula, fname).replace(os.sep, "/")
                for sec in secs:
                    items.append({
                        "u": rel,
                        "m": mat,
                        "a": title,
                        "s": sec["s"],
                        "t": sec["t"],
                        "x": sec["x"],
                    })
                n_files += 1
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(OUT) / 1024
    print("resumos indexados: %d | itens (seções): %d | tamanho: %.0f KB" % (n_files, len(items), size))
    print("saída:", OUT)


if __name__ == "__main__":
    sys.exit(main())