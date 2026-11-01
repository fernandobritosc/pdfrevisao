# ADR-004: Modo Prática Vive DENTRO do Resumo (Não Workspace à Parte)

**Status**: Aceito
**Data**: 2026-10-09
**Autores**: Fernando Brito

## Contexto

Modo prática (quiz de recall 🎯) precisava de armazenamento e UI. Opções:
1. **Workspace separado** — arquivo `practice.html` à parte, linkado do resumo
2. **Dentro do resumo** — injetado no mesmo HTML do resumo, toggle via botão 🎯 na toolbar

Usuário decidiu (09/10/2026): **dentro do resumo**.
- Regra: toda aula encerrada ganha `quiz.json` (4-8 questões) + injeção
- Camada de prática mora **DENTRO do resumo** (não em workspace à parte)

## Decisão

Implementar como módulo / funcionalidade injetada no HTML do resumo:
- CSS: `design-system/css/addons/practice.css` (painel flutuante `#rhPracticePanel`)
- JS: `design-system/js/modules/practice-mode.js` (lê `quiz.json` via `<script type="application/json" id="rhPracticeData">`)
- HTML: painel + botão 🎯 na toolbar (via `apply_shared.PRACTICE_CONFIG`)
- Dados: `quiz.json` na pasta da aula (versionado no git)
- Idempotência: marcador `<!--rh:practice:start-->` / `<!--rh:practice:end-->`

Botão 🎯 aparece após 🧠 (reparo automático se toolbar existe mas 🎯 não).

## Consequências

### Positivas
- **Experiência unificada**: Estudante não sai do resumo para praticar
- **Offline-first**: `quiz.json` + JS no mesmo HTML = funciona offline (PWA)
- **Deploy simples**: Um arquivo só, sem rotas extras no Surge
- **Contexto preservado**: Modo revisão (🧠) + prática (🎯) na mesma toolbar

### Negativas / Riscos
- **Tamanho do HTML**: Adiciona ~3KB por resumo (quiz + painel + JS)
- **Complexidade de injeção**: Precisa injetar `quiz.json` dinamicamente no `rhPracticeData` (resolvido via `post_process` no `apply_shared`)

### Neutras
- `quiz.json` versionado no git = histórico de questões por aula

## Alternativas Consideradas

1. **Workspace separado (`practice.html`)** — Rejeitado: quebra UX unificada, deploy extra, contexto perdido
2. **Iframe para `practice.html`** — Rejeitado: complexidade de comunicação, CSP, offline quebrado
3. **SPA separada** — Rejeitado: overkill, quebra deploy simples

## Referências

- [Glossário: Quiz, Modo Prática, Apply Scripts](./../../GLOSSARY.md)
- [ADR-002: Apply Scripts Thin Adapters](./ADR-002-apply-scripts-thin-adapters.md)
- Regra do usuário: 09/10/2026 (toda aula encerrada ganha quiz.json + injeção)