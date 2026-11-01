# Glossário do Domínio — Sistema de Resumos para Concursos

> **Regra**: Use estes termos exatamente. Não substitua por "componente", "serviço", "API", "módulo" (exceto no sentido técnico do codebase-design), "boundary", "feature", "page". A linguagem consistente é o ponto central.

---

## Entidades Principais

### Resumo
**Definição**: HTML final de uma aula, publicado em `Resumo_estudos/<Matéria>/<Aula XX>/resumo-aula-XX-<tema>.html`.
**Propriedades**: tem seções numeradas, sidebar, toolbar, busca, modo revisão, modo marcação, modo prática, PWA.
**Seam**: gerado pelo pipeline de build a partir do template + markdown fonte.

### Aula
**Definição**: Unidade de estudo identificada por número ordinal (ex: "Aula 05") e tema (ex: "Prazos Processuais").
**Propriedades**: pertence a uma Matéria; tem arquivos-fonte (completo, simplificado, resumo, mapa mental, marcação do aprovado); pode ter `quiz.json` (modo prática) e `sketchnote` (resumo visual).
**Exemplos**: "Aula 03 — Prazos Processuais", "Aula 14 — LRF Parte IV".

### Matéria
**Definição**: Disciplina do concurso (ex: "Direito Processual do Trabalho", "AFO", "Administração Pública").
**Propriedades**: tem cor própria (`--mat-<sigla>`); agrupa aulas sequenciais; aparece no index como card e na trilha TCE-GO.
**Siglas canônicas**: AFO, AP, AD, DC, DT, DPT, PT, INF, CP, RML, ARC.

### Seção
**Definição**: Capítulo do resumo, identificado por `id="secN"` (N = 1..5 padrão).
**Estrutura padrão**: 
- `sec1` — Conceito / Introdução
- `sec2` — Classificação / Estrutura  
- `sec3` — Regras / Aspectos técnicos
- `sec4` — Aprendizados das questões (TEC) / Incidência
- `sec5` — Pontos que mais caem em prova
**Regra**: ordem de livro (teoria → estrutura → regras → incidência → prova). Sidebar lista links para cada `secN`.

### Card
**Definição**: Bloco de conteúdo principal do resumo. Visual: flat, coluna única, borda lateral 5px na cor da matéria (`--mat`), sem sombra, hover só muda cor da borda.
**Variantes**: 
- Padrão (conteúdo)
- Com `style="border-color:var(--blue)"` (contraste)
- Com `style="border-color:var(--green)"` (positivo)
**Anatomia**: `.card-title` (Space Grotesk 1.02rem) + `.card-text` (IBM Plex Sans .9rem, line-height 1.65).
**Regra**: cards empilhados (`.card + .card { margin-top: 1rem }`), nunca grid-2/grid-3 no modo aula.

### Callout
**Definição**: Alerta colorido para informação complementar. Quatro tipos semânticos:
- `callout-info` (azul) — informação adicional
- `callout-warn` (âmbar) — atenção / ponto que cai em prova
- `callout-success` (verde) — dica de prova / orientação
- `callout-danger` (vermelho) — erro comum / pegadinha
**Anatomia**: `.callout-icon` (emoji) + `strong` (rótulo) + texto.

### Gotcha
**Definição**: Pegadinha da banca. Visual: fundo rosa claro, borda esquerda 5px vermelha, título `.gotcha-title` (JetBrains Mono .7rem uppercase vermelho).
**Regra**: NÃO usar `.mnemonic` para pegadinhas (preferência do usuário, 23/08/2026). Use `callout-danger` ou `.gotcha`.

### Tag
**Definição**: Badge de incidência TEC. Cores por faixa:
- `tag-red` / `🔴` — alta incidência (contagem ≥ 3)
- `tag-amber` / `🟡` — média incidência (contagem = 2)
- `tag-blue` / `tag-gray` — baixa incidência (contagem = 1)
**Formato**: `<span class="tag tag-red">Tema: N</span>`, uma por linha (`<br>`), agrupadas por faixa.
**Regra**: tags consolidadas por princípio/tema central (ex: "Impessoalidade: 7"), não subdivididas por subtema.

### Incidência (TEC)
**Definição**: Contador de quantas vezes um tema apareceu nas questões coladas do TEC Concursos.
**Agregação**: por seção (ex: "Seção 4 — Barreiras: 5"). Soma todas as tags da seção.
**Uso**: prioriza revisão de seções inteiras, não tags isoladas.

### Trilha
**Definição**: Sequência ordenada de aulas para um edital específico.
**Trilhas atuais**:
- **TJ/TRT** — Mentoria, aulas em andamento (trilha original)
- **TCE-GO** — Autodidata, Trilha Estratégica (Prof. Fábio de Castro Dias), cargo Técnico de Controle Externo - Técnico Administrativo (A01), banca FCC, prova 17/01/2027
**Artefatos**: `tce-go-trilha.html` (painel visual com cards ✅/❌), `tce-go-trilha.md` (tabela markdown), agenda no rodapé do painel.

### Sketchnote
**Definição**: Resumo visual de 1 página por aula (`sketchnote-aula-XX-<tema>.html`).
**Filtro**: só entram temas de **alta e média incidência (TEC)** + **pegadinhas clássicas**. Baixa incidência fica só no resumo.
**Layout**: adaptável por aula (linha evolutiva, confronto de tipos, mapa de funções). Padrão base: nó central escuro + pílulas + faixa evolutiva + blocos + link bidirecional com resumo completo.
**Criação/atualização**: SOMENTE no encerramento da aula (junto do `quiz.json`). Durante a sessão NÃO é editado.

### Quiz
**Definição**: 4–8 questões de recall ativo (pegadinhas/alta incidência), conferidas na fonte.
**Armazenamento**: `quiz.json` na pasta da aula (`questoes[]` com `q`, `opts[]` com `t`, `ok`, `why`).
**Injeção**: modo prática (🎯) vive **DENTRO do resumo** (não workspace à parte). Regra do usuário, 09/10/2026.

---

## Conceitos de Arquitetura (do codebase-design)

### Módulo
Qualquer coisa com interface e implementação. Escala-agnóstica: função, classe, package, ou fatia transversal.

### Interface
Tudo que o chamador precisa saber para usar o módulo corretamente: assinatura de tipos, invariantes, restrições de ordem, modos de erro, configuração requerida, características de performance.

### Implementação
O que está dentro do módulo. Distinto de **Adapter**: algo pode ser adapter pequeno com implementação grande (repo Postgres) ou adapter grande com implementação pequena (fake em memória).

### Profundidade (Depth)
Alavancagem na interface. Quanto comportamento o chamador/teste exerce por unidade de interface que precisa aprender. Módulo **profundo** = interface pequena + muita implementação. Módulo **raso** = interface quase tão complexa quanto implementação.

### Costura (Seam — Michael Feathers)
Lugar onde você pode alterar comportamento sem editar naquele lugar; a *localização* onde a interface do módulo vive. Onde colocar a costura é decisão de design própria, distinta do que vai atrás dela.

### Adapter
Coisa concreta que satisfaz uma interface numa costura. Descreve *papel* (que slot preenche), não substância (o que tem dentro).

### Alavancagem (Leverage)
O que chamadores ganham da profundidade. Mais capacidade por unidade de interface que aprendem. Uma implementação paga de volta em N chamadas e M testes.

### Localidade (Locality)
O que mantenedores ganham da profundidade. Mudança, bugs, conhecimento e verificação concentram em um lugar em vez de espalhar entre chamadores. Corrigiu uma vez, corrigiu em todo lugar.

### Teste da Deleção
Imagine deletar o módulo. Se complexidade desaparece, era pass-through. Se complexidade reaparece em N chamadores, ele estava ganhando seu sustento.

### A Interface é a Superfície de Teste
Chamadores e testes cruzam a mesma costura. Se você quer testar *além* da interface, o módulo provavelmente tem o formato errado.

### Um Adapter = Costura Hipotética. Dois Adapters = Costura Real
Não introduza costura a menos que algo realmente varie através dela.

---

## Termos de Processo

### Pipeline de Build
Sequência: PDF → Markdown (fonte) → Template Thin + Design System → HTML bruto → `apply-review-mode` → `apply-marks-mode` → `apply-search` → `apply-practice-mode` → `apply-pwa` → `check-html` → `build-search-index` → `build-changelog` → Deploy Surge.

### Apply Scripts (Thin Adapters)
Scripts `apply-*.py` que chamam `apply_shared.HtmlInjectionEngine` com config específica (`REV_CONFIG`, `MARKS_CONFIG`, `SEARCH_CONFIG`, `PRACTICE_CONFIG`, `PWA_CONFIG`). Idempotentes por chave (`id="rhRev"`, `data-sr-v="2"`, `<!--rh:practice:start-->`, `rel="manifest"`).

### Design System
Conjunto de tokens + componentes base + addons + módulos JS, construído por `build.py` e injetado no template thin via placeholders `{{CSS}}` `{{JS}}`.

### Template Thin
`template-thin.html` (~200 linhas) com HTML estrutural + placeholders `{{CSS}}` `{{JS}}` + slots de conteúdo (`{{DISCIPLINA}}`, `{{AULA}}`, `{{TEMA}}`, seções).

### Template Final (Gerado)
`Resumo_estudos/templates/template-sumario.html` — template thin + design system concatenado/minificado. Usado pela skill `/nova-aula` para gerar resumos novos.

### Deploy Surge
Publicação **somente da pasta `Resumo_estudos`** em `resumos-hermes.surge.sh`. **NUNCA** publicar a pasta `PDF Revisão` inteira. Deploy a **CADA alteração** (questão TEC, correção, novo resumo), com `build-search-index` + `build-changelog` antes, verificação HTTP 200 depois. Independente do git.

### Migração Obrigatória
Toda aula antiga tocada (correção, questão TEC, revisão, qualquer ajuste) é migrada ao padrão visual atual **na mesma alteração**. Nenhuma aula permanece no padrão antigo após ser editada (regra do usuário, 25/09/2026).