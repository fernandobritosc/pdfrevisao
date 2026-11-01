import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import importlib.util
spec = importlib.util.spec_from_file_location("apply_search", "apply-search.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
apply = mod.apply

path = 'test_search_real4.html'
result = apply(path)
print('Applied:', result)

if result:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    print('Has sr-box v2:', 'data-sr-v="2"' in content)
    print('Has sr-style:', 'id="sr-style"' in content)
    print('Has sr-script:', 'id="sr-script"' in content)
    print('Has sr-input:', 'id="sr-input"' in content)
    os.system('python tools/check-html.py ' + path)