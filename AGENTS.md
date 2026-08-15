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
6. **Git** no repositório `origin` (`https://github.com/fernandobritosc/pdfrevisao.git`):
   - Commitar a cada etapa concluída (conversão, resumo, aprendizado TEC).
   - **`git push origin main` SOMENTE quando o usuário encerrar a aula** — não pushar
     por bloco/etapa. Acumular commits localmente até o encerramento.
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

```
📌 Aprendizado    — o que a questão ensina (regra, exceção, distinção)
⚖️ Base legal     — artigo(s) de lei que fundamenta (ex: Lei 14.133/2021, art. 6º, XXIX)
🚨 Pegadinha      — o erro da assertiva / o que a banca adora inverter
```

- **NUNCA referenciar a questão no bloco** (nem número, banca, órgão, cargo ou ano) —
  o conteúdo deve valer por si só, sem vínculo com a questão de origem.
- **Separação de assuntos**: dentro de um mesmo bloco (card/callout/gotcha), cada
  assunto ocupa linha própria iniciada por **`→`** (quebra com `<br>`); não criar um
  novo bloco a cada assunto.
- **Rótulo único (regra do usuário, 15/08/2026)**: os rótulos `📌 Aprendizado`,
  `⚖️ Base legal` e `🚨 Pegadinha` aparecem **uma única vez por bloco/card** —
  `📌 Aprendizado` só na **primeira linha**; as linhas seguintes usam apenas o nome
  do assunto (ex.: `→ Estabilidade:`, `→ Prazo:`, `→ Acordo:`). NUNCA repetir o
  rótulo `📌 Aprendizado` a cada linha de assunto.

### Tema repetido

- Assunto já coberto no resumo? **NÃO reescrever o bloco.**
- MAS sempre checar se há **detalhe novo** (regra, exceção, artigo, pegadinha) que
  complemente o estudo. Se houver, adicionar só o detalhe novo.
- Registrar o incremento de incidência (ver abaixo).

## Medição de incidência de temas (TEC)

Manter uma seção **"Incidência de temas (TEC)"** no resumo de cada aula (após os
conteúdos, antes do rodapé ou em subseção dedicada).

- Lista temas que mais aparecem nas questões coladas, com contador.
- Cada nova questão colada incrementa o contador do(s) tema(s) correspondente(s).
- Temas de alta incidência devem ser destacados (ex: `🔴 Alta incidência`) e servem
  para o usuário priorizar a revisão.

Formato sugerido:

```html
<div class="card">
  <div class="card-title">📊 Incidência de temas (TEC)</div>
  <div class="card-text">
    <span class="tag tag-red">Pregão eletrônico: 5</span>
    <span class="tag tag-amber">Contratação direta: 3</span>
    ...
  </div>
</div>
```

## Rastreabilidade de revisão (revisão espaçada)

Registro de quais aulas já foram revisadas, direto no card da aula em
`Resumo_estudos/index.html`, via tag verde:

```html
<span class="card-tag">🔁 revisada em 11/08/2026 · 2ª revisão</span>
```

- Quando o usuário diz **"revisei Aula X"** (ou "revisada"), atualizar o card da
  aula no index: data da revisão (horário de Brasília) + contador de revisões
  (`1ª`, `2ª`, `3ª`...).
- Revisar de novo a mesma aula → atualizar a data e **incrementar** o contador.
- Após marcar: atualizar o campo "Última atualização" no header do index,
  commitar e publicar no Surge (fluxo normal).
- A classe `card-tag` já existe no CSS do index (verde) — basta inserir o span
  no `card-meta`/`card-links` do card.

## Backlog

Pendências agendadas para execução futura (ver `BACKLOG.md` na raiz): item A =
passo de verificação de seções finais na skill `/nova-aula`; item B (aguardando
ideia do usuário) = incidência TEC agregada por matéria.

## Após cada alteração

- Reportar ao usuário **onde** cada alteração foi feita (arquivo + seção + linha quando possível).
- Se houver log de revisão, registrá-lo.
