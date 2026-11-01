import re

html = open('test_search_real3.html', encoding='utf-8').read()

# Testa o pattern do post_process
pattern = r'(<div class="sr-box" data-sr-v="2">[\s\S]*?</div>\n)(\s*<div class="sidebar-sub">.*?</div>\n)'
match = re.search(pattern, html, re.S)
print('Match:', match)
if match:
    print('Group 1:', repr(match.group(1)[:150]))
    print('Group 2:', repr(match.group(2)[:150]))
else:
    print('No match - checking structure')
    idx1 = html.find('<div class="sr-box"')
    idx2 = html.find('<div class="sidebar-sub">')
    print(f'sr-box at {idx1}, sidebar-sub at {idx2}')
    print('Between:', repr(html[idx1:idx2+100]))