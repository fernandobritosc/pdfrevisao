# -*- coding: utf-8 -*-
"""
apply-search.py — injeta o campo de busca por palavra (filtro + destaque) nos resumos.
Idempotente: pula arquivos que já tenham id="sr-script". Reexecutar após regenerar
resumos pelo template (padrão dos demais apply-*.py).

Uso: python apply-search.py            (todos os resumo-aula-*.html de Resumo_estudos)
     python apply-search.py ARQUIVO    (um arquivo específico)
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resumo_estudos')

SR_BOX = (
    '  <div class="sr-box">\n'
    '    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">\n'
    '    <div class="sr-info"><span id="sr-count"></span><button id="sr-clear" type="button">limpar</button></div>\n'
    '  </div>\n'
)

SR_STYLE = '''<style id="sr-style">
.sr-box { padding: .55rem .2rem .2rem; }
#sr-input {
  width: 100%; box-sizing: border-box; background: var(--card, #fff);
  border: 1px solid var(--border, #e2dfd7); border-radius: 8px; padding: .42rem .6rem;
  color: var(--text, #1f2733); font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace; font-size: .72rem;
}
#sr-input:focus { outline: none; border-color: var(--mat, var(--blue, #2563eb)); }
.sr-info {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: .3rem; font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
  font-size: .62rem; color: var(--text2, #455064);
}
#sr-clear {
  background: none; border: none; padding: 0; cursor: pointer;
  color: var(--mat-strong, var(--blue, #2563eb)); font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace; font-size: .62rem;
}
#sr-clear:hover { text-decoration: underline; }
.sr-hide { display: none !important; }
section.sr-empty { opacity: .4; }
mark.sr-hit {
  background: rgba(217, 119, 6, .55); color: inherit;
  border-radius: 3px; padding: 0 1px; box-shadow: 0 0 0 1px rgba(217, 119, 6, .35);
}
[data-theme="dark"] mark.sr-hit { background: rgba(240, 169, 46, .45); }
mark.sr-first {
  background: rgba(220, 38, 38, .55); box-shadow: 0 0 0 2px rgba(220, 38, 38, .4);
}
@media print { .sr-box { display: none !important; } }
</style>
'''

SR_SCRIPT = '''<script id="sr-script">
(function () {
  var input = document.getElementById('sr-input');
  if (!input) return;
  var info = document.getElementById('sr-count');
  var clear = document.getElementById('sr-clear');
  var SEL = '.card, .gotcha, .callout';
  var blocks = Array.prototype.slice.call(document.querySelectorAll('.main ' + SEL));
  var total = blocks.length;
  var norm = function (s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
  };
  function clearMarks(root) {
    root.querySelectorAll('mark.sr-hit').forEach(function (m) {
      var p = m.parentNode;
      if (!p) return;
      p.replaceChild(document.createTextNode(m.textContent), m);
      p.normalize();
    });
  }
  function highlight(block, q) {
    var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        if (!p || /^(SCRIPT|STYLE|MARK)$/.test(p.nodeName)) return NodeFilter.FILTER_REJECT;
        return norm(n.nodeValue).indexOf(q) >= 0 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (n) {
      var text = n.nodeValue, low = norm(text);
      var frag = document.createDocumentFragment(), i = 0, idx;
      while ((idx = low.indexOf(q, i)) >= 0) {
        if (idx > i) frag.appendChild(document.createTextNode(text.slice(i, idx)));
        var mk = document.createElement('mark');
        mk.className = 'sr-hit';
        mk.textContent = text.slice(idx, idx + q.length);
        frag.appendChild(mk);
        i = idx + q.length;
      }
      if (i < text.length) frag.appendChild(document.createTextNode(text.slice(i)));
      n.parentNode.replaceChild(frag, n);
    });
  }
  function run() {
    var q = norm(input.value.trim());
    blocks.forEach(function (b) { b.classList.remove('sr-hide'); clearMarks(b); });
    if (q) {
      var found = 0;
      blocks.forEach(function (b) {
        if (norm(b.textContent).indexOf(q) >= 0) { found++; highlight(b, q); }
        else { b.classList.add('sr-hide'); }
      });
      document.querySelectorAll('.main section').forEach(function (s) {
        var vis = s.querySelectorAll(SEL + ':not(.sr-hide)').length;
        s.classList.toggle('sr-empty', vis === 0);
      });
      info.textContent = found + ' de ' + total + ' blocos';
      if (found) {
        var first = null;
        for (var k = 0; k < blocks.length; k++) {
          if (!blocks[k].classList.contains('sr-hide')) {
            first = blocks[k].querySelector('mark.sr-hit');
            if (first) break;
          }
        }
        if (first) {
          first.classList.add('sr-first');
          first.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
    } else {
      document.querySelectorAll('.main section').forEach(function (s) { s.classList.remove('sr-empty'); });
      info.textContent = total + ' blocos';
    }
  }
  input.addEventListener('input', run);
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { input.value = ''; run(); }
  });
  clear.addEventListener('click', function () { input.value = ''; run(); input.focus(); });
  run();
})();
</script>
'''


def inject(html):
    if 'id="sr-script"' in html:
        return None
    # campo no sidebar: após a primeira linha de sidebar-sub
    m = re.search(r'^([ \t]*<div class="sidebar-sub">.*?</div>\n)', html, re.M | re.S)
    if not m:
        return None
    html = html[:m.end(1)] + SR_BOX + html[m.end(1):]
    # estilo + script antes do </body>
    idx = html.rfind('</body>')
    if idx < 0:
        return None
    html = html[:idx] + SR_STYLE + SR_SCRIPT + html[idx:]
    return html


def main():
    targets = sys.argv[1:] or sorted(
        glob.glob(os.path.join(ROOT, '**', 'resumo-aula-*.html'), recursive=True)
    )
    ok = skip = fail = 0
    for f in targets:
        with io.open(f, encoding='utf-8') as fh:
            original = fh.read()
        new = inject(original)
        if new is None:
            if 'id="sr-script"' in original:
                skip += 1
            else:
                fail += 1
                print('FALHA (âncora não encontrada):', f)
            continue
        with io.open(f, 'w', encoding='utf-8', newline='') as fh:
            fh.write(new)
        ok += 1
        print('injetado:', os.path.relpath(f, ROOT))
    print('---')
    print('injetados:', ok, '| já tinham (pulos):', skip, '| falhas:', fail)


if __name__ == '__main__':
    main()
