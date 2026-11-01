# ADR-002: Apply Scripts como Thin Adapters sobre Engine Compartilhado

**Status**: Aceito
**Data**: 2026-10-31
**Autores**: Fernando Brito

## Contexto

Existiam 5 scripts `apply-*.py` (`review-mode`, `marks-mode`, `search`, `practice-mode`, `pwa`), cada um com ~150 linhas reimplementando a mesma lógica:
1. Ler HTML
2. Checar idempotência (chave única)
3. Remover blocos v1 (upgrade)
4. Encontrar âncoras via regex (`</style>`, `</body>`, `<!--/rh:ui-->`, `id="rhTop"`)
5. Injetar CSS/JS/HTML nas posições
6. Escrever HTML

Problemas:
- **Duplicated Code**: ~500 linhas duplicadas
- **Shotgun Surgery**: Bug na injeção (ex: upgrade v1→v2 da busca) exigia corrigir em 5 lugares
- **Divergent Change**: Novo módulo / funcionalidade = editar 5 scripts
- **Testabilidade baixa**: Cada script acoplado a filesystem + regex frágeis

## Decisão

Extrair **engine compartilhado** (`tools/apply_shared.py`):
- `HtmlInjectionEngine` — lógica de injeção (âncoras, idempotência, upgrade, post-process)
- `ApplyConfig` — dataclass declarativa por módulo / funcionalidade (âncoras, CSS, JS, HTML, chaves)
- Configs pré-definidas: `REV_CONFIG`, `MARKS_CONFIG`, `SEARCH_CONFIG`, `PRACTICE_CONFIG`, `PWA_CONFIG`

Scripts `apply-*.py` viram **thin adapters** (~35-55 linhas cada):
```python
from apply_shared import HtmlInjectionEngine, REV_CONFIG
engine = HtmlInjectionEngine()
new_html = engine.apply(html, REV_CONFIG)
```

## Consequências

### Positivas
- **Locality**: Lógica de injeção em 1 lugar. Fix de bug propaga para 5 módulos / funcionalidades.
- **Leverage**: Novo módulo / funcionalidade = 1 `ApplyConfig` + ~20 linhas adapter (vs 150 linhas boilerplate).
- **Testabilidade**: `HtmlInjectionEngine` testável com fixtures HTML (input → output esperado).
- **Deletion Test**: Apagar `apply-review-mode.py` antigo concentra complexidade no engine — sinal verde.
- **Redução**: 725 → 255 linhas nos apply scripts (**65% menos**).

### Negativas / Riscos
- **Abstração vazada**: `HtmlInjectionEngine` expõe detalhes de regex/âncoras (mitigado: configs declarativas escondem complexidade).
- **Curva**: Novos devs precisam entender `ApplyConfig` + engine (documentado no GLOSSARY).

### Neutras
- Comportamento idêntico para usuário final (idempotência, upgrade v1→v2 preservados).
- `apply-pwa.py` mantido simples (usa `PWA_CONFIG` mas logic própria de reparo de toolbar).

## Alternativas Consideradas

1. **Classe base + herança** — Rejeitado: herança acopla, composition (engine + config) é mais flexível.
2. **Manter duplicação** — Rejeitado: não escala, bugs recorrentes (ex: busca v2 upgrade).
3. **Funções utilitárias soltas** — Rejeitado: não captura estado (idempotência, upgrade) de forma coesa.

## Referências

- [Glossário: Apply Scripts, Engine Compartilhado, Thin Adapter](./../../GLOSSARY.md)
- [ADR-001: Template Monolítico](./ADR-001-template-monolith-css-js-inline.md)
- [Skill: improve-codebase-arquitetura (Candidata 1)](.agents/skills/improve-codebase-architecture/SKILL.md)