import pathlib
p = pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 05/resumo-aula-05-jornada-de-trabalho-e-descansos.html')
txt = p.read_text(encoding='utf-8', errors='ignore')
old = '<a class="next" href="../../index.html" rel="next"><span class="aula-nav-dir">próxima →</span><span class="aula-nav-label">Índice geral</span></a>'
new = '<a class="next" href="../Aula 06/resumo-aula-06-remuneracao-e-salario.html" rel="next"><span class="aula-nav-dir">próxima →</span><span class="aula-nav-label">Aula 06 — Remuneração e Salário</span></a>'
if old in txt:
    txt = txt.replace(old, new)
    p.write_text(txt, encoding='utf-8')
    print('replaced')
else:
    # try with different encoding of arrow
    # fallback search
    import re
    pattern = re.compile(r'<a class="next" href="../../index.html" rel="next"><span class="aula-nav-dir">[^<]+</span><span class="aula-nav-label">Índice geral</span></a>')
    new_txt = pattern.sub(new, txt)
    if new_txt != txt:
        p.write_text(new_txt, encoding='utf-8')
        print('replaced regex')
    else:
        print('not found')
