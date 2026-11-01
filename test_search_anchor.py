import re

html = open('test_search_real.html', encoding='utf-8').read()

# Testa o anchor do SEARCH_CONFIG
anchor = r'^([ \t]*<div class="sidebar-sub">.*?</div>\n)'
print('Testing anchor:', anchor)

match = re.search(anchor, html, re.M | re.S)
print('Match:', match)
if match:
    print('Group 1:', repr(match.group(1)))
    print('Start:', match.start(1), 'End:', match.end(1))

# Procura sidebar-sub no HTML
idx = html.find('<div class="sidebar-sub">')
print('\nsidebar-sub found at:', idx)
if idx != -1:
    print('Context:', html[idx:idx+100])