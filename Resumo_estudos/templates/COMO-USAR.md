# COMO USAR — Template Consolidado de Resumos

Este é o guia rápido para usar o template unificado nos dois computadores.

## Arquivo-base

```
PDF Revisão/templates/template-sumario.html
```

Copie esse arquivo para a pasta da aula antes de editar.

## Estrutura de pastas

```
PDF Revisão/
├── index.html                        ← índice do site (atualizar a cada nova aula)
├── templates/
│   └── template-sumario.html         ← template base — NÃO EDITAR ESTE
├── AFO/
│   └── Aula 05/
│       └── resumo-aula-05-receita-publica.html
├── Português/
│   ├── Aula 00/
│   │   └── resumo-aula-00-ortografia.html
│   ├── Aula 01/
│   │   └── resumo-aula-01-classes-palavras.html
│   ├── Aula 02/
│   │   └── resumo-aula-02-preposicoes-conjuncoes.html
│   └── Aula 03/
│       └── resumo-aula-03-pronomes-colocacao.html
...
```

## Passo a passo para cada aula

### 1. Copiar o template

```powershell
$dest = "C:\Users\fernando.brito\resumos-hermes.surge.sh\PDF Revisão\<Disciplina>\<Aula>\resumo-aula-XX-<tema>.html"
Copy-Item "C:\Users\fernando.brito\resumos-hermes.surge.sh\PDF Revisão\templates\template-sumario.html" $dest
```

### 2. Preencher os placeholders

Abra o arquivo e substitua:
- `{{DISCIPLINA}}` → ex: `Português`
- `{{AULA}}` → ex: `Aula 04`
- `{{TEMA}}` → ex: `Crase`
- Títulos das seções na sidebar e no `<section id="secX">`
- Links da sidebar (`href="#sec1"`, etc.)
- Conteúdo extraído dos PDFs

### 3. Estrutura mínima de seções

| Seção | Conteúdo |
|---|---|
| `#sec1` | Conceito / Introdução |
| `#sec2` | Classificação / Estrutura |
| `#sec3` | Regras / Aspectos técnicos |
| `#sec4` | Questões comentadas |
| `#sec5` | Gabarito final |
| `#sec6` | Pontos que mais caem em prova |

### 4. Atualizar o index.html

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

### 5. Publicar

```powershell
cd C:/Users/fernando.brito/resumos-hermes.surge.sh
npx surge . concurso-fernando.surge.sh
```

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
| Tag azul | `tag tag-blue` | Questões / categorias |
| Tag verde | `tag tag-green` | Gabaritos corretos |
| Tag âmbar | `tag tag-amber` | Gabaritos alternativos |
| Tag vermelha | `tag tag-red` | Gabaritos incorretos |

## Regras de qualidade

- **Sem mistura de disciplinas**: um resumo = uma disciplina
- **Conteúdo extraído dos PDFs**: sem improvisação
- **Questões comentadas**: todas as questões do material, com gabarito final
- **Estrutura fixa**: seguir o template, não inventar seções novas
- **Linguagem**: português brasileiro, tom direto e objetivo

## Em caso de dúvida

Consulte o resumo da Aula 05 (v5.0) como exemplo pronto:
```
PDF Revisão/AFO/Aula 05/resumo-aula-05-receita-publica.html
```
