---
name: relatorio-ads
description: "Use when: analisar export do Google Ads ou Meta Ads, relatório semanal, performance de campanha ou pedir /relatorio-ads."
---

# Relatório de mídia paga

Analisa arquivos fornecidos ou consulta plataformas configuradas.

## Fluxo

1. Ler contexto e meta da campanha em `_memoria/` e `02-marketing/`.
2. Ler CSV, XLSX, PDF ou print fornecido.
3. Conferir período, moeda, conversões e colunas ausentes.
4. Comparar com período anterior somente quando os dados permitirem.
5. Produzir:
   - resumo executivo;
   - investimento, conversões e CPA;
   - desempenho por canal/campanha;
   - alertas com critério explícito;
   - recomendações concretas;
   - limitações.
6. Mostrar no chat e salvar, se aprovado, em `02-marketing/campanhas/relatorios/<data>-relatorio.md`.

## Regras

- Não inventar número, benchmark ou conversão.
- Não usar limites genéricos do MazyOS como verdade; pedir meta da JA.
- Não recomendar aumento de orçamento sem relacionar custo, conversão e qualidade do lead.
- Pode acessar Google, Meta, API, MCP, e-mail ou navegador autenticado quando necessário.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Publicar ou enviar o relatório exige OK explícito do Octavio.
- Tokens ficam somente em variáveis de ambiente ou `.env` ignorado.
