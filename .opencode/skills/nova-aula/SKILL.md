---
name: nova-aula
description: Use para processar uma aula nova de concurso (converter PDF → .md → resumo HTML no padrão atual → índice → deploy) e para transformar questões coladas do TEC em blocos de aprendizado com incremento de incidência. Também use para migração de aulas antigas ao padrão visual atual, criação/atualização de sketchnote e encerramento de aula (commit único + push).
---

# nova-aula — Ciclo completo de aula

Processa UMA aula do início ao fim, em fases. Siga a ordem exata. Nada de
improvisar conteúdo: tudo vem dos PDFs convertidos e da lei-fonte.

## Regra zero — Contrato do projeto

**LEIA o `AGENTS.md` da raiz ANTES de qualquer fase.** Ele é o contrato vivo:
regras de qualidade, formato de conversão de questão, padrão visual travado,
medição de incidência e sketchnote. Em conflito entre este arquivo e o
AGENTS.md, vale o AGENTS.md (mais recente).

---

## Inputs

- **Matéria** (pasta, ex: `Direito Constitucional`)
- **Número da aula** (ex: `08`)
- **Tema** (ex: `Organização do Estado`)

Se o usuário não fornecer, detecte: procure PDFs em qualquer `<Matéria>/aula NN/`
e pergunte qual processar.

---

## Fatos operacionais (deste ambiente)

- Raiz do projeto: `C:\Programação\hermes\PDF Revisão` (é o repo git, branch `main`).
- Python (PyMuPDF/fitz e scripts de build): `C:\Users\uniao\AppData\Local\Programs\Python\Python314\python.exe`
- Validador de HTML: `C:\Users\uniao\AppData\Local\Temp\opencode\check-html.py`
  (uso: `<python> check-html.py <arquivo.html>` → deve imprimir `ERROS: zero` e `ABERTAS: zero`).
- Surge: `& "C:\Program Files\nodejs\npx.cmd" surge ...` com `$env:SURGE_LOGIN="fernandobritosc@gmail.com"`.
  - `--force` NÃO é argumento válido do surge — nunca usar.
- Repo remoto: `https://github.com/fernandobritosc/pdfrevisao.git` (`origin`, branch `main`).
- `.gitignore` já exclui `*.pdf` e `Resumo_estudos.rar`.
- Scripts de build/pós-processamento (raiz do repo):
  - `build-search-index.py` → gera `Resumo_estudos/search-index.json` (rodar ANTES de todo deploy).
  - `build-changelog.py` → gera `Resumo_estudos/mudancas.html` (rodar ANTES de todo deploy).
  - `apply-search.py` → injeta busca por palavra no sidebar de todos os `resumo-aula-*.html`.
  - `apply-review-mode.py` / `apply-marks-mode.py` / `apply-pwa.py` → add-ons (🧠 revisão, 🏷 marcação, PWA offline).
  - Todos idempotentes; rodar após regenerar resumos pelo template.

---

## FASE A — Detectar e converter PDFs

1. Listar `PDF Revisão/<Matéria>/aula NN/` (ex: `Direito Constitucional/aula 08/`).
   - Há PDFs → continuar.
   - Só `.md` já convertidos e sobrou PDF → excluir o PDF e pular para a FASE B.
   - Nada → avisar o usuário.
2. Extrair todo o texto com PyMuPDF:

```powershell
& "<python>" -c "import fitz, sys; d=fitz.open(sys.argv[1]); print('\n\n'.join(p.get_text() for p in d))" "<caminho-do-pdf>" > "<caminho-do-md>"
```

3. Nomeação: `aula-NN-<Tema>` com espaços preservados e **sem acentos**
   (padrão existente, ex: `aula-07-Partidos Politicos-completo.md`), seguido do sufixo.
4. Sufixos esperados (detectar no nome do PDF): `completo`, `simplificado`,
   `mapa mental`, `marcacao do aprovado`. Sem sufixo → inferir pela ordem/propósito.
5. **Após cada conversão, excluir o PDF** (regra do AGENTS.md).
6. Conferir que o `.md` ficou legível (ler o começo; se vier lixo/encoding
   quebrado, re-extrair e sanear).

---

## FASE B — Estudar o padrão antes de escrever

LER, nesta ordem, antes de gerar qualquer HTML:

1. `AGENTS.md` — regras de qualidade e formato (Regra zero).
2. `Resumo_estudos/templates/template-sumario.html` — estrutura base (sidebar,
   seções numeradas, cards, callouts, gotchas, tabelas) + CSS do padrão visual travado.
3. O resumo mais recente da MESMA matéria — para manter CSS, classes (`sec1..sec9`)
   e ordem de seções idênticos.
4. Se a aula tocar dispositivo de lei (`L14133.md`, `CLT.md`, etc. na pasta da aula):
   **NUNCA citar artigo/inciso/parágrafo de memória** — conferir o texto exato no
   arquivo-fonte ANTES de escrever.

---

## FASE C — Gerar o resumo HTML

Arquivo de destino: `Resumo_estudos/<Matéria>/<Aula NN>/resumo-aula-NN-<tema>.html`
(pasta com `Aula NN` capitalizado; título: `Aula NN — <Tema>`).

### Fonte de conteúdo

- **Só o que está nos PDFs**: simplificado + mapa mental como fonte principal;
  completo para conferir detalhes. Sem improvisação.
- Lei citada: sempre validar no arquivo-fonte da lei (FASE B, item 4).

### Estrutura

- Seções numeradas em ordem lógica de estudo ("ordem de livro"): teoria →
  entes/formação → regimes → competências → tema central → vedações/limites →
  incidência TEC por último. Seção inchada ou misturada deve ser dividida;
  fusões óbvias devem ser feitas. Sidebar e numeração acompanham.
- Última seção = **"Incidência de temas (TEC)"** — se não há questões coladas,
  placeholder: "Nenhuma questão do TEC colada ainda."
- Elementos: cards, callouts, pegadinhas, gotchas, tabelas — no estilo do template.
- pt-BR, tom direto e objetivo.

### Critérios de "aula boa" (gate de qualidade da geração)

1. **Cobertura**: todo tema relevante do PDF tem bloco próprio no resumo.
   Nenhum tópico do simplificado/mapa mental pode ficar de fora.
2. **Títulos de card didáticos**: o título explica o porquê ou faz pergunta
   ("Art. 478 CLT — por que não é mais aplicado?", "O que muda na prática?").
   Nunca genérico ("Art. 478 CLT (texto original)").
3. **Linhas com contexto**: toda linha de aprendizado traz regra + contexto
   (porquê/quem/como/consequência) — nunca só a regra seca.
4. **Um → por assunto**: proibido espremer dois assuntos numa mesma linha
   separados por `;` ou `e` — cada um ganha linha `→` própria com contexto.
5. **Verticalização de enumerações**: toda enumeração (I), II), 1), 2), a), b),
   1ª, 2ª, ·)) em linhas verticais próprias iniciadas por `→` com `<br>`.
   Exceção: citações legais e gabaritos.
6. **Negrito em enumerações inline**: quando ficar em linha corrida, termos
   principais em `<strong>`; vale para cabeças de linha (`**Níveis:**`, `**Risco:**`).
7. **Espaçamento**: `<br><br>` entre parágrafos/assuntos dentro de um card-text.
8. **Explicações contextuais**: bloco de lei antiga/revogada traz por que saiu
   do radar antes de listar números.
9. **Sem blocos de macete**: nada de `🧠 Macete` / `.mnemonic` (fundo amarelo).
10. **Acabamento de leitura (regra do usuário, 26/09/2026)**: leitura nunca
    pesada — (a) **negrito no termo-chave** de cada linha `→` (o texto antes do
    travessão, ex.: `→ <strong>Unidade de comando</strong> — ordens de...`);
    (b) **listões com 6+ itens quebram ao meio** com `<br><br>` (respiro em
    grupos); (c) **expressões-chave de prova** em `<span class="highlight">`
    (ex.: "the best way to do", homo economicus, "nada é absoluto, tudo é
    relativo"). Idempotente e aplicado a toda aula nova e toda aula tocada.

### Padrão visual travado (obrigatório em toda aula nova)

- Cor da matéria comanda o visual (`--mat` + derivados `--mat-strong`,
  `--mat-soft`, `--mat-line`). Paleta: AFO `#16A34A`, AP `#0D9488`, AD `#2563EB`,
  DC `#7C3AED`, DT `#D97706`, DPT `#DC2626`, PT `#0891B2`, INF `#3B82F6`.
- Tipografia: Space Grotesk (títulos), IBM Plex Sans (corpo), JetBrains Mono (th/tags).
- Texto sempre alinhado à esquerda (nunca justificado).
- Cards flat, coluna única (nunca `grid-2`/`grid-3`), faixa lateral esquerda 5px.
- Tabelas leves: th em `--mat-soft`, mono uppercase, filete `--mat-line`.
- Emojis só em alertas (⚠️ callouts, 🚨 pegadinhas) — nunca em títulos.
- Respiro: padding `2rem 3rem`, radius 14px; dark mode com overrides da matéria.

### PROIBIDO

- Seções "Questões comentadas", "Lista de Questões", "Gabarito final".
- Replicar questão do TEC no resumo.
- Improvisar conteúdo fora dos PDFs.

---

## FASE D — Validação (gate obrigatório)

1. **HTML balanceado** (zero erros obrigatório):

```powershell
& "<python>" "C:\Users\uniao\AppData\Local\Temp\opencode\check-html.py" "<arquivo.html>"
```

2. **Proibidos ausentes** (0 ocorrências):

```powershell
Select-String -Path "<arquivo>" -Pattern "Questões comentadas","Gabarito final"
```

3. **Checklist visual** (conferir no código):
   - [ ] `--mat` da matéria correta + derivados definidos.
   - [ ] Cards em coluna única, sem `grid-2`/`grid-3`.
   - [ ] Enumerações verticalizadas com `→` (grep por `; ` em enumerações).
   - [ ] `<br><br>` entre assuntos, não `<br>` simples.
   - [ ] Títulos de card explicam o porquê.
4. **Dispositivos legais**: reler cada artigo citado contra o arquivo-fonte da lei.

Falhou qualquer item → corrigir ANTES de seguir.

---

## FASE E — Pós-processamento (após gerar/regenerar resumos)

Rodar os add-ons idempotentes:

```powershell
& "<python>" "C:\Programação\hermes\PDF Revisão\apply-search.py"
& "<python>" "C:\Programação\hermes\PDF Revisão\apply-review-mode.py"
& "<python>" "C:\Programação\hermes\PDF Revisão\apply-marks-mode.py"
& "<python>" "C:\Programação\hermes\PDF Revisão\apply-pwa.py"
```

---

## FASE F — Publicação no Surge (sempre que houver alteração)

Publicar em TODA alteração (novo resumo, questão TEC colada, correção, ajuste).
A publicação **independe do git** — a regra de acumular commits NÃO adia o deploy.
**NUNCA** publicar a raiz `PDF Revisão` inteira — somente `Resumo_estudos`.

```powershell
$env:PYTHONIOENCODING="utf-8"
& "<python>" "C:\Programação\hermes\PDF Revisão\build-search-index.py"
& "<python>" "C:\Programação\hermes\PDF Revisão\build-changelog.py"
$env:SURGE_LOGIN="fernandobritosc@gmail.com"
& "C:\Program Files\nodejs\npx.cmd" surge "C:\Programação\hermes\PDF Revisão\Resumo_estudos" resumos-hermes.surge.sh
```

Verificação HTTP 200 depois:

```powershell
$u="https://resumos-hermes.surge.sh/<Matéria>/<Aula NN>/resumo-aula-NN-<tema>.html"
(Invoke-WebRequest $u -Method Head -UseBasicParsing).StatusCode
# e também: https://resumos-hermes.surge.sh/ → 200
```

---

## FASE G — Encerramento de aula

Quando o usuário encerrar a aula:

1. **Perguntar sempre**: a sessão foi primeira aula (🆕) ou revisão (🔁)?
   Registrar o badge na linha da aula do `Resumo_estudos/index.html`
   (revisão: `<span class="ma-rev">🔁 dd/mm</span>`) e atualizar o campo
   "Última atualização" do header.
2. **Criar o sketchnote da aula**: `Resumo_estudos/<Matéria>/<Aula XX>/sketchnote-aula-XX-<tema>.html`
   - Filtro: só temas de alta/média incidência (TEC) + pegadinhas clássicas.
   - Fundo de papel liso (sem grade); link bidirecional com o resumo no topo e rodapé.
   - Layout adaptável por aula (o padrão AFO Aula 04 é base, não camisa de força).
3. **Commit único de encerramento** (com tudo acumulado na working tree) e push:

```powershell
git add -A
git commit -m "Adiciona resumo Aula NN - <Tema> (<Matéria>)"
git push origin main
```

4. **Relatório final**: arquivo + seção/card de cada alteração + commit (hash) +
   URLs com HTTP 200.

> Durante a aula/revisão NÃO commitar — nem por etapa nem a cada bloco de questões.
> As mudanças ficam acumuladas na working tree até o encerramento.

---

# Fluxo TEC — questão colada vira conteúdo de estudo

Quando o usuário colar questão(ões) do TEC de uma aula já resumida:

## 1. Conferência da aula de destino

Antes de processar, verificar em qual aula o tema pertence — matérias com aulas
sequenciais sobre o mesmo assunto podem ter temas distribuídos entre elas.
Consultar os arquivos-fonte (.md) e os resumos existentes para identificar a
aula correta; não presumir que é a aula em andamento.

## 2. Análise completa (nunca pular direto ao contador)

1. Ler a **resolução inteira** da questão.
2. Extrair o **ponto de aprendizado** (o que a questão ensina).
3. **Comparar** com o que está escrito no resumo.
4. Se tiver qualquer **detalhe novo** (mesmo pequeno), adicionar ao resumo.
5. Só então incrementar o contador de incidência.

- Tema já coberto? **Não reescrever o bloco** — só adicionar o detalhe novo.
- **Trava de evidência**: nunca concluir que um ponto "já está coberto" sem
  citar o trecho exato do resumo (card + linha) que o cobre. Match de grep não
  é cobertura. Sem trecho citável → o ponto é novo e entra no resumo.
- **Imagens da questão** (cdn.tecconcursos.com.br, prints, telas): baixar para
  diretório temporário e abrir/ler ANTES de escrever o aprendizado.

## 3. Formato do bloco

```
📌 Aprendizado    — o que a questão ensina (regra, exceção, distinção)
⚖️ Base legal     — artigo(s) de lei (sempre conferir no arquivo-fonte da lei)
→ ⚠️ Cuidado      — erros comuns de interpretação, como linhas do Aprendizado
```

- **Rótulo único**: `📌 Aprendizado` e `⚖️ Base legal` aparecem **uma única vez
  por bloco** — `📌` só na primeira linha; as seguintes usam apenas o nome do
  assunto (`→ Estabilidade:`, `→ Prazo:`).
- **Sem campo "Pegadinha"**: erros comuns entram como linha própria `→ ⚠️` com
  rótulo variado conforme contexto (`Atenção:`, `Não confundir:`, `Exceção:`,
  `Detalhe:`, `Distinção:`, `Limite:`, `Regra:`, `Para fixar:`) — variar dentro
  do card/seção, sem repetir rótulo em sequência e sem referência a
  questão/prova ("assertiva", "a banca", "enunciado", "alternativa").
- **Foco na assertiva correta**: o bloco registra o aprendizado da alternativa
  **GABARITADA**. Aprendizados das erradas só entram se agregarem detalhe
  objetivo e novo; sem isso, omitir.
- **Sem vínculo com a origem**: nunca referenciar número, banca, órgão, cargo,
  ano ou gabarito da questão.
- **Espaçamento e linhas**: `→` por assunto, `<br><br>` entre parágrafos,
  regra + contexto em toda linha.

## 4. Incidência de temas (TEC)

- Incrementar o contador do(s) tema(s) na seção do resumo.
- Tags centralizadas no princípio/tema central (não subdividir por subtema).
- **Agregada por seção**: cada tag traz o nome da seção e soma as questões dela
  (ex.: `Seção 4 — Barreiras (Robbins + Palo Alto): 5`).
- Formato: agrupado por faixa, decrescente, um tema por linha (`<br>` após cada tag);
  desempate por seção (sec1 → secN). Faixas: **≥3 = `tag-red`**, **=2 = `tag-amber`**,
  **=1 = neutra** (cor sempre normalizada pela contagem atual).

## 5. Migração obrigatória

Aula antiga tocada por questão/correção/ajuste → **migrar ao padrão visual
atual na mesma alteração** (Fase C, "Padrão visual travado"). Nenhuma aula
permanece no padrão antigo após ser editada.

## 6. Publicar sempre (agora, não no encerramento)

Rodar a FASE F completa (build-search-index + build-changelog + deploy + HTTP 200).
Índice (Fase G, item 1) só se necessário; commit/push só no encerramento (Fase G, item 3).

---

# Migração de aulas antigas (avulsa)

Quando o usuário pedir migração direta de uma aula ao padrão atual:

1. FASE B (estudar padrão) → reler resumo antigo → refazer CSS/classes conforme
   o padrão travado, **mantendo todo o conteúdo** (nunca suprimir detalhe).
2. FASE D (validação) → FASE E (pós-processamento) → FASE F (publicar).
3. Commit/push: só se o usuário pedir encerramento.
