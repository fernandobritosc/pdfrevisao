# -*- coding: utf-8 -*-
"""Aplica o modo revisão (active recall) nos resumos: botão 🧠 no toolbar,
CSS que oculta conteúdo de estudo e JS que revela por clique.

Uso: python apply-review-mode.py
Idempotente: arquivos com id="rhRev" são pulados.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [
    os.path.join(ROOT, "*", "Aula *", "resumo-*.html"),
    os.path.join(ROOT, "templates", "template-sumario.html"),
]

BUTTON = '\n  <button type="button" id="rhRev" title="Modo revisão: oculte e se auto-teste" aria-label="Alternar modo revisão" aria-pressed="false">\U0001F9E0</button>'

CSS = """
/* ===== RH modo revisão (active recall) ===== */
html.rh-rev .card-text, html.rh-rev .gotcha, html.rh-rev .callout, html.rh-rev .table-wrap,
html.rh-rev .mnemonic-content, html.rh-rev .question-text, html.rh-rev .answer { display: none; }
html.rh-rev .card, html.rh-rev .gotcha, html.rh-rev .callout, html.rh-rev .table-wrap,
html.rh-rev .mnemonic, html.rh-rev .question { cursor: pointer; }
html.rh-rev .card.rev-open .card-text, html.rh-rev .gotcha.rev-open, html.rh-rev .callout.rev-open,
html.rh-rev .table-wrap.rev-open, html.rh-rev .mnemonic.rev-open .mnemonic-content,
html.rh-rev .question.rev-open .question-text, html.rh-rev .question.rev-open .answer { display: block; }
html.rh-rev .card.rev-open, html.rh-rev .gotcha.rev-open { border-color: var(--amber); }
.rh-toolbar button.on { border-color: var(--amber); background: #fdf3d8; }
html[data-theme="dark"] .rh-toolbar button.on { background: #33290f; border-color: #6e5a1e; }
"""

JS = """
<script id="rh-rev">
(function(){
  var b=document.getElementById('rhRev'); if(!b) return;
  var root=document.documentElement;
  function on(){return root.classList.contains('rh-rev');}
  function apply(){
    var now=!on();
    root.classList.toggle('rh-rev', now);
    b.classList.toggle('on', now);
    try{localStorage.setItem('rh-rev', now?'1':'0');}catch(e){}
    b.setAttribute('aria-pressed', now?'true':'false');
  }
  b.addEventListener('click', apply);
  try{ if(localStorage.getItem('rh-rev')==='1') apply(); }catch(e){}
  document.addEventListener('click', function(ev){
    if(!on()) return;
    var el = ev.target && ev.target.closest ? ev.target.closest('.card,.gotcha,.callout,.table-wrap,.mnemonic,.question') : null;
    if(!el || ev.target.closest('a')) return;
    el.classList.toggle('rev-open');
  });
})();
</script>
"""


def apply(path):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    if "id=\"rhRev\"" in content:
        return False
    n = content.count("id=\"rhTop\"")
    if n != 1:
        print("!! toolbar inesperado (%d rhTop): %s" % (n, os.path.relpath(path, ROOT)))
    content = re.sub(r'(id="rhTop"[^>]*>↑</button>)', r"\1" + BUTTON, content, count=1)
    idx = content.rfind("</style>")
    if idx == -1:
        print("!! sem </style>: %s" % os.path.relpath(path, ROOT))
    else:
        content = content[:idx] + CSS + content[idx:]
    idx = content.rfind("<!--/rh:ui-->")
    if idx == -1:
        print("!! sem marcador rh:ui: %s" % os.path.relpath(path, ROOT))
    else:
        content = content[:idx] + JS + "\n" + content[idx:]
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