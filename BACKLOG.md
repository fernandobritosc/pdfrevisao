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

## Item C — Revisão dirigida pelas incidências 🔴 (antes da próxima leva de questões)

**Registro de 14/08/2026 (encerramento da Aula 07 DA)**: antes de processar a
próxima leva de questões TEC, o usuário deve bater/revisar os 5 temas de maior
incidência da Aula 07 DA (cobrem ~40% da taxa de repetição do TEC):

1. Serviços com dedicação exclusiva de mão de obra (3x)
2. Matriz de riscos — arts. 22 e 103 (3x)
3. Pregão e serviços comuns de engenharia (2x)
4. Linhas de defesa/controle — arts. 169-171 (2x)
5. Revogação e anulação do certame — art. 71 (2x)

**Ação**: ao iniciar nova sessão de questões TEC de Licitações, mencionar ao
usuário a revisão desses 5 pontos antes das questões (estão marcados 🔴/🟠 na
seção "Incidência de temas (TEC)" do resumo).

## Item D — Metas de estudo do usuário (registro em 14/08/2026 · atualizado em 15/08/2026)

Acompanhamento das metas abertas e atrasadas do plano do usuário:

| Nº | Disciplina | Formato | Descrição | Status |
|----|-----------|---------|-----------|--------|
| 2 | Português | Teórico e Exercícios | Sintaxe: termos da oração | Aberta |
| 4 | Administração Pública | Exercícios | Direção. Liderança | ✅ Concluída em 15/08/2026 (aula encerrada; levas TEC processadas; incidências 🔴 registradas na Seção 12 do resumo) |
| 7 | Direito Processual do Trabalho | Exercícios | Prazos processuais | Aberta |

**Ação**: cobrar/progredir as metas abertas nas próximas sessões; oferecer suporte
conforme a disciplina (ex.: Português e AP têm material no repositório; DPT
não tem material ainda).