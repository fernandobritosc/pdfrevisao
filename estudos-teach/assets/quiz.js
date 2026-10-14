/* quiz.js — widget de recall com feedback imediato (reutilizável por todas as lições)
   Estrutura esperada:
   <div data-quiz>
     <div class="q-body">…pergunta…</div>
     <button class="opt" data-ok="1" data-why="…">…</button>
     <button class="opt" data-why="…">…</button> …
     <div class="feedback"></div>
   </div>
   <div id="quiz-score" data-total="6"></div>   ← opcional, um por página
*/
(function () {
  'use strict';
  var quizzes = document.querySelectorAll('[data-quiz]');
  var scoreEl = document.getElementById('quiz-score');
  var hits = 0, done = 0, total = quizzes.length;

  function renderScore() {
    if (!scoreEl) return;
    scoreEl.textContent = 'Placar: ' + hits + ' de ' + done +
      (done === total ? (hits === total ? ' — impecável. 🎯' : ' — revise o feedback acima e refaça a lição.') :
        ' de ' + total + ' questões');
  }

  Array.prototype.forEach.call(quizzes, function (q) {
    var opts = q.querySelectorAll('button.opt');
    var fb = q.querySelector('.feedback');
    var answered = false;

    Array.prototype.forEach.call(opts, function (b) {
      b.addEventListener('click', function () {
        if (answered) return;
        answered = true;
        done += 1;
        var ok = b.getAttribute('data-ok') === '1';
        if (ok) hits += 1;
        Array.prototype.forEach.call(opts, function (o) {
          o.disabled = true;
          if (o.getAttribute('data-ok') === '1') o.classList.add('ok');
        });
        if (!ok) b.classList.add('bad');
        fb.textContent = b.getAttribute('data-why') || '';
        fb.classList.add('show');
        renderScore();
      });
    });
  });

  renderScore();
})();
