import pathlib
p = pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 05/resumo-aula-05-jornada-de-trabalho-e-descansos.html')
txt = p.read_text(encoding='utf-8', errors='ignore')
insert = '<div class="card" id="rh-next"><div class="card-title">Próxima aula</div><div class="card-text">→ <a href="../Aula 06/resumo-aula-06-remuneracao-e-salario.html">Aula 06 — Remuneração e Salário</a></div></div>\n'
if '</body>' in txt:
    txt = txt.replace('</body>', insert + '</body>')
    p.write_text(txt, encoding='utf-8')
    print('inserted')
else:
    print('no body')
