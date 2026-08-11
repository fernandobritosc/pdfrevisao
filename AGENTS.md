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

## Regras de qualidade

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

## Após cada alteração

- Reportar ao usuário **onde** cada alteração foi feita (arquivo + seção + linha quando possível).
- Se houver log de revisão, registrá-lo.
