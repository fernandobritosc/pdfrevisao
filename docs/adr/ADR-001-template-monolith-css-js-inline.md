# ADR-001: Template Monolítico com CSS/JS Inline

**Status**: Aceito
**Data**: 2026-09-24
**Autores**: Fernando Brito

## Contexto

O projeto nasceu com um template único (`template-sumario.html`) contendo HTML + CSS + JS tudo inline (1100+ linhas). Isso facilitava:
- Deploy simples (um arquivo)
- Zero dependências de build
- Facilidade de edição direta no navegador/editor

Porém, conforme features foram adicionadas (busca v1, busca v2, modo revisão, modo marcação, modo prática, PWA), o template ficou inchado e:
- CSS duplicado entre template e `index.html` (~400 linhas)
- Dificuldade de mudar design system (cores, tipografia, spacing) — exigia tocar múltiplos arquivos
- JS injetado via regex em 5 scripts `apply-*.py` diferentes (Shotgun Surgery)
- Testes visuais impossíveis sem renderizar página completa

## Decisão

Manter o template monolítico **como artefato gerado** (`Resumo_estudos/templates/template-sumario.html`), mas separar a **fonte** em:

1. **Design System** (`design-system/`) — tokens, componentes base, addons, módulos JS ESM
2. **Template Thin** (`template-thin.html`) — ~200 linhas, HTML estrutural + placeholders `{{CSS}}` `{{JS}}`
3. **Build Script** (`build.py`) — concatena, minifica, injeta, valida HTML

O template final gerado continua sendo um arquivo único HTML com tudo inline (para deploy simples), mas a **manutenção** acontece no design system modular.

## Consequências

### Positivas
- **Locality**: Tokens de cor/tipografia/spacing em `tokens.css` (1 linha para mudar cor da AFO)
- **Leverage**: `index.html` e resumos compartilham mesmo design system — elimina duplicação
- **Testabilidade**: Design system testável isolado; `build.py` valida HTML gerado via `check-html.py`
- **AI-navigabilidade**: LLM edita `tokens.css` para redesign global sem quebrar scripts apply
- **Migração facilitada**: `build.py` roda uma vez e regenera todos os 79 resumos no novo padrão

### Negativas / Riscos
- **Complexidade de build**: Novo script `build.py` + dependências (`cssmin`, `jsmin`)
- **Curva de aprendizado**: Estrutura `design-system/` vs template único anterior
- **Debug**: CSS/JS minificado no template final dificulta inspecionar no navegador (mitigado: source maps futuros)

### Neutras
- Deploy continua sendo arquivo único (sem mudança para o usuário final)
- Template final gerado continua válido para skill `/nova-aula`

## Alternativas Consideradas

1. **Manter template monolítico sem build** — Rejeitado: não escala, Shotgun Surgery persiste
2. **Separar CSS/JS em arquivos externos (não inline)** — Rejeitado: quebra deploy Surge simples (arquivo único), adiciona requests HTTP
3. **Usar bundler (Vite, Webpack)** — Rejeitado: overkill para projeto Python-first, adiciona Node.js dependency

## Referências

- [Glossário: Template, Design System, Build Pipeline](./../../GLOSSARY.md)
- [ADR-002: Apply Scripts como Thin Adapters](./ADR-002-apply-scripts-thin-adapters.md)
- [Issue: Migração visual obrigatória (25/09/2026)](AGENTS.md#L243)