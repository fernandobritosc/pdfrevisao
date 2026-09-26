# -*- coding: utf-8 -*-
# Migração visual em lote — matéria "Administração Pública e Geral"
# Variante A (Aulas 04, 05, 07): shell antigo completo (section-title, nav.sidebar, hero, progress, main)
# Variante B (Aulas 00-03): shell intermediário (sec-header e aside já presentes; troca CSS + cards + hero)
# Regras: conteúdo ZERO tocado; aborta o lote em qualquer falha.
import io, re, os, subprocess, sys

ROOT = r'C:\Programação\hermes\PDF Revisão\Resumo_estudos\Administração Pública e Geral'
DC = r'C:\Programação\hermes\PDF Revisão\Resumo_estudos\Direito Constitucional\Aula 04\resumo-aula-04-direitos-sociais.html'
CHECK = r'C:\Users\uniao\AppData\Local\Temp\opencode\check-html.py'
AP_TOKENS = {
    '--mat: #7c3aed;': '--mat: #0d9488;',
    '--mat-strong: #6d28d9;': '--mat-strong: #0b7a70;',
    '--mat-soft: #f3edfd;': '--mat-soft: #e6f4f2;',
    '--mat-line: #ddccf9;': '--mat-line: #b8e3de;',
    '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
        '--mat: #2dd4bf; --mat-strong: #7de0d6; --mat-soft: #0f3330; --mat-line: #14584f;',
}
MAT = '#0D9488'

# ---- blocos-fonte (DC04) ----
dc = io.open(DC, encoding='utf-8').read()
m_font = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?family=Space\+Grotesk[^"]*" rel="stylesheet">', dc)
assert m_font
FONT = m_font.group(0)
i = dc.index('<style>', m_font.end()); j = dc.index('</style>', i) + len('</style>')
BASE = dc[i:j]
i = dc.index('<style id="rh-addons">'); j = dc.index('</style>', i) + len('</style>')
RH = dc[i:j]
for a, b in AP_TOKENS.items():
    assert a in BASE or a in RH, 'token AP ausente: ' + a
    BASE = BASE.replace(a, b); RH = RH.replace(a, b)

def swap_font(h, log):
    h, n = re.subn(r'<link href="https://fonts\.googleapis\.com/css2\?family=Archivo[^"]*" rel="stylesheet">', FONT, h)
    log['font'] = n; assert n == 1, 'font'
    return h

def swap_css(h, log):
    i = h.index('<style>\n:root {')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + BASE + h[j:]; log['base'] = 1; return h

def swap_css_mid(h, log):
    i = h.index('<style>', h.index('<body') * 0 or 0)  # primeiro <style> do arquivo
    i = h.index('<style>')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + BASE + h[j:]; log['base'] = 1; return h

def swap_rh(h, log):
    i = h.index('<style id="rh-addons">')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + RH + h[j:]; log['rh'] = 1; return h

def conv_cards(h, log):
    h, n = re.subn(r'<div class="card-header"><div class="card-icon">[^<]*</div><div class="card-title"([^>]*)>(.*?)</div></div>',
                   r'<div class="card-title"\1>\2</div>', h)
    log['cards'] = n; return h

def conv_secs(h, log):
    h, n = re.subn(r'<div class="section-title"><span class="tag tag-(?:blue|amber|green|red)">(\d+)</span> (.*?)</div>',
                   r'<div class="sec-header">\n    <div class="sec-num">\1</div>\n    <div class="sec-title">\2</div>\n  </div>', h)
    log['secs'] = n
    h = h.replace('class="section-subtitle"', 'class="sec-subtitle"')
    return h

def rebuild_sidebar(h, aula, tema, log):
    i = h.index('<nav class="sidebar">')
    j = h.index('</nav>', i) + len('</nav>')
    links = re.findall(r'<a href="#sec\d+">[^<]+</a>', h[i:j])
    sec_links = '\n  '.join(links)
    new = ('<aside class="sidebar">\n'
           '  <div class="sidebar-title">Administração Pública e Geral — %s</div>\n'
           '  <div class="sidebar-sub">%s · Resumos estruturados</div>\n'
           '  <div class="sr-box">\n'
           '    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">\n'
           '    <div class="sr-info"><span id="sr-count"></span><button id="sr-clear" type="button">limpar</button></div>\n'
           '  </div>\n'
           '  <div class="sidebar-heading">Navegação</div>\n'
           '  ' + sec_links + '\n'
           '  <hr class="sidebar-divider">\n'
           '  <a href="../../../index.html" style="color:var(--mat-strong);font-size:.78rem;">← Voltar ao índice</a>\n'
           '</aside>') % (aula, tema)
    h = h[:i] + new + h[j:]; log['sidebar'] = 1; return h

def remove_hero(h, log):
    h, n = re.subn(r'  <!-- HEADER -->\n  <div class="header">.*?</div>\n', '', h, count=1, flags=re.S)
    if not n:
        h, n = re.subn(r'\n\n<div class="header">\n  <h1>.*?</h1>\n  <p>.*?</p>\n</div>\n', '', h, count=1, flags=re.S)
    log['hero'] = n; return h

def remove_progress(h, log):
    h, n1 = re.subn(r'  <!-- PROGRESS -->\n  <div class="progress-wrap">.*?</div>\n  </div>\n', '', h, count=1, flags=re.S)
    h, n2 = re.subn(r'<script>\n\(function\(\)\{\n  const sections.*?\n\}\)\(\);\n</script>\n', '', h, count=1, flags=re.S)
    log['progress'] = (n1, n2); return h

def fix_main(h, log):
    h = h.replace('<main class="main">', '<div class="main">', 1)
    h = h.replace('</main>', '</div><!-- .main -->', 1)
    log['main'] = 1; return h

def validate(path, h, aula):
    io.open(path, 'w', encoding='utf-8', newline='\n').write(h)
    r = subprocess.run([sys.executable, CHECK, path], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    ok = ('ERROS: zero' in out and 'ABERTAS: zero' in out)
    print('  [check-html]', out.replace('\n', ' '))
    resid = {p: h.count(p) for p in ['family=Archivo', '<div class="card-header">', 'class="section-title"', 'grid grid-2', '<main class="main"']}
    print('  [residuos]', resid)
    return ok and not any(resid.values())

# ---- Lote ----
BATCH_A = [('Aula 04', 'resumo-aula-04-estrutura-organizacional.html', 'Estrutura e Organização'),
           ('Aula 05', 'resumo-aula-05-lideranca.html', 'Liderança'),
           ('Aula 07', 'resumo-aula-07-comunicacao.html', 'Comunicação')]
BATCH_B = [('Aula 00', 'resumo-aula-00-conceitos-introdutorios.html', 'Conceitos Introdutórios'),
           ('Aula 01', 'resumo-aula-01-teorias-administrativas.html', 'Teorias Administrativas'),
           ('Aula 02', 'resumo-aula-02-planejamento-estrategico.html', 'Planejamento Estratégico'),
           ('Aula 03', 'resumo-aula-03-ferramentas-estrategicas.html', 'Ferramentas Estratégicas')]

falhas = []
for aula, f, tema in BATCH_A + BATCH_B:
    print('=' * 60)
    print(aula, '-', tema)
    p = os.path.join(ROOT, aula, f)
    h = io.open(p, encoding='utf-8').read()
    log = {}
    try:
        h = swap_font(h, log)
        h = swap_rh(h, log)
        if aula in ('Aula 04', 'Aula 05', 'Aula 07'):
            h = swap_css(h, log)
            h = conv_secs(h, log)
            h = rebuild_sidebar(h, aula, tema, log)
            h = remove_hero(h, log)
            h = remove_progress(h, log)
            h = fix_main(h, log)
        else:
            h = swap_css_mid(h, log)
            h = remove_hero(h, log)
        h = conv_cards(h, log)
    except Exception as e:
        print('  ERRO na transformação:', e); falhas.append((aula, e)); break
    print('  log:', log)
    if not validate(p, h, aula):
        print('  FALHOU validação — lote abortado'); falhas.append((aula, 'validação')); break

print('=' * 60)
print('RESULTADO:', 'OK — 7 aulas migradas' if not falhas else 'FALHAS: %s' % falhas)
