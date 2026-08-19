/* Resumos Hermes — service worker (offline)
   Estratégia: network-first para navegação (conteúdo sempre fresco),
   cache-first para search-index.json e runtime cache para demais. */
var V = 'rh-v1';
var CORE = ['/', '/manifest.webmanifest', '/search-index.json',
            '/icons/icon-192.png', '/icons/icon-512.png', '/icons/icon-180.png'];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(V).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.filter(function (k) { return k !== V; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);

  if (url.origin !== location.origin) {
    e.respondWith(caches.match(req).then(function (r) {
      return r || fetch(req).then(function (res) {
        var cp = res.clone();
        caches.open(V).then(function (c) { c.put(req, cp); });
        return res;
      });
    }));
    return;
  }

  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).then(function (res) {
      var cp = res.clone();
      caches.open(V).then(function (c) { c.put(req, cp); });
      return res;
    }).catch(function () {
      return caches.match(req).then(function (r) { return r || caches.match('/'); });
    }));
    return;
  }

  if (url.pathname.endsWith('/search-index.json')) {
    e.respondWith(caches.match(req).then(function (r) { return r || fetch(req); }));
    return;
  }

  e.respondWith(caches.match(req).then(function (r) {
    return r || fetch(req).then(function (res) {
      var cp = res.clone();
      caches.open(V).then(function (c) { c.put(req, cp); });
      return res;
    });
  }));
});