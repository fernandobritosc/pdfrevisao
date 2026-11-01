/**
 * theme-init.js — Inicialização do tema (light/dark) e tamanho da fonte
 * Executado antes de tudo (inline no <head> ou via modulepreload)
 */

(function () {
  'use strict';

  var root = document.documentElement;

  // --- Tema ---
  var theme = null;
  try {
    theme = localStorage.getItem('rh-theme');
  } catch (e) {}

  if (theme !== 'dark' && theme !== 'light') {
    theme = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
  }

  root.setAttribute('data-theme', theme);

  // --- Tamanho da fonte ---
  var fontSize = 100;
  try {
    fontSize = parseInt(localStorage.getItem('rh-fs') || '100', 10);
  } catch (e) {}

  var steps = [85, 90, 95, 100, 107, 114, 120];
  if (steps.indexOf(fontSize) < 0) {
    fontSize = 100;
  }

  root.style.fontSize = fontSize + '%';

  // Exporta para outros módulos
  window.__RH_THEME__ = {
    getTheme: function () { return root.getAttribute('data-theme'); },
    setTheme: function (t) {
      root.setAttribute('data-theme', t);
      try { localStorage.setItem('rh-theme', t); } catch (e) {}
    },
    getFontSize: function () { return fontSize; },
    setFontSize: function (fs) {
      if (steps.indexOf(fs) >= 0) {
        fontSize = fs;
        root.style.fontSize = fs + '%';
        try { localStorage.setItem('rh-fs', String(fs)); } catch (e) {}
      }
    },
    steps: steps
  };
})();