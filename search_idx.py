import pathlib
p = pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 05/resumo-aula-05-jornada-de-trabalho-e-descansos.html')
txt = p.read_text(encoding='utf-8', errors='ignore')
i = txt.find('Índice geral')
if i != -1:
    snippet = txt[max(0,i-200):i+200]
    pathlib.Path('snippet_out.txt').write_text(snippet, encoding='utf-8')
    print('written')
else:
    print('not found')
