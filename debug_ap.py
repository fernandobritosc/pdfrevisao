import io, re, os
from pathlib import Path

REPO_ROOT = Path(r'C:\Programação\pdfrevisao-main\pdf revisao')
ROOT = REPO_ROOT / 'Resumo_estudos' / 'Administração Pública e Geral'

BATCH_A = [('Aula 04', 'resumo-aula-04-estrutura-organizacional.html'),
           ('Aula 05', 'resumo-aula-05-lideranca.html'),
           ('Aula 07', 'resumo-aula-07-comunicacao.html')]
BATCH_B = [('Aula 00', 'resumo-aula-00-conceitos-introdutorios.html'),
           ('Aula 01', 'resumo-aula-01-teorias-administrativas.html'),
           ('Aula 02', 'resumo-aula-02-planejamento-estrategico.html'),
           ('Aula 03', 'resumo-aula-03-ferramentas-estrategicas.html')]

for aula, f in BATCH_A + BATCH_B:
    p = ROOT / aula / f
    if p.exists():
        content = io.open(p, encoding='utf-8').read()
        has_archivo = 'Archivo' in content
        has_space_grotesk = 'Space Grotesk' in content
        has_card_header = '<div class="card-header">' in content
        has_section_title = 'class="section-title"' in content
        has_grid2 = 'grid grid-2' in content
        has_grid3 = 'grid grid-3' in content
        has_main = '<main class="main">' in content
        print(f'{aula}: Archivo={has_archivo}, SpaceGrotesk={has_space_grotesk}, card-header={has_card_header}, section-title={has_section_title}, grid2={has_grid2}, grid3={has_grid3}, main={has_main}')
    else:
        print(f'{aula}: FILE NOT FOUND')