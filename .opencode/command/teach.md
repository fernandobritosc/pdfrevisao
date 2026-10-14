---
description: Ensina um tema novo com workspace persistente (missão, lições HTML, registros de aprendizado) em ./estudos-teach/.
---
Invoque a skill `teach` e execute o fluxo completo. Pedido do usuário: $ARGUMENTS

Regras fixas deste projeto:
- O workspace de ensino vive em `./estudos-teach/` (raiz do repo) — crie-o se não existir e resolva TODOS os caminhos do workspace (MISSION.md, ./lessons/, ./reference/, ./learning-records/, ./assets/, RESOURCES.md, NOTES.md, GLOSSARY.md) a partir dele, não do cwd.
- Todo material gerado (lições, referências, glossário) em português brasileiro.
