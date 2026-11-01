from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG

e = HtmlInjectionEngine(verbose=True)
html = open('test_minimal_out.html', encoding='utf-8').read()
print('--- TESTE IDEMPOTÊNCIA ---')
print('Input has rhRev:', 'id="rhRev"' in html)
r = e.apply(html, REV_CONFIG)
print('Changed:', r is not None)
print('(deve ser None pois já tem id="rhRev")')