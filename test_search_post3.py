import re

html = open('test_search_real3.html', encoding='utf-8').read()

idx1 = html.find('<div class="sr-box"')
idx2 = html.find('<div class="sidebar-sub">')
print(f'sr-box at {idx1}, sidebar-sub at {idx2}')
print('sr-box comes first:', idx1 < idx2)

# Extract the region between them
region = html[idx1:idx2+200]
# Save to file to avoid encoding issues
with open('debug_region.txt', 'w', encoding='utf-8') as f:
    f.write(region)
print('Region saved to debug_region.txt')
print('Length:', len(region))