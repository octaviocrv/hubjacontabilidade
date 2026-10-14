---
name: atualizar
description: "Use when: reconciliar o contexto da JA, varrer o hub, atualizar memória ou pedir /atualizar."
---

# Atualizar contexto

Compara documentação e memória com o estado real do hub.

## Fluxo

1. Ler `CLAUDE.md`, todos os arquivos de `00-contexto/` e `_memoria/`.
2. Listar os caminhos relevantes do hub. Ler `04-projetos/` quando necessário para reconciliar fontes de verdade.
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
- Não reformatar arquivos inteiros para mudar uma linha.
- Alterações locais em `04-projetos/` exigem aprovação e seguem o Git próprio de cada projeto; esta skill não executa Git neles.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Publicação exige OK explícito do Octavio para cada peça.
- Segredos ficam somente em variáveis de ambiente ou `.env` ignorado.
