import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import importlib.util
spec = importlib.util.spec_from_file_location("apply_review_mode", "apply-review-mode.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
apply = mod.apply

path = 'test_resumo_real.html'
result = apply(path)
print('Applied:', result)

if result:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    print('Has rhRev:', 'id="rhRev"' in content)
    print('Has rh-rev CSS:', 'rh-rev' in content)
    print('Has rh-rev JS:', 'id="rh-rev"' in content)
    # Validate
    os.system('python tools/check-html.py ' + path)