---
description: Processa uma aula completa (PDF → resumo HTML → índice → git → Surge) ou questões TEC coladas.
agent: build
---

Carregue a skill `nova-aula` e execute o procedimento completo descrito nela.

**Uso:** `/nova-aula <Matéria> <número da aula> <tema>` — ex: `/nova-aula "Direito Constitucional" 08 "Organização do Estado"`

$ARGUMENTS

- Se os argumentos vierem com matéria/número/tema: processe essa aula.
- Se vierem vazios: detecte PDFs pendentes em qualquer `<Matéria>/aula NN/` e
  pergunte ao usuário qual processar antes de começar.
- Se o que o usuário colou são questões do TEC (e não uma aula nova): siga a
  seção "Fluxo TEC" da skill em vez do ciclo de aula.