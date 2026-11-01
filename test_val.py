from tools.check_html import validate_file
from pathlib import Path
errors, open_tags, details = validate_file(Path('test_marks_real.html'))
print('Errors:', errors)
print('Open:', open_tags)
for d in details:
    print('  ', d)