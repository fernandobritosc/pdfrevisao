content = open(r'C:\Programação\pdfrevisao-main\pdf revisao\Resumo_estudos\Administração Pública e Geral\Aula 04\resumo-aula-04-estrutura-organizacional.html', encoding='utf-8').read()
import re
# Search for font links
for m in re.finditer(r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]*" rel="stylesheet">', content):
    print(m.group())

# Also check for Archivo
if 'Archivo' in content:
    print('Archivo found')
else:
    print('Archivo NOT found')