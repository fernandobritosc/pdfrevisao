# -*- coding: utf-8 -*-
"""Migração visual em lote para todas as matérias — usa DC04 como referência."""
import io, re, os, subprocess, sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DC = REPO_ROOT / 'Resumo_estudos' / 'Direito Constitucional' / 'Aula 04' / 'resumo-aula-04-direitos-sociais.html'
CHECK = REPO_ROOT / 'tools' / 'check-html.py'

# Mapeamento: chave do BATCHES -> nome real do diretório no filesystem
DIR_NAMES = {
    'AFO': 'AFO',
    'AP': 'Administração Pública e Geral',
    'AD': 'Direito Administrativo',
    'DC': 'Direito Constitucional',
    'DT': 'Direito do Trabalho',
    'DPT': 'Direito Processual do Trabalho',
    'PT': 'Português',
    'INF': 'Informática',
    'Contabilidade Pública': 'Contabilidade Pública',
    'Legislação institucional - TCE': 'Legislação institucional - TCE',
}

# Matérias e suas cores
SUBJECTS = {
    'AFO': {
        'color': '#16a34a',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #16a34a;',
            '--mat-strong: #6d28d9;': '--mat-strong: #147a3c;',
            '--mat-soft: #f3edfd;': '--mat-soft: #e8f5e9;',
            '--mat-line: #ddccf9;': '--mat-line: #c8e6c9;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #4ade80; --mat-strong: #86efac; --mat-soft: #0f2e17; --mat-line: #1a5c2e;',
        }
    },
    'AP': {
        'color': '#0d9488',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #0d9488;',
            '--mat-strong: #6d28d9;': '--mat-strong: #0b7a70;',
            '--mat-soft: #f3edfd;': '--mat-soft: #e6f4f2;',
            '--mat-line: #ddccf9;': '--mat-line: #b8e3de;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #2dd4bf; --mat-strong: #7de0d6; --mat-soft: #0f3330; --mat-line: #14584f;',
        }
    },
    'AD': {
        'color': '#2563eb',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #2563eb;',
            '--mat-strong: #6d28d9;': '--mat-strong: #1d4ed8;',
            '--mat-soft: #f3edfd;': '--mat-soft: #e8effd;',
            '--mat-line: #ddccf9;': '--mat-line: #c3d5fa;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #6ea8fe; --mat-strong: #a9c3ef; --mat-soft: #1d2739; --mat-line: #33507e;',
        }
    },
    'DC': {
        'color': '#7c3aed',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #7c3aed;',
            '--mat-strong: #6d28d9;': '--mat-strong: #6d28d9;',
            '--mat-soft: #f3edfd;': '--mat-soft: #f3edfd;',
            '--mat-line: #ddccf9;': '--mat-line: #ddccf9;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;',
        }
    },
    'DT': {
        'color': '#d97706',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #d97706;',
            '--mat-strong: #6d28d9;': '--mat-strong: #b45309;',
            '--mat-soft: #f3edfd;': '--mat-soft: #fdf3d8;',
            '--mat-line: #ddccf9;': '--mat-line: #fde68a;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #fbbf24; --mat-strong: #fde047; --mat-soft: #361f00; --mat-line: #5c2e00;',
        }
    },
    'DPT': {
        'color': '#dc2626',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #dc2626;',
            '--mat-strong: #6d28d9;': '--mat-strong: #b91c1c;',
            '--mat-soft: #f3edfd;': '--mat-soft: #fef2f2;',
            '--mat-line: #ddccf9;': '--mat-line: #fecaca;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #f87b7b; --mat-strong: #fca5a5; --mat-soft: #3b0a0a; --mat-line: #7f1d1d;',
        }
    },
    'PT': {
        'color': '#0891b2',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #0891b2;',
            '--mat-strong: #6d28d9;': '--mat-strong: #0e7490;',
            '--mat-soft: #f3edfd;': '--mat-soft: #e0f2fe;',
            '--mat-line: #ddccf9;': '--mat-line: #bae6fd;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #22d3ee; --mat-strong: #67e8f9; --mat-soft: #0c1f2e; --mat-line: #155e75;',
        }
    },
    'INF': {
        'color': '#3b82f6',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #3b82f6;',
            '--mat-strong: #6d28d9;': '--mat-strong: #2563eb;',
            '--mat-soft: #f3edfd;': '--mat-soft: #eff6ff;',
            '--mat-line: #ddccf9;': '--mat-line: #bfdbfe;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #60a5fa; --mat-strong: #93c5fd; --mat-soft: #1e3a5f; --mat-line: #1e40af;',
        }
    },
    'Contabilidade Pública': {
        'color': '#64748b',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #64748b;',
            '--mat-strong: #6d28d9;': '--mat-strong: #475569;',
            '--mat-soft: #f3edfd;': '--mat-soft: #f1f5f9;',
            '--mat-line: #ddccf9;': '--mat-line: #e2e8f0;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #94a3b8; --mat-strong: #cbd5e1; --mat-soft: #0f172a; --mat-line: #334155;',
        }
    },
    'Legislação institucional - TCE': {
        'color': '#0d9488',
        'tokens': {
            '--mat: #7c3aed;': '--mat: #0d9488;',
            '--mat-strong: #6d28d9;': '--mat-strong: #0b7a70;',
            '--mat-soft: #f3edfd;': '--mat-soft: #e6f4f2;',
            '--mat-line: #ddccf9;': '--mat-line: #b8e3de;',
            '--mat: #b39af5; --mat-strong: #c9b6f2; --mat-soft: #2b2145; --mat-line: #4c3a75;':
                '--mat: #2dd4bf; --mat-strong: #7de0d6; --mat-soft: #0f3330; --mat-line: #14584f;',
        }
    },
}

# ---- blocos-fonte (DC04) ----
dc = io.open(DC, encoding='utf-8').read()
m_font = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?family=Space\+Grotesk[^"]*" rel="stylesheet">', dc)
assert m_font
FONT = m_font.group(0)
i = dc.index('<style>', m_font.end()); j = dc.index('</style>', i) + len('</style>')
BASE_DC = dc[i:j]
i = dc.index('<style id="rh-addons">'); j = dc.index('</style>', i) + len('</style>')
RH_DC = dc[i:j]

# Pre-compute BASE and RH for each subject
SUBJECT_BASE = {}
SUBJECT_RH = {}
for subj, cfg in SUBJECTS.items():
    base = BASE_DC
    rh = RH_DC
    for a, b in cfg['tokens'].items():
        base = base.replace(a, b)
        rh = rh.replace(a, b)
    SUBJECT_BASE[subj] = base
    SUBJECT_RH[subj] = rh

def swap_font(h, log):
    h, n = re.subn(r'<link href="https://fonts\.googleapis\.com/css2\?family=Archivo[^"]*" rel="stylesheet">', FONT, h)
    log['font'] = n
    return h

def swap_css(h, base_css, log):
    i = h.find('<style>\n:root {')
    if i == -1:
        i = h.find('<style>')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + base_css + h[j:]
    log['base'] = 1
    return h

def swap_rh(h, rh_css, log):
    i = h.index('<style id="rh-addons">')
    j = h.index('</style>', i) + len('</style>')
    h = h[:i] + rh_css + h[j:]
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

def rebuild_sidebar(h, subject, aula, tema, log):
    sb_start = h.find('<nav class="sidebar">')
    if sb_start == -1:
        sb_start = h.find('<aside class="sidebar">')
    if sb_start == -1:
        log['sidebar'] = 'not found'
        return h
    if '</nav>' in h[sb_start:]:
        sb_end = h.index('</nav>', sb_start) + len('</nav>')
    else:
        sb_end = h.index('</aside>', sb_start) + len('</aside>')
    links = re.findall(r'<a href="#sec\d+">[^<]+</a>', h[sb_start:sb_end])
    sec_links = '\n  '.join(links)
    new = ('<aside class="sidebar">\n'
           '  <div class="sidebar-title">%s — %s</div>\n'
           '  <div class="sidebar-sub">%s · Resumos estruturados</div>\n'
           '  <div class="sr-box">\n'
           '    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">\n'
           '    <div class="sr-info"><span id="sr-count"></span><button id="sr-clear" type="button">limpar</button></div>\n'
           '  </div>\n'
           '  <div class="sidebar-heading">Navegação</div>\n'
           '  ' + sec_links + '\n'
           '  <hr class="sidebar-divider">\n'
           '  <a href="../../../index.html" style="color:var(--mat-strong);font-size:.78rem;">← Voltar ao índice</a>\n'
           '</aside>') % (subject, aula, tema)
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

def validate(path, h):
    io.open(path, 'w', encoding='utf-8', newline='\n').write(h)
    r = subprocess.run([sys.executable, str(CHECK), str(path)], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    ok = ('[OK]' in out and 'OK' in out)
    print('  [check-html]', out.replace('\n', ' '))
    resid = {p: h.count(p) for p in ['family=Archivo', '<div class="card-header">', 'class="section-title"', 'grid grid-2', 'grid grid-3', '<main class="main"']}
    print('  [residuos]', resid)
    return ok and not any(resid.values())

# ---- Lotes por matéria (usando chaves que correspondem a SUBJECTS) ----
BATCHES = {
    'AFO': [
        ('Aula 00', 'resumo-aula-00-orcamento-publico.html', 'Orçamento Público'),
        ('Aula 01', 'resumo-aula-01-principios-orcamentarios.html', 'Princípios Orçamentários'),
        ('Aula 03', 'resumo-aula-03-ciclo-orcamentario.html', 'Ciclo Orçamentário'),
        ('Aula 04', 'resumo-aula-04-orcamento-publico-conceito.html', 'Orçamento Público - Conceito'),
        ('Aula 05', 'resumo-aula-05-divida-ativa.html', 'Dívida Ativa'),
        ('Aula 05', 'resumo-aula-05-receita-publica-consolidado.html', 'Receita Pública Consolidado'),
        ('Aula 06', 'resumo-aula-06-despesas-publicas.html', 'Despesas Públicas'),
        ('Aula 07', 'resumo-aula-07-classificamentos-orcamentarios-estrutura-programatica.html', 'Classificações Orçamentárias'),
    ],
    'AP': [
        ('Aula 00', 'resumo-aula-00-conceitos-introdutorios.html', 'Conceitos Introdutórios'),
        ('Aula 01', 'resumo-aula-01-teorias-administrativas.html', 'Teorias Administrativas'),
        ('Aula 02', 'resumo-aula-02-planejamento-estrategico.html', 'Planejamento Estratégico'),
        ('Aula 03', 'resumo-aula-03-ferramentas-estrategicas.html', 'Ferramentas Estratégicas'),
        ('Aula 04', 'resumo-aula-04-estrutura-organizacional.html', 'Estrutura e Organização'),
        ('Aula 05', 'resumo-aula-05-lideranca.html', 'Liderança'),
        ('Aula 06', 'resumo-aula-06-motivacao.html', 'Motivação'),
        ('Aula 07', 'resumo-aula-07-comunicacao.html', 'Comunicação'),
        ('Aula 08', 'resumo-aula-08-controle-avaliacao-indicadores.html', 'Controle, Avaliação e Indicadores'),
    ],
    'AD': [
        ('Aula 00', 'resumo-aula-00-principios-administrativos.html', 'Princípios Administrativos'),
        ('Aula 01', 'resumo-aula-01-estado-governo-e-administracao-publica.html', 'Estado, Governo e Administração Pública'),
        ('Aula 02', 'resumo-aula-02-organizacao-administrativa.html', 'Organização Administrativa'),
        ('Aula 03', 'resumo-aula-03-fundacoes-empresas-publicas-sociedades-de-economia-mista.html', 'Fundações, Empresas Públicas e Sociedades de Economia Mista'),
        ('Aula 04', 'resumo-aula-04-paraestatais-e-terceiro-setor.html', 'Paraestatais e Terceiro Setor'),
    ],
    'DC': [
        ('Aula 00', 'resumo-aula-00-natureza-conceito-interpretacao.html', 'Natureza, Conceito e Interpretação'),
        ('Aula 03', 'resumo-aula-03-direitos-e-deveres-individuais-coletivos.html', 'Direitos e Deveres Individuais e Coletivos'),
        ('Aula 05', 'resumo-aula-05-nacionalidade.html', 'Nacionalidade'),
        ('Aula 06', 'resumo-aula-06-direitos-politicos.html', 'Direitos Políticos'),
        ('Aula 07', 'resumo-aula-07-partidos-politicos.html', 'Partidos Políticos'),
    ],
    'DT': [
        ('Aula 00', 'resumo-aula-00-relacoes-de-trabalho-e-emprego.html', 'Relações de Trabalho e Emprego'),
        ('Aula 01', 'resumo-aula-01-principios-do-direito-do-trabalho.html', 'Princípios do Direito do Trabalho'),
        ('Aula 02', 'resumo-aula-02-relacoes-de-trabalho-e-emprego.html', 'Relações de Trabalho e Emprego'),
        ('Aula 03', 'resumo-aula-03-contrato-de-trabalho.html', 'Contrato de Trabalho'),
        ('Aula 04', 'resumo-aula-04-termino-do-contrato-de-trabalho.html', 'Término do Contrato de Trabalho'),
        ('Aula 05', 'resumo-aula-05-jornada-de-trabalho-e-descansos.html', 'Jornada de Trabalho e Descansos'),
    ],
    'DPT': [
        ('Aula 00', 'resumo-aula-00-processo-do-trabalho.html', 'Processo do Trabalho'),
        ('Aula 01', 'resumo-aula-01-competencia-da-justica-do-trabalho.html', 'Competência da Justiça do Trabalho'),
        ('Aula 02', 'resumo-aula-02-servicos-auxiliares-da-justica-do-trabalho.html', 'Serviços Auxiliares da Justiça do Trabalho'),
        ('Aula 03', 'resumo-aula-03-prazos-custas-nulidades-peticao-inicial.html', 'Prazos, Custas, Nulidades e Petição Inicial'),
        ('Aula 04', 'resumo-aula-04-notificacao-do-reclamado.html', 'Notificação do Reclamado'),
    ],
    'PT': [
        ('Aula 01', 'resumo-aula-01-classes-palavras.html', 'Classes de Palavras'),
        ('Aula 02', 'resumo-aula-02-preposicoes-conjuncoes.html', 'Preposições e Conjunções'),
        ('Aula 03', 'resumo-aula-03-pronomes-colocacao.html', 'Pronomes e Colocação'),
        ('Aula 04', 'resumo-aula-04-classe-palavras-verbos.html', 'Classe de Palavras - Verbos'),
        ('Aula 05', 'resumo-aula-05-funcoes-sintaticas.html', 'Funções Sintáticas'),
        ('Aula 06', 'resumo-aula-06-relacoes-coordenacao-entre-oracoes.html', 'Relações de Coordenação entre Orações'),
    ],
    'INF': [
        ('Aula 02', 'resumo-aula-02-sitios-de-busca-e-pesquisa.html', 'Sítios de Busca e Pesquisa'),
        ('Aula 03', 'resumo-aula-03-computacao-em-nuvem.html', 'Computação em Nuvem'),
        ('Aula 04', 'resumo-aula-04-redes-sociais.html', 'Redes Sociais'),
        ('Aula 05', 'resumo-aula-05-internet-e-navegacao.html', 'Internet e Navegação'),
        ('Aula 06', 'resumo-aula-06-correio-eletronico.html', 'Correio Eletrônico'),
    ],
    'Contabilidade Pública': [
        ('Aula 00', 'resumo-aula-00-aspectos-introdutorios.html', 'Aspectos Introdutórios'),
    ],
    'Legislação institucional - TCE': [
        ('Aula 00', 'resumo-aula-00-administracao-publica.html', 'Administração Pública'),
    ],
}

def process_subject(subject, batch):
    print('=' * 60)
    print(f'PROCESSANDO: {subject} ({len(batch)} arquivos)')
    print('=' * 60)
    
    dir_name = DIR_NAMES.get(subject, subject)
    subject_root = REPO_ROOT / 'Resumo_estudos' / dir_name
    base_css = SUBJECT_BASE[subject]
    rh_css = SUBJECT_RH[subject]
    
    falhas = []
    for aula, f, tema in batch:
        print(f'\n{aula} - {tema}')
        p = subject_root / aula / f
        if not p.exists():
            print('  ARQUIVO NÃO ENCONTRADO')
            falhas.append((aula, 'arquivo não encontrado'))
            continue
        h = io.open(p, encoding='utf-8').read()
        log = {}
        try:
            h = swap_font(h, log)
            h = swap_css(h, base_css, log)
            h = swap_rh(h, rh_css, log)
            h = conv_cards(h, log)
            h = conv_secs(h, log)
            h = remove_grid(h, log)
            h = fix_main(h, log)
            h = rebuild_sidebar(h, subject, aula, tema, log)
            h = remove_hero(h, log)
            h = remove_progress(h, log)
        except Exception as e:
            print(f'  ERRO na transformação: {e}')
            falhas.append((aula, str(e)))
            continue
        print('  log:', log)
        if not validate(p, h):
            print('  FALHOU validação')
            falhas.append((aula, 'validação'))
    return falhas

def main():
    all_falhas = []
    for subject, batch in BATCHES.items():
        if subject not in SUBJECTS:
            print(f'Matéria não configurada: {subject}')
            continue
        falhas = process_subject(subject, batch)
        all_falhas.extend([(subject, a, e) for a, e in falhas])
    
    print('\n' + '=' * 60)
    print('RESULTADO FINAL')
    print('=' * 60)
    if not all_falhas:
        total = sum(len(b) for b in BATCHES.values())
        print(f'OK — {total} aulas migradas')
    else:
        for subj, aula, err in all_falhas:
            print(f'FALHA: {subj} - {aula}: {err}')

if __name__ == '__main__':
    main()