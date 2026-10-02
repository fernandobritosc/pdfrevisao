---
name: sketchnote
description: Gera sketchnote de aula de concurso — página HTML manuscrita (papel quadriculado, contornos tortos, marca-texto) a partir do resumo HTML e dos .md da aula. Use SEMPRE que o usuário pedir sketchnote, mapa visual, resumo visual ou ilustrado de uma aula, mesmo sem a palavra "sketchnote".
---

# Sketchnote de aula (HTML)

## Quando usar

Frases que disparam esta skill: "faça o sketchnote da aula X", "mapa visual da aula",
"resumo visual/ilustrado", "é tipo assim" + HTML de referência. Vale para qualquer
matéria do projeto.

## Template

O padrão visual é o sketchnote da Aula 01 de Direito Administrativo:

`Resumo_estudos/Direito Administrativo/Aula 01/sketchnote-aula-01-estado-governo-adm.html`

**NUNCA gerar PNG/PDF via Pillow** (abordagem antiga, descartada pelo usuário).
Sketchnote é sempre HTML seguindo esse template: copiar o arquivo e adaptar o
conteúdo, mantendo o `<style>`, os símbolos SVG (`#i-*`, `#a-*`), o filtro `#rough`
e as classes (`.box`, `.chip`, `.blob`, `.hl/.hm/.hp/.hb`, `.wav`, `.trap`, `.rule`).

## Design system do template (manter)

- Papel quadriculado claro + dark mode automático + impressão limpa (`@media print`).
- Fontes manuscritas (Google Fonts): Permanent Marker (títulos), Caveat (notas),
  Patrick Hand (corpo). Funcionam online; offline caem para Segoe Print/Comic Sans.
- Caixas com contorno "torto" (border-radius irregular + `filter:url(#rough)`),
  alternando inclinação `.tilt-l`/`.tilt-r`; caixa `.trap` (vermelha, tracejada) para pegadinhas.
- Marca-texto amarelo/verde/rosa/azul (`.hl/.hm/.hp/.hb`), sublinhado ondulado
  vermelho (`.wav`), chips coloridos, divisórias `.squig` entre painéis.
- Ícones: reutilizar os símbolos SVG existentes; só criar símbolo novo se o conceito
  não tiver equivalente.

## Estrutura de conteúdo (seguir)

1. `.hero`: fita `.tape` (matéria + aula), `h1` (tema), `.note` (frase-guia), `.route`
   (chips do roteiro ligados por setas).
2. Painéis numerados (`.panel` + `.ph` + `.pn`): Estado/governo → elementos/estrutura →
   sentidos da Administração → regime jurídico → cai em prova.
3. Recursos didáticos: tabelas de rabisco (`.tw`), pares `A × B` (`.pair` + `.vs`),
   tríades com soma (`.tri` + `.plus` + `.bigres`), regra de ouro (`.rule`),
   checklist (`.check`), alertas (`.warn`), bizu (`.box` + `#i-bulb`).
4. Fechar com `.rule` de dica final + `.src` (fontes do resumo).

## Passos

1. Ler o resumo HTML da aula (títulos dos cards = blocos) e os `.md` da aula.
2. **NUNCA citar artigo, inciso ou parágrafo de lei de memória** — conferir cada
   dispositivo no .md-fonte antes de escrever (regra crítica do AGENTS.md).
3. Copiar o template para
   `Resumo_estudos/<Matéria>/Aula XX/sketchnote-aula-XX-<tema>.html` e adaptar o
   conteúdo, preservando classes e estrutura.
4. Validar balanceamento de tags (script em Temp/opencode) — **zero problemas**.
5. Reportar arquivo + painéis incluídos. **Não commitar nem publicar** sem pedido
   (regra do AGENTS.md: acumular na working tree).
