# -*- coding: utf-8 -*-
import io, re, sys

AP = r'C:\Programação\hermes\PDF Revisão\Resumo_estudos\Administração Pública e Geral\Aula 06\resumo-aula-06-motivacao.html'
DC = r'C:\Programação\hermes\PDF Revisão\Resumo_estudos\Direito Constitucional\Aula 04\resumo-aula-04-direitos-sociais.html'

ap = io.open(AP, encoding='utf-8').read()
dc = io.open(DC, encoding='utf-8').read()

# --- extract blocks from DC04 (piloto) ---
m_font = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?family=Space\+Grotesk[^"]*" rel="stylesheet">', dc)
assert m_font, 'font link nao achado'
FONT = m_font.group(0)

i = dc.index('<style>', m_font.end())
j = dc.index('</style>', i) + len('</style>')
BASE_CSS = dc[i:j]

i = dc.index('<style id="rh-addons">')
j = dc.index('</style>', i) + len('</style>')
RH = dc[i:j]

# --- AP tokens (teal #0D9488) ---
BASE_CSS = BASE_CSS.replace('--mat: #7c3aed;', '--mat: #0d9488;')
BASE_CSS = BASE_CSS.replace('--mat-strong: #6d28d9;', '--mat-strong: #0b7a70;')
BASE_CSS = BASE_CSS.replace('--mat-soft: #f3edfd;', '--mat-soft: #e6f4f2;')
BASE_CSS = BASE_CSS.replace('--mat-line: #ddccf9;', '--mat-line: #b8e3de;')
RH = RH.replace('--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;',
                '--mat: #2dd4bf; --mat-strong: #7de0d6; --mat-soft: #0f3330; --mat-line: #14584f;')

orig = ap
n_changes = {}

# 1) font link
ap, n = re.subn(r'<link href="https://fonts\.googleapis\.com/css2\?family=Archivo[^"]*" rel="stylesheet">', FONT, ap)
n_changes['font'] = n

# 2) base css (primeiro bloco <style> ... </style>)
i = ap.index('<style>\n:root {')
j = ap.index('</style>', i) + len('</style>')
ap = ap[:i] + BASE_CSS + ap[j:]
n_changes['base_css'] = 1

# 3) rh-addons
i = ap.index('<style id="rh-addons">')
j = ap.index('</style>', i) + len('</style>')
ap = ap[:i] + RH + ap[j:]
n_changes['rh'] = 1

# 4) section-title -> sec-header
def sec_repl(m):
    return ('<div class="sec-header">\n    <div class="sec-num">%s</div>\n'
            '    <div class="sec-title">%s</div>\n  </div>') % (m.group(1), m.group(2))
ap, n = re.subn(r'<div class="section-title"><span class="tag tag-(?:blue|amber|green)">(\d+)</span> (.*?)</div>', sec_repl, ap)
n_changes['sec_title'] = n

# 5) section-subtitle -> sec-subtitle
ap = ap.replace('class="section-subtitle"', 'class="sec-subtitle"')
n_changes['subtitle'] = orig.count('class="section-subtitle"')

# 6) card-header/icon -> card-title
ap, n = re.subn(r'<div class="card-header"><div class="card-icon">[^<]*</div><div class="card-title"([^>]*)>(.*?)</div></div>',
                r'<div class="card-title"\1>\2</div>', ap)
n_changes['card_header'] = n

# 7) sidebar nova
sb_start = ap.index('<nav class="sidebar">')
sb_end = ap.index('</nav>', sb_start) + len('</nav>')
links = re.findall(r'<a href="#sec\d+">[^<]+</a>', orig[sb_start:sb_end])
sec_links = '\n  '.join(links)
NEW_SB = (
    '<aside class="sidebar">\n'
    '  <div class="sidebar-title">Administração Pública e Geral — Aula 06</div>\n'
    '  <div class="sidebar-sub">Motivação · Resumos estruturados</div>\n'
    '  <div class="sr-box">\n'
    '    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">\n'
    '    <div class="sr-info"><span id="sr-count"></span><button id="sr-clear" type="button">limpar</button></div>\n'
    '  </div>\n'
    '  <div class="sidebar-heading">Navegação</div>\n'
    '  ' + sec_links + '\n'
    '  <hr class="sidebar-divider">\n'
    '  <a href="../../../index.html" style="color:var(--mat-strong);font-size:.78rem;">← Voltar ao índice</a>\n'
    '</aside>'
)
ap = ap[:sb_start] + NEW_SB + ap[sb_end:]
n_changes['sidebar'] = 1

# 8) remover hero header
ap, n = re.subn(r'  <!-- HEADER -->\n  <div class="header">.*?</div>\n', '', ap, count=1, flags=re.S)
n_changes['hero'] = n

# 9) remover progress html
ap, n = re.subn(r'  <!-- PROGRESS -->\n  <div class="progress-wrap">.*?</div>\n  </div>\n', '', ap, count=1, flags=re.S)
n_changes['progress_html'] = n

# 10) remover script de progresso
ap, n = re.subn(r'<script>\n\(function\(\)\{\n  const sections.*?\n\}\)\(\);\n</script>\n', '', ap, count=1, flags=re.S)
n_changes['progress_js'] = n

# 11) main -> div
ap = ap.replace('<main class="main">', '<div class="main">', 1)
ap = ap.replace('</main>', '</div><!-- .main -->', 1)
n_changes['main'] = 1

io.open(AP, 'w', encoding='utf-8', newline='\n').write(ap)
print('OK', n_changes)
# residuos
for pat in ['Archivo', 'card-header', 'section-title', 'grid grid-2', 'progress-wrap">\n', '<main']:
    c = ap.count(pat)
    print('residuo %-16s: %d' % (pat, c))
