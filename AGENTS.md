# AGENTS.md — Sistema de Resumos para Concursos

Guia de trabalho deste projeto. Leia antes de qualquer tarefa.

## Missão

Gerar e manter resumos de estudo para concursos públicos a partir de PDFs de aulas
(Estratégia Concursos, TEC Concursos, etc.), publicados como HTML navegável.

## Estrutura de pastas

```
PDF Revisão/
├── index.html                         ← índice do site
├── AGENTS.md                          ← este arquivo
├── template-resumo.html               ← template antigo (gerado por auto_resumo.py)
├── auto_resumo.py                     ← script legado (não usar para conteúdo)
├── <Matéria>/
│   └── <Aula XX>/
│       ├── aula-XX-<tema>-completo.md        ← conversão integral do PDF
│       ├── aula-XX-<tema>-simplificado.md    ← versão condensada
│       ├── aula-XX-<tema>-resumo.md          ← síntese
│       ├── aula-XX-<tema>-mapa mental.md     ← mapa mental
│       └── aula-XX-<tema>-marcação do aprovado.md
├── Resumo_estudos/                    ← DESTINO dos resumos finais (compartilhável)
│   ├── index.html
│   ├── <Matéria>/
│   │   └── <Aula XX>/
│   │       └── resumo-aula-XX-<tema>.html    ← resumo final no padrão
│   └── templates/
│       ├── template-sumario.html      ← template base do resumo
│       └── COMO-USAR.md
```

## Fluxo de trabalho

**Automação**: o comando `/nova-aula <Matéria> <número> <tema>` (skill local
`.opencode/skills/nova-aula/`) executa o ciclo completo abaixo (conversão,
resumo, índice, git, Surge). Pode ser usado também para transformar questões
TEC coladas em conteúdo de estudo e incrementar a incidência.

1. **Entrada**: usuário coloca a aula em PDF na pasta da matéria.
2. **Conversão**: converter PDF → `.md` (completo) e **excluir o PDF** após conversão.
   - Se já existir o `.md` e sobrar PDF, excluir o PDF.
3. **Resumo**: gerar o resumo final em `Resumo_estudos/<Matéria>/<Aula XX>/resumo-aula-XX-<tema>.html`
   usando o template `template-sumario.html`.
4. **Questões do TEC**: usuário faz questões no TEC Concursos e cola aqui.
   - **NÃO replicar a questão no resumo.**
   - Transformar o aprendizado da questão em **conteúdo de estudo** (ver formato abaixo).
5. **Publicação**: publicar **somente a pasta `Resumo_estudos`** no Surge:
   `npx surge "PDF Revisão\Resumo_estudos" resumos-hermes.surge.sh`
   - **NUNCA** publicar a pasta `PDF Revisão` inteira — o domínio serve o conteúdo de `Resumo_estudos`.
   - **Publicar em TODA alteração** (questão TEC colada, correção, novo resumo),
     com busca (`build-search-index.py`) e changelog (`build-changelog.py`)
     regenerados antes, e verificação HTTP 200 depois.
     A publicação **independe do git**: a regra de acumular commits (item 6)
     NÃO adia o deploy (esclarecimento de 23/08/2026 após deploy esquecido).
6. **Git** no repositório `origin` (`https://github.com/fernandobritosc/pdfrevisao.git`):
   - **NÃO commitar no decorrer da aula ou da revisão** — nem por etapa (conversão,
     resumo, aprendizado TEC) nem a cada bloco de questões. Acumular as mudanças na
     working tree (regra do usuário, 19/08/2026).
   - Commitar e **`git push origin main` SOMENTE quando o usuário encerrar a aula**
     — commit único de encerramento, com as mudanças acumuladas.
   - O `.gitignore` já exclui `*.pdf` e `Resumo_estudos.rar` do versionamento.

## Ambiente opencode (reproduzir em máquina nova)

Este projeto usa **opencode** com a distribuição **GSD-OpenCode** (skills, agentes
e comandos `gsd-*`). Em uma máquina nova, após clonar o repositório, faça:

1. **Instalar o GSD-OpenCode globalmente** (instala skills, agentes, comandos e
   regras em `~/.config/opencode/`):
   `npx gsd-opencode --global`
   - Fonte: https://github.com/rokicool/gsd-opencode (MIT).
   - Para reparametrizar modelos (perfis simple/smart/genius): `/gsd-set-profile`.
2. **Arquivos do projeto que viajam no repositório**:
   - `.opencode/opencode.json` → config local do opencode (schema base).
   - `.opencode/rule/gsd-oc-work-hard.md` → regra "executar, não descrever" (cópia).
   - `.opencode/skills/nova-aula/SKILL.md` + `.opencode/command/nova-aula.md` →
     automação do ciclo de aula (`/nova-aula`), incluindo caminhos de python
     (PyMuPDF) e do CLI do Surge usados neste ambiente.
   - `.opencode/skills/frontend-design/SKILL.md` → design system "caderno de um
     aprovado" (papel/tinta/Archivo+IBM Plex): aplicar em qualquer redesign visual
     dos resumos/index; manter classes HTML e regras do AGENTS.md (verticalização,
     `.card-text + .card-text`, validação check-html.py).
   - `.opencode/skills/canvas-design/SKILL.md` → arte estática (capa/banner do index
     em PNG/PDF) — uso opcional, não afeta o layout dos resumos.
   - **Scripts de build (raiz do repo, rodar com o Python da skill)**:
     - `build-search-index.py` → gera `Resumo_estudos/search-index.json` (busca full-text do index).
     - `build-changelog.py` → gera `Resumo_estudos/mudancas.html` (página "O que mudou", via git log) — rodar **antes de todo deploy** (Passo 8 da skill).
     - `apply-review-mode.py` / `apply-marks-mode.py` / `apply-pwa.py` → injetam os add-ons nos resumos (modo revisão 🧠, marcação 🏷, PWA offline); idempotentes, rodar após regenerar resumos pelo template.
3. **MCP**: nenhum servidor MCP é obrigatório para este projeto. Se o usuário
   configurar algum no futuro, registrar aqui (nome, `type`, `command`).
4. **Restart**: após qualquer mudança em config do opencode, reiniciar o opencode.

## Regras de qualidade

- **Verticalização de enumerações**: toda enumeração de lista (I), II), 1), 2), a),
  b), 1ª, 2ª, 3ª, ·) deve ficar em **linhas verticais próprias** iniciadas por
  `→` com quebra `<br>` em todos os resumos. Exceção: citações legais ("art. 5º,
  II", "(art. 22, § 2º, I)") e gabaritos não são verticalizados. É a regra padrão:
  **aplicar proativamente**, sem o usuário pedir, sempre que identificar
  enumeração em linha corrida em qualquer arquivo do Resumo_estudos.
- **Verificação de dispositivo legal (regra crítica)**: **NUNCA** citar artigo,
  inciso, parágrafo ou alínea de lei de memória — sempre conferir o texto exato
  no arquivo-fonte da lei da pasta da aula (`L14133.md` para a Lei 14.133/2021,
  `CLT.md` para a CLT etc.) ANTES de escrever no resumo. Número de inciso errado
  (ex.: art. 6º, XXII vs XLII) anula a questão em prova — o usuário estuda pelo
  material e falha assim prejudica a preparação. Corrigir imediatamente se o
  usuário apontar divergência com o texto legal.
- **Espaçamento entre parágrafos**: manter o CSS `.card-text + .card-text { margin-top: .65rem; }`
  em todos os resumos (já aplicado globalmente).
- **HTML válido**: após qualquer edição, validar tags com
  `check-all-html.py` (Temp/opencode) — o material deve ter **zero problemas**
  de balanceamento. Bugs pré-existentes de gerador legado (auto_resumo.py:
  `</div>` a mais fechando section) foram corrigidos; não reintroduzir.
- **Sem seções de questões**: NÃO existir seção "Questões comentadas" nem "Gabarito final"
  no resumo. O usuário já resolve as questões no TEC.
- **Conteúdo extraído dos PDFs**: sem improvisação.
- **Linguagem**: português brasileiro, tom direto e objetivo.
- **Estrutura**: seguir o template-sumario; sidebar, seções numeradas, cards, callouts,
  mnemônicos, gotchas, tabelas.

## Formato de conversão de questão → conteúdo de estudo

Cada questão colada vira um bloco de aprendizado no resumo, na seção temática correta:

- **Conferência da aula de destino (regra do usuário, 24/08/2026)**: antes de processar uma questão do TEC, verificar em qual aula o tema pertence — matérias com aulas sequenciais sobre o mesmo assunto (ex.: "Licitações Públicas" Aula 07 e "Lei 14.133/2021 - Parte 2" Aula 08) podem ter temas distribuídos entre elas. Consultar os arquivos-fonte (.md) e os resumos existentes para identificar a aula correta, e não presumir que é a aula em andamento.

```
📌 Aprendizado    — o que a questão ensina (regra, exceção, distinção)
⚖️ Base legal     — artigo(s) de lei que fundamenta (ex: Lei 14.133/2021, art. 6º, XXIX)
→ ⚠️ Cuidado      — erros comuns de interpretação, como linhas dentro do Aprendizado
```

- **Imagens das questões (regra do usuário, 19/08/2026)**: sempre que a questão
  colada tiver imagem (figuras do TEC em cdn.tecconcursos.com.br, prints de suporte
  do Firefox/Mozilla, telas de interface, etc.), baixar a imagem para o diretório
  temporário e abrir/ler o conteúdo ANTES de escrever o aprendizado — costuma haver
  informação relevante (configurações, menus, capturas).
- **NUNCA referenciar a questão no bloco** (nem número, banca, órgão, cargo, ano,
  assertiva ou gabarito) — o conteúdo deve valer por si só, sem vínculo com a
  questão de origem.
- **Separação de assuntos**: dentro de um mesmo bloco (card/callout/gotcha), cada
  assunto ocupa linha própria iniciada por **`→`** (quebra com `<br>`); não criar um
  novo bloco a cada assunto.
- **Espaçamento entre parágrafos/assuntos (regra do usuário, 15/08/2026)**: quando
  houver separação entre parágrafos ou assuntos, usar **`<br><br>`** (dupla quebra)
  entre eles — texto colado (um único `<br>`) dificulta a leitura. Aplicar sempre
  que houver mudança de parágrafo/assunto dentro de um card-text.
- **Rótulo único (regra do usuário, 15/08/2026)**: os rótulos `📌 Aprendizado` e
  `⚖️ Base legal` aparecem **uma única vez por bloco/card** — `📌 Aprendizado` só na
  **primeira linha**; as linhas seguintes usam apenas o nome do assunto (ex.:
  `→ Estabilidade:`, `→ Prazo:`, `→ Acordo:`). NUNCA repetir o rótulo
  `📌 Aprendizado` a cada linha de assunto.
- **Sem campo "Pegadinha" (regra do usuário, 19/08/2026)**: os blocos TEC NÃO têm
  o campo `🚨 Pegadinha`. Erros comuns de interpretação entram como linha própria
  dentro do Aprendizado, iniciada por `→ ⚠️ Cuidado:` — sem usar "assertiva",
  "a banca", "enunciado", "alternativa" ou qualquer referência a questão/prova.
- **Foco na assertiva correta (regra do usuário, 23/08/2026)**: em questões de
  múltiplas afirmativas/alternativas, o bloco principal registra o aprendizado da
  alternativa **GABARITADA** (o que está certo — é ela que orienta a revisão).
  Aprendizados das alternativas erradas só entram se agregarem detalhe objetivo e
  novo (ex.: inversão clássica de conceito); sem isso, omitir — catálogo de erros
  tira o foco do estudo.
- **Sem blocos de macete (regra do usuário, 23/08/2026)**: NÃO criar blocos
  `🧠 Macete` / `.mnemonic` (fundo amarelo) nos resumos. Conteúdo de memorização
  entra como **card normal** (ex.: "Ordem das etapas — iniciais"), sem rótulo de
  macete. Template já atualizado; não reintroduzir o padrão.
- **Sugestões de melhoria (regra do usuário, 24/08/2026)**: sempre que eu
  identificar uma sugestão de **inclusão, alteração ou exclusão** de conteúdo
  (num card, seção, regra, pegadinha, tabela, estrutura) que considerar necessária
  ou benéfica, **NÃO aplicar por conta própria** — perguntar ao usuário antes e
  aguardar a confirmação. Ex.: reorganizar um card que ficou confuso, remover
  informação redundante, simplificar uma enumeração, renomear título. A regra vale
  para qualquer arquivo do projeto (resumos, index, templates, AGENTS.md, scripts),
  exceto correções de erro factual/legal (que seguem o fluxo normal de correção).

### Tema repetido

- Assunto já coberto no resumo? **NÃO reescrever o bloco.**
- MAS sempre checar se há **detalhe novo** (regra, exceção, artigo, pegadinha) que
  complemente o estudo. Se houver, adicionar só o detalhe novo.
- **Análise completa da questão (regra do usuário, 29/08/2026)**: NUNCA pular
  direto pro contador de incidência só porque o tema "já existe". Sempre:
  1. Ler a **resolução inteira** da questão
  2. Extrair o **ponto de aprendizado** (o que a questão ensina)
  3. **Comparar** com o que está escrito no resumo
  4. Se tiver qualquer **detalhe novo** (mesmo pequeno), adicionar ao resumo
  5. Só então incrementar o contador de incidência
  - Motivo: já perdemos vários detalhes (art. 841 §3º desistência, prescrição
    em pluralidade de reclamados, etc.) por assumir que "tema já coberto" significava
    "conteúdo completo".
- **Trava de evidência (regra do usuário, 04/09/2026)**: NUNCA concluir que um
  ponto "já está coberto" sem citar o trecho exato do resumo (card + linha)
  que o cobre. Match de grep não é cobertura — é preciso ler o card. Se não
  há trecho citável, o ponto é novo e entra no resumo.
- **Propor melhorias no AGENTS.md (regra do usuário, 04/09/2026)**: sempre que
  eu sentir dificuldade recorrente (contexto, ambiguidade de regra, etapa que
  vivo pulando, atrito no fluxo), devo **propor proativamente** o ajuste de
  regra — apresentar o texto exato a adicionar/alterar e aplicar após
  confirmação. Não esperar o usuário cobrar; o AGENTS.md é o contrato vivo
  do projeto.
- Registrar o incremento de incidência (ver abaixo).

## Medição de incidência de temas (TEC)

Manter uma seção **"Incidência de temas (TEC)"** no resumo de cada aula (após os
conteúdos, antes do rodapé ou em subseção dedicada).

- Lista temas que mais aparecem nas questões coladas, com contador.
- Cada nova questão colada incrementa o contador do(s) tema(s) correspondente(s).
- Temas de alta incidência devem ser destacados (ex: `🔴 Alta incidência`) e servem
  para o usuário priorizar a revisão.
- **Tags consolidadas por princípio (regra do usuário, 17/08/2026)**: na seção de
  incidência, manter as tags **centralizadas no princípio/tema central** (ex.:
  `Impessoalidade: 7`, `Eficiência: 3`) — **não subdividir** por subtema (evitar
  "Impessoalidade — promoção pessoal", "Impessoalidade — patrimonialismo", etc.).
  Só manter tag própria quando o tema não se encaixar em princípio central
  (ex.: `Lei 9.784/1999 — rol do art. 2º, parágrafo único`).

Formato sugerido:

```html
<div class="card">
  <div class="card-title">📊 Incidência de temas (TEC)</div>
  <div class="card-text">
    <span class="tag tag-red">Impessoalidade: 7</span>
    <span class="tag tag-amber">Eficiência: 3</span>
    ...
  </div>
</div>
```

## Rastreabilidade de revisão (revisão espaçada)

Registro de quais aulas já foram revisadas, no index em `Resumo_estudos/index.html`,
via badge verde na linha da aula:

```html
<span class="ma-rev">🔁 17/08</span>
```

- Quando o usuário diz **"revisei Aula X"** (ou "revisada"), atualizar a data da
  revisão no badge da aula (formato: `🔁 dd/mm`).
- Revisar de novo a mesma aula → apenas atualizar a data (sem contador).
- **Ao encerrar uma aula** (comitar e encerrar sessão), **SEMPRE perguntar** ao
  usuário se a sessão foi **primeira aula** (🆕) ou **revisão** (🔁), e registrar
  no index antes de publicar. Não esperar o usuário cobrar.
- Após marcar: atualizar o campo "Última atualização" no header do index,
  commitar e publicar no Surge (fluxo normal).
- O badge fica na linha da aula, na coluna `ma-rev` (Plex Mono, verde).

## Backlog

Pendências agendadas para execução futura (ver `BACKLOG.md` na raiz): item A =
passo de verificação de seções finais na skill `/nova-aula`; item B (aguardando
ideia do usuário) = incidência TEC agregada por matéria.

## Após cada alteração

- Reportar ao usuário **onde** cada alteração foi feita (arquivo + seção + linha quando possível).
- Se houver log de revisão, registrá-lo.
