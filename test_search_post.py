import re

html = open('test_search_real2.html', encoding='utf-8').read()

# Testa o pattern do post_process
pattern = r'(  <div class="sr-box" data-sr-v="2">[\s\S]*?</div>\n)(  <div class="sidebar-sub">.*?</div>\n)'
match = re.search(pattern, html, re.S)
print('Match:', match)
if match:
    print('Group 1:', repr(match.group(1)[:100]))
    print('Group 2:', repr(match.group(2)[:100]))

# O HTML real tem indentação diferente
# Vamos ver o HTML real ao redor
idx = html.find('<div class="sr-box"')
print('\n--- HTML real (sr-box) ---')
print(repr(html[idx:idx+200]))

idx2 = html.find('<div class="sidebar-sub">')
print('\n--- HTML real (sidebar-sub) ---')
print(repr(html[idx2:idx2+100]))