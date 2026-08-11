---
name: nova-aula
description: Use para processar uma aula nova de concurso: converter PDFs de aula (Estratégia Concursos/TEC) em .md, excluir os PDFs, gerar o resumo HTML no padrão do template-sumario, atualizar o card do index.html, commitar+pushar e publicar no Surge (resumos-hermes.surge.sh). Também use para transformar questões coladas do TEC em blocos de aprendizado (📌 Aprendizado / ⚖️ Base legal / 🚨 Pegadinha) e incrementar a seção "Incidência de temas (TEC)".
---

# nova-aula — Ciclo completo de aula (conversão → resumo → índice → git → Surge)

Processa UMA aula do início ao fim. Siga os passos na ordem exata. Nada de
improvisar conteúdo: tudo vem dos PDFs convertidos.

## Inputs

- **Matéria** (pasta, ex: `Direito Constitucional`)
- **Número da aula** (ex: `08`)
- **Tema** (ex: `Organização do Estado`)

Se o usuário não fornecer, detecte: procure PDFs em qualquer `<Matéria>/aula NN/`
e pergunte qual processar (tool `question`).

## Fatos operacionais (deste ambiente)

- Raiz do projeto: `C:\Concurso\Resumo_estudos` (é o repo git, branch `main`).
- Python p/ conversão (PyMuPDF/fitz): `C:\Users\fernando.brito\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe`
- Surge: `& "C:\nodejs-portable\npx.cmd" surge ...` com `$env:SURGE_LOGIN="fernandobritosc@gmail.com"`.
  - `--force` NÃO é argumento válido do surge — nunca usar.
- Repo remoto: `https://github.com/fernandobritosc/pdfrevisao.git` (`origin`, branch `main`).
- `.gitignore` já exclui `*.pdf` e `Resumo_estudos.rar`.

## Passo 1 — Detectar PDFs

Listar `PDF Revisão/<Matéria>/aula NN/` (ex: `Direito Constitucional/aula 08/`).
Se houver PDFs: continuar. Se só houver `.md` (já convertidos) e sobrar PDF:
excluir o PDF e pular para o Passo 3. Se não houver nada: avisar o usuário.

## Passo 2 — Converter PDF → Markdown e excluir o PDF

Para cada PDF, extrair todo o texto com PyMuPDF. Padrão do script:

```powershell
& "<python-do-venv>" -c "import fitz, sys; d=fitz.open(sys.argv[1]); print('\n\n'.join(p.get_text() for p in d))" "<caminho-do-pdf>" > "<caminho-do-md>"
```

- Nome-base do `.md`: `aula-NN-<Tema sem acentos/espacos vira hifen? NÃO: manter espaços>`. Padrão existente dos arquivos: `aula-07-Partidos Politicos-completo.md` — ou seja, `aula-NN-<Tema>` com espaços preservados e **sem acentos**, seguido do sufixo.
- Sufixos esperados (detectar no nome do PDF): `completo`, `simplificado`, `mapa mental`, `marcacao do aprovado` (sem acento). Se o PDF não trouxer sufixo, inferir pela ordem/propósito (conteúdo integral ↔ condensado ↔ síntese ↔ marcações).
- **Após cada conversão, excluir o PDF** (regra do AGENTS.md). Conferir que o `.md` ficou legível (ler o começo; se vier lixo/encoding quebrado, re-extrair e sanear).

## Passo 3 — Estudar o padrão antes de escrever

LER antes de gerar o HTML:
1. `Resumo_estudos/templates/template-sumario.html` — estrutura base (sidebar, seções numeradas, cards, callouts, mnemônicos, gotchas, tabelas).
2. O resumo mais recente da MESMA matéria (ex: `Resumo_estudos/Direito Constitucional/Aula 06/resumo-aula-06-direitos-politicos.html`) — para manter CSS, classes (`sec1..sec9`) e ordem de seções idênticos.

## Passo 4 — Gerar o resumo HTML

Arquivo de destino: `Resumo_estudos/<Matéria>/<Aula NN>/resumo-aula-NN-<tema>.html`
(nota: pasta de destino com `Aula NN` capitalizado; título: `Aula NN — <Tema>`).

Conteúdo:
- **Só o que está nos PDFs** (simplificado + mapa mental como fonte principal; completo para conferir detalhes). Sem improvisação.
- Estrutura: 9 seções numeradas. Última seção (`sec9` ou equivalente) = **"Incidência de temas (TEC)"** — se não há questões coladas, usar placeholder: "Nenhuma questão do TEC colada ainda." (usar o bloco com `tag tag-red/tag-amber` quando houver contadores).
- Elementos: cards, callouts, mnemônicos, gotchas, tabelas — no estilo do template.
- pt-BR, tom direto e objetivo.

**PROIBIDO**: seções "Questões comentadas", "Lista de Questões", "Gabarito final" —
o usuário resolve as questões no TEC, o resumo não replica questão.

## Passo 5 — Verificar o HTML

```powershell
Select-String -Path "<arquivo>" -Pattern "Questões comentadas|Gabarito final" -SimpleMatch
```
Deve retornar 0 ocorrências. Se houver, corrigir antes de seguir.

## Passo 6 — Atualizar o índice

Em `Resumo_estudos/index.html`, inserir o card da aula na seção da matéria,
logo após o card da aula anterior, mesmo padrão (borda `var(--green)`, ícone
`📄`, descrição curta com tópicos do conteúdo real, link `Abrir resumo →`):

```html
<div class="card" style="border-color:var(--green);">
  <div class="card-header"><div class="card-icon">📄</div><div class="card-title" style="color:var(--green);">Aula NN — <Tema></div></div>
  <div class="card-text">…tópicos reais…</div>
  <div class="card-links">
    <a href="<Matéria>/<Aula NN>/resumo-aula-NN-<tema>.html">Abrir resumo →</a>
  </div>
</div>
```

## Passo 7 — Git (obrigatório)

```powershell
git add -A
git commit -m "Adiciona resumo Aula NN - <Tema> (<Matéria>)"
git push origin main
```
Confirmar que o push saiu (`origin/main` avançou). NUNCA commitar PDFs
(o `.gitignore` cuida).

## Passo 8 — Publicar no Surge (somente a subpasta)

```powershell
$env:SURGE_LOGIN="fernandobritosc@gmail.com"
& "C:\nodejs-portable\npx.cmd" surge "C:\Concurso\Resumo_estudos\Resumo_estudos" resumos-hermes.surge.sh
```
**NUNCA** publicar a raiz `PDF Revisão` inteira. Depois verificar HTTP 200:

```powershell
$u="https://resumos-hermes.surge.sh/<Matéria>/<Aula NN>/resumo-aula-NN-<tema>.html"
(Invoke-WebRequest $u -Method Head -UseBasicParsing).StatusCode
```
E também o índice (`https://resumos-hermes.surge.sh/` → 200).

## Passo 9 — Relatório

Informar ao usuário onde cada alteração foi feita: arquivo + seção/card +
commit (hash) + confirmação do deploy (URLs com 200).

---

# Fluxo TEC — questão colada vira conteúdo de estudo

Quando o usuário colar questão(ões) do TEC de uma aula já resumida:

1. Identificar o(s) tema(s) da questão e a seção temática correta do resumo.
2. Transformar o aprendizado em bloco de estudo (NÃO replicar a questão):
   - `📌 Aprendizado` — regra/exceção/distinção que a questão ensina
   - `⚖️ Base legal` — artigo(s) (ex: Lei 14.133/2021, art. 6º, XXIX)
   - `🚨 Pegadinha` — o erro da assertiva / o que a banca inverte
3. Tema já coberto? Não reescrever o bloco — só adicionar **detalhe novo**
   (regra, exceção, artigo, pegadinha) se houver.
4. Incrementar o contador do(s) tema(s) na seção **"Incidência de temas (TEC)"**
   do resumo (tags `tag-red` = alta incidência, `tag-amber` = média).
5. Seguir Passos 6–9 (índice só se necessário, git, publicar no Surge).