from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG
import re

e = HtmlInjectionEngine(verbose=True)
html = open('test_minimal.html', encoding='utf-8').read()

# Testa o regex do anchor
anchor = REV_CONFIG.html_anchor
print('Anchor pattern:', anchor.replace('\u2191', '\\u2191'))
match = re.search(anchor, html)
print('Match:', match)
if match:
    print('Match group:', repr(match.group(0)).replace('\u2191', '\\u2191'))
    print('Match start:', match.start())
    print('Match end:', match.end())

# Testa o post_process pattern
test_html = html[:match.end()] + '\n  <button type="button" id="rhRev" title="Modo revisão: oculte e se auto-teste" aria-label="Alternar modo revisão" aria-pressed="false">🧠</button>' + html[match.end():]
print('\n--- HTML simulado com injeção ANTES do match ---')
print(test_html[match.start():match.end()+200])

pattern = r'(<button type="button" id="rhRev"[^>]*>🧠</button>)(<button type="button" id="rhTop"[^>]*>↑</button>)'
match2 = re.search(pattern, test_html)
print('\nPost-process match:', match2)
if match2:
    print('Groups:', match2.groups())