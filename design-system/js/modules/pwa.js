/**
 * pwa.js — Service Worker registration
 * Registra o SW para PWA offline.
 */

(function () {
  'use strict';

  if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
    navigator.serviceWorker.register('/sw.js').catch(function () {});
  }
})();