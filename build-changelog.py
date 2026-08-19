# -*- coding: utf-8 -*-
"""Gera Resumo_estudos/mudancas.html — log de alterações derivado do git log
(mensagens descritivas dos commits + resumos afetados).

Uso: python build-changelog.py
Rodar sempre antes de publicar no Surge (fluxo /nova-aula).
"""
import datetime
import html
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(REPO, "Resumo_estudos", "mudancas.html")
LIMIT = 60

CSS = """
:root { --bg:#F5F4F0; --card:#FFFFFF; --ink:#1F2733; --text2:#55503F; --border:#E2DFD7;
        --line-strong:#B6B2A6; --amber:#B45309; --green:#0B5D3B; --blue:#2563EB; --red:#B91C1C; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg); color: var(--ink); font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; line-height: 1.55; }
.container { max-width: 760px; margin: 0 auto; padding: 2rem 1.2rem 4rem; }
.header { border-bottom: 2px solid var(--ink); padding-bottom: 1rem; margin-bottom: 1.6rem; }
.header h1 { font-family: 'Archivo', 'Segoe UI', sans-serif; font-size: 1.7rem; font-weight: 800; letter-spacing: -.03em; }
.header .sub { color: var(--text2); font-size: .85rem; margin-top: .2rem; }
.back { display: inline-block; margin-top: .8rem; color: var(--blue); font-size: .82rem; text-decoration: none; font-family: 'IBM Plex Mono', 'Consolas', monospace; }
.day { margin-bottom: 1.8rem; }
.day-title { font-family: 'Archivo', 'Segoe UI', sans-serif; font-size: 1.05rem; font-weight: 700;
             display: flex; align-items: center; gap: .5rem; margin-bottom: .6rem; }
.day-title .badge-new { background: #B45309; color: #fff; font-size: .65rem; font-family: 'IBM Plex Mono', 'Consolas', monospace;
                        padding: .15rem .45rem; border-radius: 4px; letter-spacing: .05em; }
.card { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: .75rem 1rem; margin-bottom: .55rem; }
.card.is-new { border-color: var(--amber); box-shadow: 0 0 0 1px var(--amber); }
.c-hash { font-family: 'IBM Plex Mono', 'Consolas', monospace; font-size: .68rem; color: var(--text2); }
.c-msg { font-size: .9rem; font-weight: 600; margin: .1rem 0 .25rem; }
.c-files { font-size: .8rem; color: var(--text2); }
.c-files a { color: var(--blue); text-decoration: none; }
.c-files a:hover { text-decoration: underline; }
.footer { margin-top: 2rem; color: var(--text2); font-size: .72rem; font-family: 'IBM Plex Mono', 'Consolas', monospace; }
"""


def run_git_log():
    cmd = ["git", "log", "-%d" % LIMIT,
           "--pretty=format:__C__%h|%ad|%s", "--date=short", "--name-only"]
    out = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, encoding="utf-8").stdout
    commits = []
    blocks = re.split(r"__C__", out)[1:]
    for block in blocks:
        lines = block.strip().splitlines()
        head = lines[0].split("|")
        if len(head) < 3:
            continue
        h, date, msg = head[0], head[1], "|".join(head[2:])
        paths = [p for p in lines[1:] if p.startswith("Resumo_estudos/")]
        commits.append({"h": h, "date": date, "msg": msg, "paths": paths})
    return commits


def friendly(path):
    m = re.match(r"Resumo_estudos/([^/]+)/(Aula \d+)/(resumo-.*)\.html$", path)
    if not m:
        return None, None
    name = re.sub(r"^resumo-aula-\d+-", "", m.group(3)).replace("-", " ").title()
    return m.group(1), "%s · %s" % (m.group(1), name)


def fmt_date(d):
    y, m, d = d.split("-")
    return "%02d/%02d/%04d" % (int(d), int(m), int(y))


def main():
    commits = run_git_log()
    by_day = {}
    for c in commits:
        by_day.setdefault(c["date"], []).append(c)
    days = sorted(by_day, reverse=True)

    body_parts = []
    for d in days:
        items = []
        for c in by_day[d]:
            links = []
            for p in c["paths"]:
                mat, label = friendly(p)
                if label:
                    links.append('<a href="%s">📄 %s</a>' % (html.escape(p), html.escape(label)))
            files = " · ".join(links) if links else '<span style="color:var(--text2);">(index / scripts / docs)</span>'
            items.append(
                '<div class="card">'
                '<div class="c-hash">%s</div>'
                '<div class="c-msg">%s</div>'
                '<div class="c-files">%s</div>'
                "</div>" % (c["h"], html.escape(c["msg"]), files))
        body_parts.append(
            '<div class="day" data-d="%s">'
            '<div class="day-title">%s<span class="badge-new" hidden>novo</span></div>%s</div>'
            % (d, fmt_date(d), "".join(items)))

    page = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>O que mudou — Resumos Hermes</title>
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#F5F4F0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>📜 O que mudou</h1>
    <div class="sub">Alterações recentes nos resumos (derivado do git log — adições TEC, novas aulas, correções)</div>
    <a class="back" href="/">← Voltar ao índice</a>
  </div>
  %s
  <div class="footer">Gerado por build-changelog.py em %s (horário de Brasília)</div>
</div>
<script>
(function(){
  var last = 0;
  try { last = parseInt(localStorage.getItem('rh-last-visit') || '0', 10); } catch (e) {}
  if (last > 0) {
    document.querySelectorAll('.day').forEach(function (day) {
      var t = Date.parse(day.getAttribute('data-d') + 'T12:00:00-03:00');
      if (t > last) day.querySelector('.badge-new').hidden = false;
    });
  }
  try { localStorage.setItem('rh-last-visit', String(Date.now())); } catch (e) {}
})();
</script>
</body>
</html>""" % (CSS, "".join(body_parts), datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("gerado:", OUT, "| commits:", len(commits), "| dias:", len(days))


if __name__ == "__main__":
    sys.exit(main())