import pathlib, re
p=pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 05/resumo-aula-05-jornada-de-trabalho-e-descansos.html')
txt=p.read_text(encoding='utf-8', errors='ignore')
titles=re.findall(r'<div class="sec-title">([^<]+)</div>', txt)
for t in titles:
    print(t)
