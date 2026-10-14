---
name: mapear-rotinas
description: "Use when: mapear tarefas repetitivas, propor automações locais, criar skills ou pedir /mapear-rotinas."
---

# Mapear rotinas da JA

Antes de começar, ler todos os arquivos de `00-contexto/` e `_memoria/`.

## Descoberta

Perguntar, uma por vez:

1. Quais tarefas se repetem?
2. Qual é a entrada real de cada uma?
3. Qual entrega é esperada?
4. O que sempre exige aprovação humana?

## Proposta

1. Verificar se `.claude/skills/` já cobre a tarefa.
2. Propor no máximo cinco skills com nome, gatilho, entrada, saída, destino e riscos.
3. Identificar dependências externas e listar o que será instalado ou configurado antes da ação.
4. Esperar aprovação explícita.

## Criação

- Criar apenas skills aprovadas em `.claude/skills/<nome>/SKILL.md`.
- Incluir descrição com gatilhos claros.
- Herdar todas as regras de `CLAUDE.md`.
- Usar caminhos numerados existentes.
- Exigir aprovação antes de entrega final ou mudança persistente.

## Proibições

- Não criar skill que faça push, crie remoto ou envie conteúdo ao GitHub.
- Skills que publiquem devem exigir OK explícito do Octavio para cada peça.
- MCPs, dependências e `.env` podem ser configurados após explicar a mudança; tokens nunca entram no repositório.
- Não executar a skill recém-criada como parte da criação.
