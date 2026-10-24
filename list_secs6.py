import pathlib, re
p=pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 06/resumo-aula-06-remuneracao-e-salario.html')
txt=p.read_text(encoding='utf-8', errors='ignore')
titles=re.findall(r'<div class="sec-title">([^<]+)</div>', txt)
for t in titles:
    print(t)
