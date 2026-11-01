import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools"))

from apply_shared import HtmlInjectionEngine, PWA_CONFIG

e = HtmlInjectionEngine(verbose=True)
html = open('test_pwa_out.html', encoding='utf-8').read()
r = e.apply(html, PWA_CONFIG)
print('Idempotent (should be None):', r is None)