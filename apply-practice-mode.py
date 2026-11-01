# -*- coding: utf-8 -*-
"""Modo prática (🎯): injeta quiz de recall nos resumos a partir do quiz.json da pasta da aula.
Bônus de reparo: restaura o botão 🧠 (rhRev) ausente e recria a toolbar quando o bloco rh:ui sumiu.

Uso: python apply-practice-mode.py [resumo.html ...]   (sem argumentos: todos os resumos)
Idempotente: o bloco do modo prática é delimitado por <!--rh:practice:start--> ...
<!--rh:practice:end--> e substituído a cada execução (permite atualizar o quiz.json e rodar de novo).

Refatorado para usar apply_shared.HtmlInjectionEngine + PRACTICE_CONFIG.
"""
import glob
import json
import os
import sys

# Adiciona tools ao path para importar apply_shared
TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from apply_shared import (
    HtmlInjectionEngine, PRACTICE_CONFIG,
    TOOLBAR_CSS, ensure_rev_button, ensure_practice_button,
    inject_toolbar_css
)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [os.path.join(ROOT, "*", "Aula *", "resumo-*.html")]

engine = HtmlInjectionEngine(verbose=True)


def process(path: str):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    original = content
    msgs = []

    has_rev_js = 'id="rh-rev"' in content
    has_rev_btn = 'id="rhRev"' in content
    has_toolbar = 'class="rh-toolbar"' in content

    # 1) Reparo: sem toolbar mas com JS do modo revisão -> recria toolbar mínima com o botão 🧠
    if has_rev_js and not has_toolbar and not has_rev_btn:
        anchor = content.find('<script id="rh-rev">')
        if anchor != -1:
            from apply_shared import REV_BTN
            toolbar = ('\n<div class="rh-toolbar" role="group" aria-label="Ferramentas de leitura">'
                       + REV_BTN + "\n</div>\n\n")
            content = content[:anchor] + toolbar + content[anchor:]
            content = inject_toolbar_css(content)
            has_toolbar = has_rev_btn = True
            msgs.append("toolbar+🧠 recriados")

    # 2) Reparo: toolbar existe, botão 🧠 ausente -> restaura após o rhTop
    if has_rev_js and not has_rev_btn and has_toolbar:
        content = ensure_rev_button(content)
        has_rev_btn = True
        msgs.append("🧠 restaurado")

    # 3) Modo prática (se quiz.json existe)
    quiz_path = os.path.join(os.path.dirname(path), "quiz.json")
    if os.path.exists(quiz_path):
        with open(quiz_path, encoding="utf-8") as fh:
            quiz = json.load(fh)
        n = len(quiz.get("questoes", []))

        # Prepara o bloco de prática com dados dinâmicos
        data = json.dumps(quiz, ensure_ascii=False).replace("</", "<\\/")
        data_script = ('<script type="application/json" id="rhPracticeData">' + data + "</script>")

        # O PRACTICE_CONFIG já tem CSS, JS, HTML base
        # Usamos post_process para injetar o data_script no lugar certo
        # O HTML do PRACTICE_CONFIG tem: PAINEL_HTML + data_script placeholder + JS
        # Precisamos substituir o placeholder vazio pelo data_script real
        def practice_with_data(html):
            # Substitui o script vazio pelo data_script real
            placeholder = '<script type="application/json" id="rhPracticeData"></script>'
            if placeholder in html:
                html = html.replace(placeholder, data_script)
            return html

        # Config temporária com post_process customizado
        from apply_shared import ApplyConfig
        practice_config = ApplyConfig(
            idempotency_key='<!--rh:practice:start-->',
            css_anchor=r"</style>",
            js_anchor=r"</body>",
            css=PRACTICE_CONFIG.css,
            js=PRACTICE_CONFIG.js,
            html=PRACTICE_CONFIG.html,
            upgrade_v1_regex=PRACTICE_CONFIG.upgrade_v1_regex,
            post_process=practice_with_data,
        )

        new_content = engine.apply(content, practice_config)
        if new_content is not None:
            content = new_content
            content = ensure_practice_button(content)
            msgs.append("modo prática 🎯 (%d questões)" % n)
        else:
            msgs.append("!! modo prática não aplicado (idempotente)")

    # Garante toolbar CSS e botão 🧠 se não existirem
    if "rh-toolbar" not in content and "rh-toolbar" not in original:
        idx = content.rfind("</style>")
        if idx != -1:
            content = content[:idx] + TOOLBAR_CSS + content[idx:]
    content = ensure_rev_button(content)
    content = ensure_practice_button(content)

    if content != original:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(content)
        return msgs
    return []


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