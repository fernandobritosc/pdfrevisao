import pathlib, re
p = pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 05/resumo-aula-05-jornada-de-trabalho-e-descansos.html')
txt = p.read_text(encoding='utf-8', errors='ignore')
# replace any link that contains Índice geral with link to Aula 06
pattern = re.compile(r'<a href="[^"]+">Próxima[^<]*Índice geral</a>')
replacement = '<a href="../Aula 06/resumo-aula-06-remuneracao-e-salario.html">Próxima → Aula 06 — Remuneração e Salário</a>'
new_txt, count = pattern.subn(replacement, txt)
if count:
    p.write_text(new_txt, encoding='utf-8')
    print('replaced', count)
else:
    # fallback: replace href of link containing Índice geral
    pattern2 = re.compile(r'(<a href="[^"]+">[^<]*Índice geral</a>)')
    new_txt2 = re.sub(pattern2, '<a href="../Aula 06/resumo-aula-06-remuneracao-e-salario.html">Próxima → Aula 06 — Remuneração e Salário</a>', txt)
    if new_txt2 != txt:
        p.write_text(new_txt2, encoding='utf-8')
        print('replaced fallback')
    else:
        print('no match')
