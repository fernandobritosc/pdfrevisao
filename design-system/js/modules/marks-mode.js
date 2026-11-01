/**
 * marks-mode.js — Marcação pessoal (vacilo)
 * Botão 🏷 no toolbar, marca cards/blocos em vermelho com persistência em localStorage,
 * export/import de backup JSON.
 */

(function () {
  'use strict';

  var b = document.getElementById('rhMarks');
  if (!b) return;

  var root = document.documentElement;
  var LS = 'rh-marks';
  var KEY = location.pathname || 'local';

  var store = {};
  try { store = JSON.parse(localStorage.getItem(LS) || '{}') || {}; } catch (e) {}

  // Painel
  var panel = document.createElement('div');
  panel.id = 'rhMarkPanel';
  panel.innerHTML = '<div class="rhmp-count">Vacilos marcados: <span id="rhmpN">0</span></div>' +
    '<button type="button" id="rhmpExp">⬇ exportar</button>' +
    '<button type="button" id="rhmpImp">⬆ importar</button><input id="rhmpFile" type="file" accept="application/json" hidden>';
  document.body.appendChild(panel);

  var nEl = document.getElementById('rhmpN');
  var fileIn = document.getElementById('rhmpFile');

  function blkKey(el) {
    var sec = el.closest('section');
    var sid = sec ? (sec.id || '') : '';
    var t = el.querySelector('.card-title, .gotcha-title, .mnemonic-label');
    var txt = '';
    if (t) { txt = t.textContent.trim(); }
    else {
      var th = el.querySelector('th');
      txt = th ? th.textContent.trim() : '';
    }
    if (!txt) {
      var f = el.firstElementChild;
      txt = (f ? f.textContent : '') || '';
    }
    return (sid ? sid + '|' : '') + (txt.slice(0, 60) || 'bloco');
  }

  var SEL = '.card, .gotcha, .callout, .table-wrap, .mnemonic, .question';

  function collect() {
    var out = [];
    document.querySelectorAll('.rh-marked').forEach(function (el) { out.push(blkKey(el)); });
    return out;
  }

  function save() {
    store[KEY] = collect();
    try { localStorage.setItem(LS, JSON.stringify(store)); } catch (e) {}
    render();
  }

  function render() {
    nEl.textContent = String(collect().length);
  }

  function applyMarks(list) {
    document.querySelectorAll('.rh-marked').forEach(function (el) { el.classList.remove('rh-marked'); });
    document.querySelectorAll(SEL).forEach(function (el) {
      if (list.indexOf(blkKey(el)) >= 0) el.classList.add('rh-marked');
    });
    save();
  }

  function isActive() {
    return root.classList.contains('rh-marking');
  }

  b.addEventListener('click', function () {
    var now = !isActive();
    root.classList.toggle('rh-marking', now);
    b.classList.toggle('on', now);
    b.setAttribute('aria-pressed', now ? 'true' : 'false');
    panel.classList.toggle('show', now);
  });

  document.addEventListener('click', function (ev) {
    if (!isActive()) return;
    var el = ev.target && ev.target.closest ? ev.target.closest(SEL) : null;
    if (!el || ev.target.closest('a') || ev.target.closest('#rhMarkPanel')) return;
    el.classList.toggle('rh-marked');
    save();
  });

  document.getElementById('rhmpExp').addEventListener('click', function () {
    var blob = new Blob([JSON.stringify({ version: 1, path: KEY, marks: collect() }, null, 2)], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'marcacoes' + KEY.replace(/[^\w]+/g, '-') + '.json';
    a.click();
  });

  document.getElementById('rhmpImp').addEventListener('click', function () { fileIn.click(); });

  fileIn.addEventListener('change', function () {
    var f = fileIn.files && fileIn.files[0];
    if (!f) return;
    var r = new FileReader();
    r.onload = function () {
      try {
        var d = JSON.parse(r.result);
        if (d && d.marks) applyMarks(d.marks);
      } catch (e) {}
    };
    r.readAsText(f);
  });

  // Restaura marcas salvas
  try {
    var saved = (store[KEY] || []);
    if (saved.length) applyMarks(saved);
  } catch (e) {}

  render();
})();