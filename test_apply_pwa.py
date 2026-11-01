import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools"))

from apply_shared import HtmlInjectionEngine, PWA_CONFIG

e = HtmlInjectionEngine(verbose=True)

# Testa em arquivo mínimo
html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Teste PWA</title>
<style>
body { font-family: sans-serif; }
</style>
</head>
<body>
<h1>Teste</h1>
</body>
</html>"""

r = e.apply(html, PWA_CONFIG)
print('Changed:', r is not None)
if r:
    print('Has manifest:', 'rel="manifest"' in r)
    print('Has SW register:', 'serviceWorker.register' in r)
    print('Has theme-color:', 'theme-color' in r)
    # Valida
    with open('test_pwa_out.html', 'w', encoding='utf-8') as f:
        f.write(r)
    os.system('python tools/check-html.py test_pwa_out.html')