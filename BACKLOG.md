# Backlog — pendências agendadas

Tarefas deferidas para execução futura por agente. Cada item: contexto suficiente
para retomar sem depender da conversa original.

## Item A — Coerência entre resumos (item 5 da lista do usuário)

**Objetivo**: garantir numeração/ordem idênticas das seções finais nos resumos,
facilitando revisão cruzada ("onde estava X? sempre na mesma seção").

**Ação 1 (agendada, barata)**: adicionar à skill `/nova-aula`
(`.opencode/skills/nova-aula/SKILL.md`) um passo de verificação ao gerar cada
resumo: última seção deve ser **"Incidência de temas (TEC)"** e a penúltima
**"Pontos que mais caem em prova"** (padrão atual do template). Se desviar,
reportar antes de prosseguir.

**Ação 2 (opcional, futura)**: normalizar os ~10 resumos legados fora do padrão:
- AFO 02, 03, 04 — terminam com "Questões comentadas"/"Tabela comparativa"
  (AFO 04 ainda tem seção de "Gabarito", que viola a regra do AGENTS.md)
- Administração Pública e Geral 00–05 — terminam com "Questões"
- Português 00 e 01 — sem as seções finais padrão
- Português 02 e 03 — ordem invertida (Incidência na 14ª, Pontos na 15ª)
- AFO 05 (receita consolidado) — usa "Pontos de prova" em vez do padrão

Regra de ouro: **conteúdo extraído dos PDFs sem improvisação** — a normalização
mexe só nas seções finais/estruturais, não no conteúdo.

## Item B (aguardando ideia do usuário) — Incidência TEC agregada por matéria

Modelo já foi prototipado e cancelado (página `incidencia-tec.html` + card no
index). Usuário está desenvolvendo a própria ideia — **não implementar** até ele
trazer; retomar com ele, não sozinho.