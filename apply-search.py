# -*- coding: utf-8 -*-
"""
apply-search.py — injeta o campo de busca por palavra (filtro + destaque + navegação) nos resumos.

v2 (14/10/2026):
  - navegação entre ocorrências: botões ↑/↓ + Enter (próxima) / Shift+Enter (anterior)
    + contador de posição "n/m" (a ocorrência atual fica com o destaque vermelho);
  - busca multi-palavra: cada palavra digitada é procurada separadamente no bloco
    (todas devem estar presentes — E lógico) e cada uma ganha seu destaque âmbar;
  - upgrade idempotente: arquivos com a v1 (id="sr-script" sem data-sr-v) são
    reprocessados — o bloco antigo é removido e o novo injetado no mesmo lugar.

Idempotente: pula arquivos que já tenham data-sr-v="2". Reexecutar após regenerar
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

SR_V = '2'
SR_CUR = 'data-sr-v="%s"' % SR_V

# Box da v1 (removida no upgrade — string exata, sem surpresas de regex)
SR_BOX_V1 = (
    '  <div class="sr-box">\n'
    '    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">\n'
    '    <div class="sr-info"><span id="sr-count"></span><button id="sr-clear" type="button">limpar</button></div>\n'
    '  </div>\n'
)

SR_BOX = (
    '  <div class="sr-box" ' + SR_CUR + '>\n'
    '    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">\n'
    '    <div class="sr-info"><span id="sr-count"></span>'
    '<span class="sr-nav"><button id="sr-prev" type="button" title="Ocorrência anterior (Shift+Enter)" disabled>↑</button>'
    '<span id="sr-pos"></span>'
    '<button id="sr-next" type="button" title="Próxima ocorrência (Enter)" disabled>↓</button></span>'
    '<button id="sr-clear" type="button">limpar</button></div>\n'
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
  display: flex; justify-content: space-between; align-items: center; gap: .3rem;
  margin-top: .3rem; font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
  font-size: .62rem; color: var(--text2, #455064);
}
.sr-nav { display: inline-flex; align-items: center; gap: .25rem; }
.sr-nav button {
  background: none; border: 1px solid var(--border, #e2dfd7); border-radius: 5px;
  cursor: pointer; color: var(--text2, #455064); font-family: inherit;
  font-size: .62rem; padding: 0 .32rem; line-height: 1.5;
}
.sr-nav button:hover:not(:disabled) { border-color: var(--mat, var(--blue)); color: var(--mat-strong, var(--blue)); }
.sr-nav button:disabled { opacity: .35; cursor: default; }
#sr-pos { min-width: 3.2ch; text-align: center; color: var(--mat-strong, var(--blue, #2563eb)); font-weight: 600; }
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

SR_SCRIPT = '''<script id="sr-script" data-sr-v="2">
(function () {
  var input = document.getElementById('sr-input');
  if (!input) return;
  var info = document.getElementById('sr-count');
  var posEl = document.getElementById('sr-pos');
  var bPrev = document.getElementById('sr-prev');
  var bNext = document.getElementById('sr-next');
  var clear = document.getElementById('sr-clear');
  var SEL = '.card, .gotcha, .callout';
  var blocks = Array.prototype.slice.call(document.querySelectorAll('.main ' + SEL));
  var total = blocks.length;
  var hits = [], cur = -1;
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
  function highlight(block, words) {
    var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        if (!p || /^(SCRIPT|STYLE|MARK)$/.test(p.nodeName)) return NodeFilter.FILTER_REJECT;
        var low = norm(n.nodeValue);
        for (var w = 0; w < words.length; w++) {
          if (low.indexOf(words[w]) >= 0) return NodeFilter.FILTER_ACCEPT;
        }
        return NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (n) {
      var text = n.nodeValue, low = norm(text);
      var frag = document.createDocumentFragment(), i = 0;
      for (;;) {
        var best = -1, bestLen = 0;
        for (var w = 0; w < words.length; w++) {
          var idx = low.indexOf(words[w], i);
          if (idx >= 0 && (best < 0 || idx < best)) { best = idx; bestLen = words[w].length; }
        }
        if (best < 0) break;
        if (best > i) frag.appendChild(document.createTextNode(text.slice(i, best)));
        var mk = document.createElement('mark');
        mk.className = 'sr-hit';
        mk.textContent = text.slice(best, best + bestLen);
        frag.appendChild(mk);
        i = best + bestLen;
      }
      if (i < text.length) frag.appendChild(document.createTextNode(text.slice(i)));
      n.parentNode.replaceChild(frag, n);
    });
  }
  function setActive(n, scroll) {
    if (cur >= 0 && hits[cur]) hits[cur].classList.remove('sr-first');
    cur = n;
    if (!hits.length) { posEl.textContent = ''; sync(); return; }
    cur = ((n % hits.length) + hits.length) % hits.length;
    hits[cur].classList.add('sr-first');
    posEl.textContent = (cur + 1) + '/' + hits.length;
    if (scroll) hits[cur].scrollIntoView({ behavior: 'smooth', block: 'center' });
    sync();
  }
  function sync() {
    bPrev.disabled = bNext.disabled = hits.length === 0;
  }
  function run(scrollToFirst) {
    var q = norm(input.value.trim());
    var words = q ? q.split(/\\s+/).filter(Boolean) : [];
    blocks.forEach(function (b) { b.classList.remove('sr-hide'); clearMarks(b); });
    hits = []; cur = -1;
    if (words.length) {
      var found = 0;
      blocks.forEach(function (b) {
        var low = norm(b.textContent);
        var all = words.every(function (w) { return low.indexOf(w) >= 0; });
        if (all) { found++; highlight(b, words); }
        else { b.classList.add('sr-hide'); }
      });
      document.querySelectorAll('.main section').forEach(function (s) {
        var vis = s.querySelectorAll(SEL + ':not(.sr-hide)').length;
        s.classList.toggle('sr-empty', vis === 0);
      });
      info.textContent = found + ' de ' + total + ' blocos';
      hits = Array.prototype.slice.call(document.querySelectorAll('.main mark.sr-hit'));
      if (hits.length && scrollToFirst !== false) setActive(0, true); else sync();
      if (!hits.length) { posEl.textContent = ''; sync(); }
    } else {
      document.querySelectorAll('.main section').forEach(function (s) { s.classList.remove('sr-empty'); });
      info.textContent = total + ' blocos';
      posEl.textContent = ''; sync();
    }
  }
  input.addEventListener('input', function () { run(true); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { input.value = ''; run(true); }
    else if (e.key === 'Enter') { e.preventDefault(); setActive(hits.length ? cur + (e.shiftKey ? -1 : 1) : -1, true); }
  });
  bNext.addEventListener('click', function () { if (hits.length) setActive(cur + 1, true); });
  bPrev.addEventListener('click', function () { if (hits.length) setActive(cur - 1, true); });
  clear.addEventListener('click', function () { input.value = ''; run(true); input.focus(); });
  run(false);
})();
</script>
'''


def inject(html):
    if SR_CUR in html:
        return None
    changed = False
    if 'id="sr-script"' in html or 'class="sr-box"' in html or 'id="sr-style"' in html:
        # upgrade: remover blocos antigos (v1) antes de reinjetar
        if SR_BOX_V1 in html:
            html = html.replace(SR_BOX_V1, '')
        if 'class="sr-box"' in html:
            html = re.sub(r'[ \t]*<div class="sr-box"[^>]*>[\s\S]*?^[ \t]*</div>\n', '', html, count=1, flags=re.M)
        html = re.sub(r'<style id="sr-style">[\s\S]*?</style>\n?', '', html, count=1)
        html = re.sub(r'<script id="sr-script"[^>]*>[\s\S]*?</script>\n?', '', html, count=1)
        changed = True
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
    return html if (changed or SR_CUR in html) else None


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
            if SR_CUR in original:
                skip += 1
            else:
                fail += 1
                print('FALHA (âncora não encontrada):', f)
            continue
        with io.open(f, 'w', encoding='utf-8', newline='') as fh:
            fh.write(new)
        ok += 1
        print('atualizado:', os.path.relpath(f, ROOT))
    print('---')
    print('atualizados:', ok, '| já na v2 (pulos):', skip, '| falhas:', fail)


if __name__ == '__main__':
    main()
