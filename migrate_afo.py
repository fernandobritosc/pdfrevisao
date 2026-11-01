# -*- coding: utf-8 -*-
"""Migração visual AFO — usa DC04 como referência, adapta cor para AFO (#16A34A)."""
import io, re, os, subprocess, sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DC = REPO_ROOT / 'Resumo_estudos' / 'Direito Constitucional' / 'Aula 04' / 'resumo-aula-04-direitos-sociais.html'
AFO_ROOT = REPO_ROOT / 'Resumo_estudos' / 'AFO'
CHECK = REPO_ROOT / 'tools' / 'check-html.py'

# AFO color tokens
AFO_TOKENS = {
    '--mat: #7c3aed;': '--mat: #16a34a;',
    '--mat-strong: #6d28d9;': '--mat-strong: #147a3c;',
    '--mat-soft: #f3edfd;': '--mat-soft: #e8f5e9;',
    '--mat-line: #ddccf9;': '--mat-line: #c8e6c9;',
    '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
        '--mat: #4ade80; --mat-strong: #86efac; --mat-soft: #0f2e17; --mat-line: #1a5c2e;',
}

# ---- blocos-fonte (DC04) ----
dc = io.open(DC, encoding='utf-8').read()
m_font = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?family=Space\+Grotesk[^"]*" rel="stylesheet">', dc)
assert m_font
FONT = m_font.group(0)
i = dc.index('<style>', m_font.end()); j = dc.index('</style>', i) + len('</style>')
BASE = dc[i:j]
i = dc.index('<style id="rh-addons">'); j = dc.index('</style>', i) + len('</style>')
RH = dc[i:j]
for a, b in AFO_TOKENS.items():
    assert a in BASE or a in RH, 'token AFO ausente: ' + a
    BASE = BASE.replace(a, b); RH = RH.replace(a, b)

def swap_font(h, log):
    h, n = re.subn(r'<link href="https://fonts\.googleapis\.com/css2\?family=Archivo[^"]*" rel="stylesheet">', FONT, h)
    log['font'] = n
    return h

def swap_css(h, log):
    # Find first <style> block with :root
    i = h.find('<style>\n:root {')
    if i == -1:
        i = h.find('<style>')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + BASE + h[j:]
    log['base'] = 1
    return h

def swap_rh(h, log):
    i = h.index('<style id="rh-addons">')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + RH + h[j:]
    log['rh'] = 1
    return h

def conv_cards(h, log):
    h, n = re.subn(r'<div class="card-header"><div class="card-icon">[^<]*</div><div class="card-title"([^>]*)>(.*?)</div></div>',
                   r'<div class="card-title"\1>\2</div>', h)
    log['cards'] = n
    return h

def conv_secs(h, log):
    h, n = re.subn(r'<div class="section-title"><span class="tag tag-(?:blue|amber|green|red)">(\d+)</span> (.*?)</div>',
                   r'<div class="sec-header">\n    <div class="sec-num">\1</div>\n    <div class="sec-title">\2</div>\n  </div>', h)
    log['secs'] = n
    h = h.replace('class="section-subtitle"', 'class="sec-subtitle"')
    return h

def remove_grid(h, log):
    # Remove grid-2 and grid-3 classes
    h = h.replace('class="grid grid-2"', 'class="grid"')
    h = h.replace('class="grid grid-3"', 'class="grid"')
    h = h.replace('class="grid-2"', 'class="grid"')
    h = h.replace('class="grid-3"', 'class="grid"')
    log['grid'] = 1
    return h

def fix_main(h, log):
    h = h.replace('<main class="main">', '<div class="main">', 1)
    h = h.replace('</main>', '</div><!-- .main -->', 1)
    log['main'] = 1
    return h

def rebuild_sidebar(h, aula, tema, log):
    # Find existing sidebar (nav or aside)
    sb_start = h.find('<nav class="sidebar">')
    if sb_start == -1:
        sb_start = h.find('<aside class="sidebar">')
    if sb_start == -1:
        log['sidebar'] = 'not found'
        return h
    sb_end = h.index('</nav>', sb_start) + len('</nav>') if '</nav>' in h[sb_start:] else h.index('</aside>', sb_start) + len('</aside>')
    links = re.findall(r'<a href="#sec\d+">[^<]+</a>', h[sb_start:sb_end])
    sec_links = '\n  '.join(links)
    new = ('<aside class="sidebar">\n'
           '  <div class="sidebar-title">AFO — %s</div>\n'
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
    h = h[:sb_start] + new + h[sb_end:]
    log['sidebar'] = 1
    return h

def remove_hero(h, log):
    h, n = re.subn(r'  <!-- HEADER -->\n  <div class="header">.*?</div>\n', '', h, count=1, flags=re.S)
    if not n:
        h, n = re.subn(r'\n\n<div class="header">\n  <h1>.*?</h1>\n  <p>.*?</p>\n</div>\n', '', h, count=1, flags=re.S)
    log['hero'] = n
    return h

def remove_progress(h, log):
    h, n1 = re.subn(r'  <!-- PROGRESS -->\n  <div class="progress-wrap">.*?</div>\n  </div>\n', '', h, count=1, flags=re.S)
    h, n2 = re.subn(r'<script>\n\(function\(\)\{\n  const sections.*?\n\}\)\(\);\n</script>\n', '', h, count=1, flags=re.S)
    log['progress'] = (n1, n2)
    return h

def validate(path, h, aula):
    io.open(path, 'w', encoding='utf-8', newline='\n').write(h)
    r = subprocess.run([sys.executable, str(CHECK), str(path)], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    ok = ('[OK]' in out and 'OK' in out)
    print('  [check-html]', out.replace('\n', ' '))
    resid = {p: h.count(p) for p in ['family=Archivo', '<div class="card-header">', 'class="section-title"', 'grid grid-2', 'grid grid-3', '<main class="main"']}
    print('  [residuos]', resid)
    return ok and not any(resid.values())

# ---- Lote AFO ----
BATCH = [
    ('Aula 00', 'resumo-aula-00-orcamento-publico.html', 'Orçamento Público'),
    ('Aula 01', 'resumo-aula-01-principios-orcamentarios.html', 'Princípios Orçamentários'),
    ('Aula 03', 'resumo-aula-03-ciclo-orcamentario.html', 'Ciclo Orçamentário'),
    ('Aula 04', 'resumo-aula-04-orcamento-publico-conceito.html', 'Orçamento Público - Conceito'),
    ('Aula 05', 'resumo-aula-05-divida-ativa.html', 'Dívida Ativa'),
    ('Aula 05', 'resumo-aula-05-receita-publica-consolidado.html', 'Receita Pública Consolidado'),
    ('Aula 06', 'resumo-aula-06-despesas-publicas.html', 'Despesas Públicas'),
    ('Aula 07', 'resumo-aula-07-classificamentos-orcamentarios-estrutura-programatica.html', 'Classificações Orçamentárias'),
]

falhas = []
for aula, f, tema in BATCH:
    print('=' * 60)
    print(aula, '-', tema)
    p = AFO_ROOT / aula / f
    if not p.exists():
        print('  ARQUIVO NÃO ENCONTRADO')
        falhas.append((aula, 'arquivo não encontrado'))
        continue
    h = io.open(p, encoding='utf-8').read()
    log = {}
    try:
        h = swap_font(h, log)
        h = swap_css(h, log)
        h = swap_rh(h, log)
        h = conv_cards(h, log)
        h = conv_secs(h, log)
        h = remove_grid(h, log)
        h = fix_main(h, log)
        h = rebuild_sidebar(h, aula, tema, log)
        h = remove_hero(h, log)
        h = remove_progress(h, log)
    except Exception as e:
        print('  ERRO na transformação:', e)
        falhas.append((aula, e))
        continue
    print('  log:', log)
    if not validate(p, h, aula):
        print('  FALHOU validação — lote abortado')
        falhas.append((aula, 'validação'))
        break

print('=' * 60)
print('RESULTADO:', 'OK — %d aulas migradas' % len(BATCH) if not falhas else 'FALHAS: %s' % falhas)