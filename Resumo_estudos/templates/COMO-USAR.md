# COMO USAR — Template de Resumos para Concursos

Guia rápido de uso do template consolidado de resumos.

> **Regra oficial**: o `AGENTS.md` (raiz do repositório) é a fonte de verdade.
> Em caso de divergência entre este guia e o AGENTS.md, prevalece o AGENTS.md.

## Arquivo-base

```
Resumo_estudos/templates/template-sumario.html
```

Copie esse arquivo para a pasta da aula antes de editar. **NÃO editar o template original.**

## Estrutura de pastas

```
Resumo_estudos/
├── index.html                        ← índice do site (atualizar a cada nova aula)
├── <Matéria>/
│   └── <Aula XX>/
│       └── resumo-aula-XX-<tema>.html ← resumo final no padrão
└── templates/
    ├── template-sumario.html         ← template base — NÃO EDITAR ESTE
    └── COMO-USAR.md                  ← este guia
```

Exemplos reais:

```
Resumo_estudos/AFO/Aula 05/resumo-aula-05-receita-publica-consolidado.html
Resumo_estudos/Português/Aula 01/resumo-aula-01-....html
```

## Passo a passo para cada aula

1. **Entrada**: usuário coloca a aula em PDF na pasta da matéria.
2. **Conversão**: converter PDF → `.md` (completo) e **excluir o PDF** após conversão.
   - Se já existir o `.md` e sobrar PDF, excluir o PDF.
3. **Copiar o template** para a pasta da aula:

   ```powershell
   $dest = "Resumo_estudos\<Disciplina>\<Aula XX>\resumo-aula-XX-<tema>.html"
   Copy-Item "Resumo_estudos\templates\template-sumario.html" $dest
   ```

4. **Preencher os placeholders** (ver "Estrutura de seções" abaixo):
   - `{{DISCIPLINA}}` → ex: `Português`
   - `{{AULA}}` → ex: `Aula 04`
   - `{{TEMA}}` → ex: `Crase`
   - Títulos das seções na sidebar e no `<section id="secX">`
   - Links da sidebar (`href="#sec1"`, etc.)
   - Conteúdo extraído dos PDFs (sem improvisação)
5. **Questões do TEC**: usuário faz questões no TEC e cola aqui.
   - **NÃO replicar a questão no resumo.**
   - Transformar o aprendizado em conteúdo de estudo (ver formato abaixo).
6. **Atualizar o index.html** (ver modelo de card abaixo).
7. **Publicar** somente a pasta `Resumo_estudos` (ver passo abaixo).
8. **Git (obrigatório a cada aula)**: `git add -A` → commit descritivo → `git push origin main`.

## Estrutura de seções

| Seção | Conteúdo |
|---|---|
| `#sec1` | Conceito / Introdução |
| `#sec2` | Classificação / Estrutura |
| `#sec3` | Regras / Aspectos técnicos |
| `#sec4` | Aprendizados das questões (TEC) / Incidência de temas |
| `#sec5` | Pontos que mais caem em prova |

**Proibido**: seções "Questões comentadas" e "Gabarito final" **não existem** no resumo.
O usuário resolve as questões diretamente no TEC; o resumo guarda apenas o aprendizado.

## Formato de conversão de questão → conteúdo de estudo

Cada questão colada vira um bloco de aprendizado na seção temática correta:

```
📌 Aprendizado    — o que a questão ensina (regra, exceção, distinção)
⚖️ Base legal     — artigo(s) de lei que fundamenta (ex: Lei 14.133/2021, art. 6º, XXIX)
🚨 Pegadinha      — o erro da assertiva / o que a banca adora inverter
```

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
- Temas de alta incidência destacados (ex: `🔴 Alta incidência`) para priorizar a revisão.

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

## Atualizar o index.html

Adicione um card na seção correspondente:

```html
<div class="card" style="border-color:var(--green);">
  <div class="card-header">
    <div class="card-icon">📄</div>
    <div class="card-title" style="color:var(--green);">Aula XX — Tema</div>
  </div>
  <div class="card-text">Descrição curta do conteúdo.</div>
  <div class="card-links">
    <span class="tag tag-green">Disciplina</span>
    <a href="Disciplina/Aula XX/resumo-aula-XX-tema.html">Resumo</a>
  </div>
</div>
```

## Publicar

Publicar **somente a pasta `Resumo_estudos`** (o domínio serve o conteúdo dela):

```powershell
npx surge "PDF Revisão\Resumo_estudos" resumos-hermes.surge.sh
```

- **NUNCA** publicar a pasta `PDF Revisão` inteira.
- Domínio atual: `resumos-hermes.surge.sh` (confirmado no `CNAME`).

## Git (obrigatório a cada aula)

```powershell
git add -A
git commit -m "<mensagem descritiva da aula>"   # ex: "Adiciona resumo Aula 07 - Licitações"
git push origin main
```

- O `.gitignore` já exclui `*.pdf` e `Resumo_estudos.rar` do versionamento.

## Elementos visuais disponíveis

| Elemento | Classe CSS | Uso |
|---|---|---|
| Callout info | `callout callout-info` | Informações adicionais |
| Callout warn | `callout callout-warn` | Atenção / pegadinhas |
| Callout success | `callout callout-success` | Dicas de prova |
| Callout danger | `callout callout-danger` | Erros comuns |
| Mnemônico | `mnemonic` | Macetes e bizus |
| Pegadinha | `gotcha` | Armadilhas da banca |
| Tabela | `table-wrap` + `table` | Classificações, quadros |
| Tag azul | `tag tag-blue` | Categorias / questões |
| Tag verde | `tag tag-green` | Destaques positivos |
| Tag âmbar | `tag tag-amber` | Atenção / incidência média |
| Tag vermelha | `tag tag-red` | Alta incidência / erros |

## Regras de qualidade

- **Sem seções de questões**: NÃO existir "Questões comentadas" nem "Gabarito final".
- **Sem mistura de disciplinas**: um resumo = uma aula de uma disciplina.
- **Conteúdo extraído dos PDFs**: sem improvisação.
- **Estrutura fixa**: seguir o template, não inventar seções novas.
- **Linguagem**: português brasileiro, tom direto e objetivo.
- **Incidência de temas**: registrar contadores a cada questão colada.

## Em caso de dúvida

Consulte o resumo da Aula 05 (exemplo pronto):
```
Resumo_estudos/AFO/Aula 05/resumo-aula-05-receita-publica-consolidado.html
```