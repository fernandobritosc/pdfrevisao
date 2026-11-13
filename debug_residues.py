import io, re, os
from pathlib import Path

REPO_ROOT = Path(r'C:\Programação\pdfrevisao-main\pdf revisao')

# Check a few files from validation output
files_to_check = [
    'Resumo_estudos/AFO/Aula 00/resumo-aula-00-orcamento-publico.html',
    'Resumo_estudos/AFO/Aula 01/resumo-aula-01-principios-orcamentarios.html',
    'Resumo_estudos/Direito Administrativo/Aula 00/resumo-aula-00-principios-administrativos.html',
    'Resumo_estudos/Direito Constitucional/Aula 00/resumo-aula-00-natureza-conceito-interpretacao.html',
    'Resumo_estudos/Direito do Trabalho/Aula 00/resumo-aula-00-relacoes-de-trabalho-e-emprego.html',
    'Resumo_estudos/Português/Aula 01/resumo-aula-01-classes-palavras.html',
]

for rel in files_to_check:
    p = REPO_ROOT / rel
    if p.exists():
        content = io.open(p, encoding='utf-8').read()
        has_archivo = 'Archivo' in content
        has_space_grotesk = 'Space Grotesk' in content
        has_card_header = '<div class="card-header">' in content
        has_section_title = 'class="section-title"' in content
        has_grid2 = 'grid grid-2' in content
        has_grid3 = 'grid grid-3' in content
        has_main = '<main class="main">' in content
        has_sec_subtitle = 'class="section-subtitle"' in content
        print(f'{rel}:')
        print(f'  Archivo={has_archivo}, SpaceGrotesk={has_space_grotesk}')
        print(f'  card-header={has_card_header}, section-title={has_section_title}')
        print(f'  grid2={has_grid2}, grid3={has_grid3}, main={has_main}, sec-subtitle={has_sec_subtitle}')
        # Show font link
        for m in re.finditer(r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]*" rel="stylesheet">', content):
            print(f'  Font: {m.group()}')
        print()
    else:
        print(f'{rel}: NOT FOUND')