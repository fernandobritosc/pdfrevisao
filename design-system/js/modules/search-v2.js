/**
 * search-v2.js — Busca por palavra (filtro + destaque + navegação)
 * v2: navegação entre ocorrências + busca multi-palavra (E lógico)
 */

(function () {
  'use strict';

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
    return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
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
    var words = q ? q.split(/\s+/).filter(Boolean) : [];
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

  if (bNext) bNext.addEventListener('click', function () { if (hits.length) setActive(cur + 1, true); });
  if (bPrev) bPrev.addEventListener('click', function () { if (hits.length) setActive(cur - 1, true); });
  if (clear) clear.addEventListener('click', function () { input.value = ''; run(true); input.focus(); });

  run(false);
})();