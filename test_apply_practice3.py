import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import importlib.util
spec = importlib.util.spec_from_file_location("apply_practice_mode", "apply-practice-mode.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
process = mod.process

path = 'test_practice_dir3/resumo-teste.html'
msgs = process(path)
print('Messages:', msgs)

if msgs:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    print('Has practice panel:', 'id="rhPracticePanel"' in content)
    print('Has practice btn:', 'id="rhPractice"' in content)
    print('Has practice data:', 'id="rhPracticeData"' in content)
    print('Practice data content:', 'questoes' in content)
    print('rh-practice count:', content.count('id="rh-practice"'))
    os.system('python tools/check-html.py ' + path)