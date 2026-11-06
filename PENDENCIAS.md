# Pendências — Migração visual dos resumos

**Última atualização:** 06/11/2026
**Estado:** migração dos 79 resumos concluída, validada e publicada no Surge.
**Contexto:** continuidade do processo por etapas (Onda 1 → Ondas 2/3), executado nesta sessão.

---

## 1. O que já está concluído

| Item | Resultado |
|---|---|
| CSS de página | 79/79 resumos com o CSS canônico de `Resumo_estudos/templates/template-sumario.html` (fim das variantes legadas) |
| Tokens `--mat` | 79/79 com bloco `<style id="rh-mat">` (claro e escuro) por matéria |
| `--mat` por matéria | AFO `#16a34a`, AP `#0d9488`, AD `#2563eb`, DC `#7c3aed`, DT `#d97706`, DPT `#0891b2`, PT `#0891b2`, CP `#db2777`, INF `#3b82f6`, RML `#65a30d`, LI-TCE `#475569` |
| `text-align: justify` | 0 ocorrências nos resumos |
| Numeral de seção no dark | `color:var(--mat)` em todos (bug antigo de `#8ab0fe`/`#17191f` corrigido na fonte `design-system/css/addons/dark-mode.css`) |
| Regras próprias de página | preservadas em `<style id="rh-page-extra">`; hoje resta **1 página** (AP Aula 08, `.sec-subtitle.destaque`) |
| Regras mortas removidas | `.dot*` (0 páginas usam) e `.aula .sidebar{display:none}` no mobile (quebrava a gaveta ☰) |
| Mobile | padding de seção 20 px em ≤768 px e header 1.5rem/1rem (antes: 48 px de cada lado) |
| Acessibilidade | `prefers-reduced-motion` global no CSS canônico |
| Fontes | JetBrains Mono incluída na URL do Google Fonts nos 79 |
| QA | 79 páginas × 1280/390 × claro/escuro: 0 problemas (overflow, add-ons, alinhamento, numeral ≡ faixa do card, erros de JS); gaveta ☰ testada em todas |
| HTML | `check-html.py --dir Resumo_estudos --check`: 79/79 OK, 0 erros |
| Build | `build-search-index.py` (79 resumos / 760 seções) e `build-changelog.py` regenerados; `tools/validate-all.py` OK |
| Deploy | `npx surge ./Resumo_estudos resumos-hermes.surge.sh` — HTTP 200 em `/`, AP 00, RML 00, AFO 07, `mudancas.html`; gaveta e `.destaque` conferidos no domínio publicado |

---

## 2. Pendências (em ordem de prioridade)

### P1 — Data do index · 5 min · bloqueio: aprovação
- **Arquivo:** [Resumo_estudos/index.html](../Resumo_estudos/index.html) — linha 342
- **Hoje:** `01/11/2026` · **correto:** `06/11/2026`
- **Ação:** trocar o `<div class="sc-value date">01/11/2026</div>` e republicar.
- **Por que não foi feito:** o AGENTS.md manda atualizar a data ao marcar revisão; esta sessão foi manutenção visual, não revisão de aula.

### P2 — Documentar as ferramentas no AGENTS.md · 10 min · bloqueio: aprovação
Adicionar na seção "Scripts de build" (após `apply-a11y.py`):

```markdown
- `audit_visual_migration.py` → só leitura: agrupa os resumos por folha de estilo
  e aponta o que falta do padrão travado (tokens, justify, dark, numeral, card, th).
- `apply-visual-migration.py` → aplica a migração por ondas:
  `--wave swap-a` (variantes com 3+ páginas), `--wave swap-b` (variantes isoladas),
  `--wave tokens` (bloco `#rh-mat`), `--wave dark` (numeral no dark),
  `--wave extras` (limpa/preserva `#rh-page-extra`). `--dry-run` lista tudo antes;
  preserva regras próprias de página e é idempotente (2ª execução = 0 arquivos).
```

### P3 — Borda azul inline em 5 cards da Administração Pública · 10 min · bloqueio: aprovação (conteúdo)
- **Páginas:** AP Aulas 00, 01, 04, 05 e 06
- **O quê:** o primeiro card de cada página tem `<div class="card" style="border-left: 4px solid var(--blue);">` — azul fixo, destoando do `--mat` teal e da faixa de 5 px.
- **Ação sugerida:** remover o atributo `style` inline (o padrão já aplica a faixa na cor da matéria).
- **Por que não foi feito:** alteração de conteúdo HTML exige confirmação (regra "Sugestões de melhoria").

### P4 — `.dot` voltar ao design system se necessário · decisão futura
- As regras `.dot`, `.dot.a|b|c|g|p|r` (bolinhas de legenda) existiam nos CSS legados, mas **nenhuma página as usa** no corpo. Foram descartadas.
- Se uma aula nova usar `<span class="dot">`, incluir o utilitário em `design-system/css/base.css` antes.

### P5 — Variantes de `rh-addons` · opcional
- Existem **10 variantes** do bloco `<style id="rh-addons">` (de 4 KB a 12,6 KB). Duas (AFO Aula 07 e DC Aula 08) não tinham o `@media (max-width:900px)` da navegação — já corrigidas no lugar.
- Consolidar todas na versão canônica é possível, mas mexe em bloco compartilhado com JS (`rh-init`, toolbar, revisão, marcação); baixo ganho, risco médio.

### P6 — Sketchnotes · decisão de escopo
- Os 28 sketchnotes receberam apenas o pacote de a11y (skip link, `#conteudo`, `scope="col"`, menu mobile). **Não** passaram pela migração `--mat` (têm layout próprio, sem tokens).
- Se quiser que sketchnotes sigam a cor da matéria, é um trabalho separado (não foi pedido e não estava na Onda 1/2/3).

### P7 — Backlog antigo (não tocado)
De `BACKLOG.md`:
- **A:** passo de verificação de seções finais na skill `/nova-aula`.
- **B:** incidência TEC agregada por matéria (aguardando ideia do usuário).

### P8 — Badge de revisão 🆕/🔁
- Não registrado: esta sessão foi manutenção visual do site, não estudo/revisão de aula. Se o usuário tratar como aula, atualizar o badge no index (regra do encerramento) junto com P1.

### P9 — Conferir a CI após o push
- `.github/workflows/ci.yml` roda em push para `main`: build + testes + validação e, em seguida, o job **deploy-surge** publica o artefato `site`.
- Após o push, conferir a execução: `gh run list --branch main --limit 3` e `gh run view <id>`.
- O deploy manual já foi feito; a CI republica o mesmo conteúdo montado a partir de `Resumo_estudos`.

### P10 — Ambientes ao continuar em outra máquina
- Python: o build exige `PyMuPDF`, `cssmin`, `jsmin` (ver `requirements`/`build.py`).
- Playwright: `npm install` (devDependencies `playwright`/`@playwright/test`) e `npx playwright install chromium`.
- Servidor local para QA: servir a raiz do repo em `http://localhost:8765` (os scripts esperam esse endereço).
- Surge: `npx surge ./Resumo_estudos resumos-hermes.surge.sh` (login em `~/.netrc` ou `SURGE_LOGIN`/`SURGE_TOKEN`).

---

## 3. Como reproduzir a validação

```bash
# 1. HTML balanceado
python tools/check-html.py --dir Resumo_estudos --check

# 2. Build índice de busca + changelog (antes de todo deploy)
python build-search-index.py
python build-changelog.py

# 3. Validação geral (HTML, add-ons, resíduos, freshness)
python tools/validate-all.py

# 4. QA visual (requer servidor na 8765 e Playwright)
node _check-all.js   # recriar: 79 páginas × 1280/390 × claro/escuro + gaveta ☰

# 5. Migração idempotente (deve selecionar 0 arquivos)
python apply-visual-migration.py --wave swap-a --dry-run
python apply-visual-migration.py --wave swap-b --dry-run
python apply-visual-migration.py --wave tokens --dry-run

# 6. Deploy
npx surge ./Resumo_estudos resumos-hermes.surge.sh
```

O script `_check-all.js` foi usado como QA temporário e removido; se precisar de novo, recriar com o teste de gaveta (o bug corrigido em 06/11 era invisível sem ele).

---

## 4. Mapa das alterações deste ciclo

| Grupo | Arquivos | Natureza |
|---|---|---|
| Resumos | 79 (`Resumo_estudos/*/*/resumo-aula-*.html`) | CSS canônico, `#rh-mat`, `#rh-page-extra`, wrap de `code`/`sec-title`, dark `sec-num` |
| Sketchnotes | 28 | a11y (skip link, `#conteudo`, `scope="col"`, menu mobile) — de etapa anterior |
| Index e trilhas | `Resumo_estudos/index.html`, `Resumo_estudos/*/index.html`, `tce-go-trilha.html`, `mudancas.html` | a11y, lazy-load do `search-index.json`, regeneração do changelog |
| Design system | `design-system/css/base.css`, `components/layout.css`, `components/header.css`, `addons/dark-mode.css` | mobile 768, reduced-motion, `code`/`sec-title` wrap, numeral dark `var(--mat)` |
| Template | `template-thin.html`, `Resumo_estudos/templates/template-sumario.html` | regenerados por `build.py design template` |
| Scripts | `apply-a11y.py` (novo), `apply-visual-migration.py` (novo), `audit_visual_migration.py` (novo), `build-changelog.py`, `tools/apply_shared.py` | tooling |
| Docs | `AGENTS.md`, `.opencode/skills/nova-aula/SKILL.md`, este arquivo | regras e mapeamento |

---

## 5. Decisões travadas (não reabrir sem motivo)

1. **Cor da matéria comanda o visual** (`--mat`, `--mat-strong`, `--mat-soft`, `--mat-line`), inclusive no dark.
2. **Li-TCE = slate `#475569`** (light) / `#94a3b8` (dark) — escolha do usuário.
3. **Texto à esquerda** em todos os resumos; `justify` abolido.
4. **Cards flat em coluna única**, faixa lateral de 5 px, radius 14 px, sem hover-lift.
5. **Extras preservados só quando há uso real no corpo**; regra morta e regra que conflita com add-on são descartadas (caso `.dot` e `.aula .sidebar`).
6. **Mobile**: 20 px de padding de seção em ≤768 px; menu ☰ abre gaveta (não `display:none`).
7. **Deploy independente do git** (ADR-005): publicar a cada alteração; commit só no encerramento.
8. **Regra do projeto**: não citar artigo de lei de memória; não remover conteúdo; sugestões de conteúdo só com aprovação.

---

## 6. Armadilhas encontradas (para a próxima sessão)

- **Trocar o CSS e recalcular extras na mesma passada apaga extras**: depois que o bloco #0 vira canônico, o legado não existe mais. O script só reencontra `.destaque` por uma tabela explícita (`DESTAQUE_*`). Se surgir novo utilitário de página, adicioná-lo lá **antes** de rodar `--wave extras`.
- **`rh-addons` é bloco compartilhado** com toolbar/revisão/marcação: não reescrever às cegas; comparar variantes.
- **Regra legada no `@media` pode sobreviver escondida** e só aparecer no celular (foi o caso da gaveta).
- **Rebuild do template muda o CSS canônico**: depois de `build.py design template`, os arquivos já migrados voltam a ser "legados" para o script — é esperado e seguro, mas rodar `swap` de novo.
- **Caminhos no Surge são case- e espaço-sensíveis** (`Aula%2007`, `Direito%20Constitucional`).
- **`git status` deste clone tem filtros de conteúdo**: confirmar com `git ls-files`/`git diff --stat` antes de operações destrutivas.

---

## 7. Ordem sugerida para retomar

1. P1 (data do index) — rápido.
2. P2 (AGENTS.md) — evita retrabalho.
3. P3 (cards inline da AP) — se aprovado, 5 arquivos e republicar.
4. P9 (conferir CI do push).
5. P7 e P4/P5/P6 — só quando houver decisão.
