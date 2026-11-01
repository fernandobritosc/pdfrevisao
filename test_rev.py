from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG

e = HtmlInjectionEngine(verbose=True)
html = open('Resumo_estudos/templates/template-sumario.html', encoding='utf-8').read()
r = e.apply(html, REV_CONFIG)
print('Changed:', r is not None)
print('Has rhRev:', 'id="rhRev"' in (r or html))