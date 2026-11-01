from tools.apply_shared import HtmlInjectionEngine, REV_CONFIG

e = HtmlInjectionEngine(verbose=True)
html = open('test_minimal.html', encoding='utf-8').read()
print('--- ANTES ---')
print('Has rhRev:', 'id="rhRev"' in html)
print('Has rhTop:', 'id="rhTop"' in html)
print('Has rh:ui:', '<!--/rh:ui-->' in html)

r = e.apply(html, REV_CONFIG)
print('\n--- DEPOIS ---')
print('Changed:', r is not None)
if r:
    print('Has rhRev:', 'id="rhRev"' in r)
    print('Has CSS rh-rev:', 'rh-rev' in r)
    print('Has JS rh-rev:', 'id="rh-rev"' in r)
    # Salva para inspeção
    open('test_minimal_out.html', 'w', encoding='utf-8').write(r)
    print('Salvo em test_minimal_out.html')