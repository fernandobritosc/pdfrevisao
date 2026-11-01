# -*- coding: utf-8 -*-
"""
apply-search.py — injeta o campo de busca por palavra (filtro + destaque + navegação) nos resumos.

v2 (14/10/2026):
  - navegação entre ocorrências: botões ↑/↓ + Enter (próxima) / Shift+Enter (anterior)
    + contador de posição "n/m" (a ocorrência atual fica com o destaque vermelho);
  - busca multi-palavra: cada palavra digitada é procurada separadamente no bloco
    (todas devem estar presentes — E lógico) e cada uma ganha seu destaque âmbar;
  - upgrade idempotente: arquivos com a v1 (id="sr-script" sem data-sr-v) são
    reprocessados — o bloco antigo é removido e o novo injetado no mesmo lugar.

Idempotente: pula arquivos que já tenham data-sr-v="2". Reexecutar após regenerar
resumos pelo template (padrão dos demais apply-*.py).

Uso: python apply-search.py            (todos os resumo-aula-*.html de Resumo_estudos)
     python apply-search.py ARQUIVO    (um arquivo específico)

Refatorado para usar apply_shared.HtmlInjectionEngine + SEARCH_CONFIG.
"""
import glob
import io
import os
import sys

# Adiciona tools ao path para importar apply_shared
TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from apply_shared import HtmlInjectionEngine, SEARCH_CONFIG, TOOLBAR_CSS, ensure_rev_button

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resumo_estudos')

engine = HtmlInjectionEngine(verbose=True)


def apply(path: str) -> bool:
    with io.open(path, encoding='utf-8') as fh:
        content = fh.read()

    new_content = engine.apply(content, SEARCH_CONFIG)
    if new_content is None:
        return False

    # Reparo extra: garante toolbar CSS + botão 🧠 se não existirem
    if "rh-toolbar" not in new_content and "rh-toolbar" not in content:
        idx = new_content.rfind("</style>")
        if idx != -1:
            new_content = new_content[:idx] + TOOLBAR_CSS + new_content[idx:]
    new_content = ensure_rev_button(new_content)

    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(new_content)
    return True


def main():
    targets = sys.argv[1:] or sorted(
        glob.glob(os.path.join(ROOT, '**', 'resumo-aula-*.html'), recursive=True)
    )
    ok = skip = fail = 0
    for f in targets:
        if apply(f):
            ok += 1
            print('atualizado:', os.path.relpath(f, ROOT))
        else:
            # Verifica se já tem a v2
            with io.open(f, encoding='utf-8') as fh:
                original = fh.read()
            if 'data-sr-v="2"' in original:
                skip += 1
            else:
                fail += 1
                print('FALHA (âncora não encontrada):', f)
    print('---')
    print('atualizados:', ok, '| já na v2 (pulos):', skip, '| falhas:', fail)


if __name__ == '__main__':
    sys.exit(main())