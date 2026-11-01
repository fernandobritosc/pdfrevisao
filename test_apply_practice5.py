import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import importlib.util
spec = importlib.util.spec_from_file_location("apply_practice_mode", "apply-practice-mode.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
process = mod.process

path = 'test_practice_dir4/resumo-teste.html'
msgs = process(path)
with open('test_out.txt', 'w', encoding='utf-8') as f:
    f.write(str(msgs))

if msgs:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    with open('test_out.txt', 'a', encoding='utf-8') as f:
        f.write('\nHas practice panel: ' + str('id="rhPracticePanel"' in content))
        f.write('\nHas practice btn: ' + str('id="rhPractice"' in content))
        f.write('\nHas practice data: ' + str('id="rhPracticeData"' in content))
        f.write('\nPractice data content: ' + str('questoes' in content))
        f.write('\nrh-practice count: ' + str(content.count('id="rh-practice"')))
    os.system('python tools/check-html.py ' + path + ' > test_html_out.txt 2>&1')