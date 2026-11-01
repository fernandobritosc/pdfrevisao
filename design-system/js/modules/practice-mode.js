/**
 * practice-mode.js — Modo prática (quiz de recall)
 * Carrega quiz.json da pasta da aula e injeta UI.
 */

(function () {
  'use strict';

  var dataEl = document.getElementById('rhPracticeData');
  var btn = document.getElementById('rhPractice');
  var panel = document.getElementById('rhPracticePanel');

  if (!dataEl || !btn || !panel) return;

  var DATA;
  try { DATA = JSON.parse(dataEl.textContent); } catch (e) { return; }

  var qs = DATA.questoes || [];
  var list = document.getElementById('rhPracticeList');
  var scoreEl = document.getElementById('rhPracticeScore');
  var hits = 0, done = 0, total = qs.length;

  function score() {
    scoreEl.textContent = hits + ' acertos · ' + done + '/' + total;
  }

  function render() {
    hits = 0; done = 0; list.innerHTML = '';
    qs.forEach(function (item, qi) {
      var box = document.createElement('div'); box.className = 'rhpp-item';
      var q = document.createElement('div'); q.className = 'rhpp-q';
      q.textContent = 'Q' + (qi + 1) + ' · ' + item.q; box.appendChild(q);

      item.opts.forEach(function (o) {
        var b = document.createElement('button'); b.type = 'button';
        b.className = 'rhpp-opt'; b.textContent = o.t;
        b.addEventListener('click', function () {
          if (box.getAttribute('data-done') === '1') return;
          box.setAttribute('data-done', '1');

          var opts = box.querySelectorAll('.rhpp-opt');
          Array.prototype.forEach.call(opts, function (s, si) {
            s.disabled = true;
            if (item.opts[si] && item.opts[si].ok) s.classList.add('ok');
          });

          if (!o.ok) b.classList.add('bad');

          var why = document.createElement('div'); why.className = 'rhpp-why';
          why.textContent = o.why || ''; box.appendChild(why);

          done++; if (o.ok) hits++; score();
        });
        box.appendChild(b);
      });
      list.appendChild(box);
    });
    score();
  }

  btn.addEventListener('click', function () {
    var show = !panel.classList.contains('show');
    panel.classList.toggle('show', show);
    btn.classList.toggle('on', show);
    btn.setAttribute('aria-pressed', show ? 'true' : 'false');
    if (show && !list.children.length) render();
  });

  document.getElementById('rhPracticeClose').addEventListener('click', function () {
    panel.classList.remove('show');
    btn.classList.remove('on');
    btn.setAttribute('aria-pressed', 'false');
  });

  document.getElementById('rhPracticeReset').addEventListener('click', render);
})();