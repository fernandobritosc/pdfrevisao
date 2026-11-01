/**
 * review-mode.js — Modo revisão (active recall)
 * Botão 🧠 no toolbar, CSS oculta conteúdo e JS revela por clique.
 */

(function () {
  'use strict';

  var b = document.getElementById('rhRev');
  if (!b) return;

  var root = document.documentElement;

  function isActive() {
    return root.classList.contains('rh-rev');
  }

  function apply() {
    var now = !isActive();
    root.classList.toggle('rh-rev', now);
    b.classList.toggle('on', now);
    try { localStorage.setItem('rh-rev', now ? '1' : '0'); } catch (e) {}
    b.setAttribute('aria-pressed', now ? 'true' : 'false');
  }

  b.addEventListener('click', apply);

  // Restaura estado salvo
  try {
    if (localStorage.getItem('rh-rev') === '1') apply();
  } catch (e) {}

  // Click em cards/blocos para abrir/fechar
  document.addEventListener('click', function (ev) {
    if (!isActive()) return;
    var el = ev.target && ev.target.closest
      ? ev.target.closest('.card, .gotcha, .callout, .table-wrap, .mnemonic, .question')
      : null;
    if (!el || ev.target.closest('a')) return;
    el.classList.toggle('rev-open');
  });
})();