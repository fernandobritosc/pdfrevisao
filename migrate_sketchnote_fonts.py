# -*- coding: utf-8 -*-
"""Migra fontes dos sketchnotes antigos para o trio aprovado (24/09):
Caveat + Space Grotesk + JetBrains Mono (+ IBM Plex Sans no corpo)."""
import io, re, os

ROOT = r'C:\Programação\hermes\PDF Revisão\Resumo_estudos'

NEW_LINK_A = ('<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&'
              'family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500;600&'
              'family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">')
OLD_LINK_A = '<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Archivo:wght@700;800&family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">'

NEW_LINK_B = ('<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&'
              'family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500;600&'
              'family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">')
OLD_LINK_B = '<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Patrick+Hand&family=Permanent+Marker&display=swap" rel="stylesheet">'

GROUP_A = [
    r'AFO\Aula 04\sketchnote-aula-04-orcamento-publico-conceito.html',
    r'Direito Administrativo\Aula 00\sketchnote-aula-00-principios-administrativos.html',
    r'Direito Constitucional\Aula 05\sketchnote-aula-05-nacionalidade.html',
]
GROUP_B = [
    r'Direito Administrativo\Aula 01\sketchnote-aula-01-estado-governo-e-administracao-publica.html',
    r'Direito Administrativo\Aula 02\sketchnote-aula-02-organizacao-administrativa.html',
    r'Direito Administrativo\Aula 06\sketchnote-aula-06-atos-administrativos.html',
]

for rel in GROUP_A:
    p = os.path.join(ROOT, rel)
    html = io.open(p, encoding='utf-8').read()
    if 'Archivo' not in html:
        print('pular (sem Archivo):', rel); continue
    html = html.replace(OLD_LINK_A, NEW_LINK_A)
    html = html.replace('font-family:Archivo', "font-family:'Space Grotesk'")
    # pill de tags (.biz span) vai para JetBrains Mono, como no DC Aula 04
    html, n = re.subn(r"(\.biz span\{[^}]*?)font-family:'Space Grotesk'",
                      r"\1font-family:'JetBrains Mono'", html)
    io.open(p, 'w', encoding='utf-8', newline='').write(html)
    print('grupo A ok:', rel, '| tags p/ JetBrains:', n)

for rel in GROUP_B:
    p = os.path.join(ROOT, rel)
    html = io.open(p, encoding='utf-8').read()
    if 'Permanent Marker' not in html:
        print('pular (sem Permanent Marker):', rel); continue
    html = html.replace(OLD_LINK_B, NEW_LINK_B)
    html = html.replace(
        "--f-display:'Permanent Marker','Segoe Print','Bradley Hand','Comic Sans MS',cursive",
        "--f-display:'Space Grotesk','Segoe UI',sans-serif")
    html = html.replace(
        "--f-body:'Patrick Hand','Segoe Print','Bradley Hand','Comic Sans MS',sans-serif",
        "--f-body:'IBM Plex Sans','Segoe UI',sans-serif")
    io.open(p, 'w', encoding='utf-8', newline='').write(html)
    print('grupo B ok:', rel)

# verificação: nenhum resquício
print('--- verificacao ---')
for rel in GROUP_A + GROUP_B:
    html = io.open(os.path.join(ROOT, rel), encoding='utf-8').read()
    resto = [w for w in ('Archivo', 'Permanent Marker', 'Patrick Hand', 'IBM Plex Mono') if w in html]
    print(os.path.basename(rel), '->', 'OK' if not resto else 'RESTOU: ' + ','.join(resto))
