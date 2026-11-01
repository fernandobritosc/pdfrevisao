from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG
import re

html = open('test_minimal.html', encoding='utf-8').read()
anchor = REV_CONFIG.html_anchor
match = re.search(anchor, html)

injected = '\n  <button type="button" id="rhRev" title="Modo revisão" aria-label="Alternar modo revisão" aria-pressed="false">🧠</button>'
new_html = html[:match.start()] + injected + html[match.start():]

# Salva em arquivo para inspecionar
with open('debug_injected.html', 'w', encoding='utf-8') as f:
    f.write(new_html[match.start()-20:match.end()+200])

print('HTML salvo em debug_injected.html')

# Testa o post_process pattern
pattern = r'(<button type="button" id="rhRev"[^>]*>🧠</button>)(<button type="button" id="rhTop"[^>]*>↑</button>)'
match2 = re.search(pattern, new_html)
print('Post-process match found:', match2 is not None)
if match2:
    print('Groups:', match2.groups())