# ADR-003: Busca v2 com Navegação + E Lógico Multi-palavra

**Status**: Aceito
**Data**: 2026-10-14
**Autores**: Fernando Brito

## Contexto

Busca v1 (set/2026): filtro simples + destaque âmbar. Limitações:
- Sem navegação entre ocorrências
- Busca de palavra única
- Sem contador de posição

Usuário pediu (14/10/2026):
1. Navegação: botões ↑/↓ + Enter (próxima) / Shift+Enter (anterior) + contador "n/m" (ocorrência atual em vermelho)
2. Busca multi-palavra: E lógico — cada palavra digitada deve estar presente no bloco, cada uma com seu destaque âmbar
3. Upgrade idempotente: arquivos v1 reprocessados automaticamente

## Decisão

Implementar **busca v2** como módulo / funcionalidade completa no design system:
- CSS: `design-system/css/addons/search.css` (estilos `.sr-box`, `.sr-nav`, `mark.sr-hit`, `mark.sr-first`)
- JS: `design-system/js/modules/search-v2.js` (TreeWalker + normalização NFD + E lógico + navegação)
- Config: `SEARCH_CONFIG` no `apply_shared.py` com upgrade automático v1→v2
- Injeção no sidebar: após `<div class="sidebar-sub">` (via `html_anchor` + `inject_html_after=True`)

Idempotência: chave `data-sr-v="2"` no container `.sr-box`.

## Consequências

### Positivas
- **UX**: Navegação fluida entre ocorrências (Enter/Shift+Enter + botões), contador "n/m"
- **Precisão**: Busca multi-palavra com E lógico reduz falsos positivos
- **Idempotência robusta**: Detecta v1 (sem `data-sr-v`) e migra automaticamente
- **Integração**: Funciona com dark mode, print mode, modo revisão

### Negativas / Riscos
- **Complexidade JS**: TreeWalker + normalização Unicode + navegação stateful (~200 linhas)
- **Performance**: Em resumos muito longos, highlight pode ser lento (mitigado: filtra blocos antes)

### Neutras
- v1 migrada transparente para 79 resumos existentes

## Alternativas Consideradas

1. **Biblioteca externa (Fuse.js, Lunr)** — Rejeitado: overkill, adiciona dependência, busca é simples (substring match)
2. **Manter v1** — Rejeitado: UX insuficiente para revisão ativa

## Referências

- [Glossário: Busca v2, Apply Scripts](./../../GLOSSARY.md)
- [ADR-002: Apply Scripts Thin Adapters](./ADR-002-apply-scripts-thin-adapters.md)
- Regra do usuário: 25/09/2026 (aprovado em teste DC Aula 04, expandido 61 resumos), v2 14/10/2026 (67 resumos)