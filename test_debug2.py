from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG
import re

e = HtmlInjectionEngine(verbose=True)
html = open('test_minimal.html', encoding='utf-8').read()

# Testa o regex do anchor
anchor = REV_CONFIG.html_anchor
match = re.search(anchor, html)
print('Match found:', match is not None)
if match:
    g = match.group(0)
    print('Match start:', match.start())
    print('Match end:', match.end())
    print('Match length:', len(g))

# Simula o que o engine faz: injeta ANTES do match.start()
injected = '\n  <button type="button" id="rhRev" title="Modo revisão" aria-label="Alternar modo revisão" aria-pressed="false">🧠</button>'
new_html = html[:match.start()] + injected + html[match.start():]

# Testa o post_process pattern
pattern = r'(<button type="button" id="rhRev"[^>]*>🧠</button>)(<button type="button" id="rhTop"[^>]*>↑</button>)'
match2 = re.search(pattern, new_html)
print('\nPost-process match found:', match2 is not None)
if match2:
    print('Groups:', match2.groups())
    # Aplica o fix
    fixed = re.sub(pattern, r'\2\1', new_html, count=1)
    print('\n--- FIXED (around rhTop) ---')
    print(fixed[match.start()-50:match.end()+150])