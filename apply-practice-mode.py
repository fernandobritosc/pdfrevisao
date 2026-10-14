# -*- coding: utf-8 -*-
"""Modo prática (🎯): injeta quiz de recall nos resumos a partir do quiz.json da pasta da aula.
Bônus de reparo: restaura o botão 🧠 (rhRev) ausente e recria a toolbar quando o bloco rh:ui sumiu.

Uso: python apply-practice-mode.py [resumo.html ...]   (sem argumentos: todos os resumos)
Idempotente: o bloco do modo prática é delimitado por <!--rh:practice:start--> ...
<!--rh:practice:end--> e substituído a cada execução (permite atualizar o quiz.json e rodar de novo).
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [os.path.join(ROOT, "*", "Aula *", "resumo-*.html")]

START, END = "<!--rh:practice:start-->", "<!--rh:practice:end-->"
BTN_S, BTN_E = "<!--rh:practice-btn:start-->", "<!--rh:practice-btn:end-->"

REV_BTN = ('\n  <button type="button" id="rhRev" title="Modo revisão: oculte e se auto-teste" '
           'aria-label="Alternar modo revisão" aria-pressed="false">\U0001F9E0</button>')
PRAC_BTN = ('<button type="button" id="rhPractice" title="Modo prática: quiz de recall da aula" '
            'aria-label="Abrir modo prática" aria-pressed="false">\U0001F3AF</button>')

TOOLBAR_CSS = """
/* ===== RH toolbar base (reparo) ===== */
.rh-toolbar { position: fixed; right: 1.1rem; bottom: 1.1rem; display: flex; flex-direction: column; gap: .45rem; z-index: 300; }
.rh-toolbar button {
  width: 42px; height: 42px; border-radius: 50%; border: 1px solid var(--line-strong);
  background: var(--card); color: var(--text); cursor: pointer; padding: 0; line-height: 1;
  font-family: 'JetBrains Mono', 'Consolas', monospace; font-weight: 600; font-size: .9rem;
  box-shadow: 0 4px 14px rgba(31,39,51,.18); display: flex; align-items: center; justify-content: center;
  transition: transform .15s, border-color .15s;
}
.rh-toolbar button:hover { transform: translateY(-2px); border-color: var(--blue); }
.rh-toolbar button[hidden] { display: none; }
@media (max-width: 768px) { .rh-toolbar { right: .7rem; bottom: .7rem; } }
@media print { .rh-toolbar { display: none !important; } }
"""

PRACTICE_CSS = """
/* ===== RH modo prática (quiz) ===== */
#rhPracticePanel { position: fixed; right: 1.1rem; bottom: 5.8rem; z-index: 301; display: none;
  width: min(390px, calc(100vw - 2.2rem)); max-height: min(72vh, 580px); overflow: auto;
  background: var(--card, #fff); border: 1px solid var(--border, #e2dfd7); border-radius: 12px;
  box-shadow: 0 8px 28px rgba(31,39,51,.2); padding: .85rem .95rem .95rem; }
#rhPracticePanel.show { display: block; }
#rhPracticePanel .rhpp-head { display: flex; align-items: center; gap: .5rem; margin-bottom: .3rem; }
#rhPracticePanel .rhpp-head strong { font-size: .88rem; color: var(--text, #1f2733); }
#rhPracticePanel .rhpp-score { font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: .7rem;
  color: var(--text2, #455064); margin-left: auto; white-space: nowrap; }
#rhPracticePanel .rhpp-close { background: none; border: none; font-size: 1.15rem; line-height: 1;
  cursor: pointer; color: var(--text2, #455064); padding: 0 .1rem; }
#rhPracticePanel .rhpp-item { margin: .55rem 0; }
#rhPracticePanel .rhpp-q { font-size: .83rem; font-weight: 700; color: var(--text, #1f2733);
  margin-bottom: .3rem; line-height: 1.45; }
#rhPracticePanel .rhpp-opt { display: block; width: 100%; text-align: left; font-size: .79rem; line-height: 1.45;
  font-family: inherit; background: var(--bg, #fff); color: var(--text, #1f2733);
  border: 1px solid var(--border, #e2dfd7); border-radius: 8px; padding: .4rem .6rem;
  margin: .25rem 0; cursor: pointer; }
#rhPracticePanel .rhpp-opt:hover:not(:disabled) { border-color: var(--mat, var(--blue, #2563eb)); }
#rhPracticePanel .rhpp-opt:disabled { cursor: default; opacity: .72; }
#rhPracticePanel .rhpp-opt.ok { border-color: #15803d; background: rgba(21,128,61,.1); opacity: 1; }
#rhPracticePanel .rhpp-opt.bad { border-color: var(--red, #b3261e); background: rgba(179,38,30,.08); opacity: 1; }
#rhPracticePanel .rhpp-why { font-size: .75rem; color: var(--text2, #455064); line-height: 1.5;
  background: var(--surface, #f6f4ee); border-left: 3px solid var(--mat, var(--blue, #2563eb));
  border-radius: 0 8px 8px 0; padding: .42rem .6rem; margin-top: .28rem; }
#rhPracticePanel .rhpp-reset { font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: .72rem;
  font-weight: 600; background: var(--card, #fff); color: var(--mat, var(--blue, #2563eb));
  border: 1px solid var(--border, #e2dfd7); border-radius: 8px; padding: .35rem .7rem;
  cursor: pointer; margin-top: .55rem; }
html[data-theme="dark"] #rhPracticePanel { background: var(--surface, #1f232b); }
html[data-theme="dark"] #rhPracticePanel .rhpp-opt { background: var(--card, #262b34); }
html[data-theme="dark"] #rhPracticePanel .rhpp-why { background: rgba(255,255,255,.05); }
@media print { #rhPracticePanel { display: none !important; } }
"""

PRACTICE_JS = """<script id="rh-practice">
(function(){
  var dataEl = document.getElementById('rhPracticeData');
  var btn = document.getElementById('rhPractice');
  var panel = document.getElementById('rhPracticePanel');
  if (!dataEl || !btn || !panel) return;
  var DATA; try { DATA = JSON.parse(dataEl.textContent); } catch (e) { return; }
  var qs = DATA.questoes || [];
  var list = document.getElementById('rhPracticeList');
  var scoreEl = document.getElementById('rhPracticeScore');
  var hits = 0, done = 0, total = qs.length;
  function score() { scoreEl.textContent = hits + ' acertos · ' + done + '/' + total; }
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
    panel.classList.remove('show'); btn.classList.remove('on');
    btn.setAttribute('aria-pressed', 'false');
  });
  document.getElementById('rhPracticeReset').addEventListener('click', render);
})();
</script>"""

PANEL_HTML = ("""<div id="rhPracticePanel" role="dialog" aria-label="Modo prática — quiz da aula">"""
              """\n  <div class="rhpp-head"><strong>\U0001F3AF Modo prática</strong>"""
              """<span class="rhpp-score" id="rhPracticeScore"></span>"""
              """<button type="button" class="rhpp-close" id="rhPracticeClose" aria-label="Fechar">×</button></div>"""
              """\n  <div id="rhPracticeList"></div>"""
              """\n  <button type="button" class="rhpp-reset" id="rhPracticeReset">Refazer</button>"""
              """\n</div>""")


def strip_markers(content):
    content = re.sub(re.escape(BTN_S) + r".*?" + re.escape(BTN_E), "", content, flags=re.S)
    content = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", content, flags=re.S)
    return content


def inject_css(content, css):
    idx = content.rfind("</style>")
    if idx == -1:
        return content
    return content[:idx] + css + content[idx:]


def process(path):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    original = content
    msgs = []

    has_rev_js = 'id="rh-rev"' in content
    has_rev_btn = 'id="rhRev"' in content
    has_toolbar = 'class="rh-toolbar"' in content

    # 1) reparo: sem toolbar mas com JS do modo revisão -> recria toolbar mínima com o botão 🧠
    if has_rev_js and not has_toolbar and not has_rev_btn:
        anchor = content.find('<script id="rh-rev">')
        if anchor != -1:
            toolbar = ('\n<div class="rh-toolbar" role="group" aria-label="Ferramentas de leitura">'
                       + REV_BTN + "\n</div>\n\n")
            content = content[:anchor] + toolbar + content[anchor:]
            content = inject_css(content, TOOLBAR_CSS)
            has_toolbar = has_rev_btn = True
            msgs.append("toolbar+🧠 recriados")

    # 2) reparo: toolbar existe, botão 🧠 ausente -> restaura após o rhTop
    if has_rev_js and not has_rev_btn and has_toolbar:
        m = re.search(r'(id="rhTop"[^>]*>.*?</button>)', content)
        if m:
            content = content[:m.end(1)] + REV_BTN + content[m.end(1):]
            has_rev_btn = True
            msgs.append("🧠 restaurado")

    # 3) modo prática
    quiz_path = os.path.join(os.path.dirname(path), "quiz.json")
    if os.path.exists(quiz_path):
        with open(quiz_path, encoding="utf-8") as fh:
            quiz = json.load(fh)
        n = len(quiz.get("questoes", []))
        content = strip_markers(content)
        data = json.dumps(quiz, ensure_ascii=False).replace("</", "<\\/")
        data_script = ('<script type="application/json" id="rhPracticeData">' + data + "</script>")
        block = (START + "\n<style id=\"rh-practice-style\">" + PRACTICE_CSS + "</style>\n"
                 + PANEL_HTML + "\n" + data_script + "\n" + PRACTICE_JS + "\n" + END)
        idx = content.rfind("</body>")
        if idx == -1:
            msgs.append("!! sem </body>")
        else:
            content = content[:idx] + block + "\n" + content[idx:]
        anchor = (re.search(r'(id="rhRev"[^>]*>.*?</button>)', content)
                  or re.search(r'(id="rhTop"[^>]*>.*?</button>)', content))
        if anchor:
            btn = "\n  " + BTN_S + PRAC_BTN + BTN_E
            content = content[:anchor.end(1)] + btn + content[anchor.end(1):]
            msgs.append("modo prática 🎯 (%d questões)" % n)
        else:
            msgs.append("!! sem âncora de botão para o 🎯")

    if content != original:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(content)
    return msgs


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    targets = sys.argv[1:] or [p for g in GLOBS for p in sorted(glob.glob(g))]
    fixed = prac = 0
    for path in targets:
        msgs = process(path)
        if not msgs:
            continue
        rel = os.path.relpath(path, ROOT)
        print(os.path.basename(os.path.dirname(path)) + "/" + os.path.basename(path) + ": " + " · ".join(msgs))
        if any("🧠" in m or "toolbar" in m for m in msgs):
            fixed += 1
        if any("prática" in m for m in msgs):
            prac += 1
    print("resumos com reparo de revisão/toolbar: %d | com modo prática: %d" % (fixed, prac))


if __name__ == "__main__":
    sys.exit(main())
