# -*- coding: utf-8 -*-
"""Aplica o PWA offline nos resumos: manifest link + apple-touch-icon +
theme-color + registro do service worker no head de todas as páginas.

Uso: python apply-pwa.py
Idempotente: arquivos com manifest.webmanifest no head são pulados.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [
    os.path.join(ROOT, "index.html"),
    os.path.join(ROOT, "*", "Aula *", "resumo-*.html"),
    os.path.join(ROOT, "templates", "template-sumario.html"),
]

HEAD = """
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/icons/icon-180.png">
<meta name="theme-color" content="#F5F4F0">
<script>
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
  navigator.serviceWorker.register('/sw.js').catch(function () {});
}
</script>
</head>"""


def apply(path):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    if 'rel="manifest"' in content:
        return False
    idx = content.rfind("</head>")
    if idx == -1:
        print("!! sem </head>: %s" % os.path.relpath(path, ROOT))
        return False
    content = content[:idx] + HEAD + content[idx + len("</head>"):]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
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