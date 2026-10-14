---
name: atualizar
description: "Use when: reconciliar o contexto da JA, varrer o hub, atualizar memória ou pedir /atualizar."
---

# Atualizar contexto

Compara documentação e memória com o estado real do hub.

## Fluxo

1. Ler `CLAUDE.md`, `00-contexto/` e `_memoria/`.
2. Listar apenas caminhos do hub; ignorar conteúdo interno de `04-projetos/`, salvo leitura explicitamente solicitada.
3. Comparar:
   - mapa de pastas;
   - serviços, público e posicionamento;
   - identidade e referências aprovadas;
   - prioridades e lacunas `[PREENCHER]`;
   - skills locais disponíveis.
4. Apresentar uma lista numerada de divergências com evidência e mudança proposta.
5. Esperar aprovação explícita antes de editar.
6. Aplicar somente os itens aprovados, preservando citações e mostrando o resumo das alterações.

## Regras

- Nunca preencher lacuna por inferência.
- Nunca apagar informação; marcar obsolescência ou substituir apenas com aprovação.
- Nunca alterar `04-projetos/`, executar scripts, instalar, publicar ou fazer push.
- Não reformatar arquivos inteiros para mudar uma linha.
