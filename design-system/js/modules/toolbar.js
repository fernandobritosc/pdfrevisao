/**
 * toolbar.js — Toolbar flutuante (tema, fonte, topo, revisão, marcação, prática)
 * Dependências: theme-init.js (window.__RH_THEME__)
 */

(function () {
  'use strict';

  var root = document.documentElement;
  var theme = window.__RH_THEME__;

  // Elementos
  var bTheme = document.getElementById('rhTheme');
  var bFontMinus = document.getElementById('rhFontMinus');
  var bFontPlus = document.getElementById('rhFontPlus');
  var bTop = document.getElementById('rhTop');
  var bRev = document.getElementById('rhRev');
  var bMarks = document.getElementById('rhMarks');
  var bPractice = document.getElementById('rhPractice');

  if (!bTheme || !bFontMinus || !bFontPlus || !bTop) {
    return; // toolbar não existe nesta página
  }

  // --- Tema ---
  function updateThemeIcon() {
    if (bTheme) {
      bTheme.textContent = root.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';
    }
  }

  if (bTheme) {
    bTheme.addEventListener('click', function () {
      var current = root.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      if (theme && theme.setTheme) {
        theme.setTheme(next);
      } else {
        root.setAttribute('data-theme', next);
        try { localStorage.setItem('rh-theme', next); } catch (e) {}
      }
      updateThemeIcon();
    });
  }

  updateThemeIcon();

  // --- Fonte ---
  function updateFontButtons() {
    if (!theme || !theme.steps) return;
    var cur = theme.getFontSize ? theme.getFontSize() : 100;
    var idx = theme.steps.indexOf(cur);
    if (bFontMinus) bFontMinus.disabled = idx === 0;
    if (bFontPlus) bFontPlus.disabled = idx === theme.steps.length - 1;
  }

  if (bFontMinus) {
    bFontMinus.addEventListener('click', function () {
      if (theme && theme.setFontSize) {
        var cur = theme.getFontSize();
        var idx = theme.steps.indexOf(cur);
        if (idx > 0) theme.setFontSize(theme.steps[idx - 1]);
      }
      updateFontButtons();
    });
  }

  if (bFontPlus) {
    bFontPlus.addEventListener('click', function () {
      if (theme && theme.setFontSize) {
        var cur = theme.getFontSize();
        var idx = theme.steps.indexOf(cur);
        if (idx < theme.steps.length - 1) theme.setFontSize(theme.steps[idx + 1]);
      }
      updateFontButtons();
    });
  }

  updateFontButtons();

  // --- Botão Topo ---
  function onScroll() {
    if (bTop) {
      bTop.hidden = (window.scrollY || document.documentElement.scrollTop) < 500;
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (bTop) {
    bTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // --- Modo Revisão (delegado para review-mode.js se existir) ---
  // Apenas garante que o botão existe; review-mode.js faz o resto

  // --- Modo Marcação (delegado para marks-mode.js se existir) ---

  // --- Modo Prática (delegado para practice-mode.js se existir) ---

  // Expõe API para outros módulos
  window.__RH_TOOLBAR__ = {
    getButtons: function () {
      return {
        theme: bTheme,
        fontMinus: bFontMinus,
        fontPlus: bFontPlus,
        top: bTop,
        rev: bRev,
        marks: bMarks,
        practice: bPractice
      };
    }
  };
})();