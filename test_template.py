from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG

e = HtmlInjectionEngine(verbose=True)
html = open('Resumo_estudos/templates/template-sumario.html', encoding='utf-8').read()
r = e.apply(html, REV_CONFIG)
print('Changed:', r is not None)
if r:
    open('test_template_out.html', 'w', encoding='utf-8').write(r)
    print('Saved test_template_out.html')