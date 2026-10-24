import pathlib, re
for aula in [5,6]:
    p=pathlib.Path(f'Resumo_estudos/Direito do Trabalho/Aula {aula:02d}/resumo-aula-{aula:02d}-*')
    # find file
import glob
files=glob.glob('Resumo_estudos/Direito do Trabalho/Aula 05/resumo-aula-05-*.html')
print(files)
