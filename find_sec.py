import pathlib, re
p = pathlib.Path('Resumo_estudos/Direito do Trabalho/Aula 06/resumo-aula-06-remuneracao-e-salario.html')
txt = p.read_text(encoding='utf-8', errors='ignore')
# find first occurrence of insalubridade
idx = txt.lower().find('insalubridade')
if idx != -1:
    # find previous sec-title
    prev = txt.rfind('<div class="sec-title">', 0, idx)
    if prev != -1:
        start = txt.find('>', prev) + 1
        end = txt.find('</div>', start)
        sec = txt[start:end]
        print('Section:', sec)
    else:
        print('no sec title')
else:
    print('not found')
