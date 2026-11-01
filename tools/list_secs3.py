import pathlib, re
p=pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 03/resumo-aula-03-contrato-de-trabalho.html')
txt=p.read_text(encoding='utf-8', errors='ignore')
titles=re.findall(r'<div class="sec-title">([^<]+)</div>', txt)
for t in titles:
    print(t)
