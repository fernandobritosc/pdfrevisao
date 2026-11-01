import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import importlib.util
spec = importlib.util.spec_from_file_location("apply_marks_mode", "apply-marks-mode.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
apply = mod.apply

path = 'Resumo_estudos/templates/template-sumario.html'
result = apply(path)
print('Applied:', result)

if result:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    print('Has rhMarks:', 'id="rhMarks"' in content)
    print('Has rh-marks CSS:', 'rh-marked' in content)
    print('Has rh-marks JS:', 'id="rh-marks"' in content)
    os.system('python tools/check-html.py ' + path)