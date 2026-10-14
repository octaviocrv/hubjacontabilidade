---
name: anuncio-google
description: "Use when: estruturar campanha Search, anúncios Google, palavras-chave, CSV para Google Ads ou pedir /anuncio-google."
---

# Rascunho de campanha Google Ads

Gera planejamento e CSVs para revisão. Pode importar ou ativar somente após OK explícito do Octavio para a campanha.

## Dependências

- Ler todos os arquivos de `00-contexto/` antes de começar.
- `00-contexto/marca.md`
- `00-contexto/tom-de-voz.md`
- `_memoria/empresa.md`
- Pesquisa em `02-marketing/seo/`, se existir

## Briefing

Confirmar:

1. Serviço.
2. Público e região.
3. Objetivo da conversão.
4. Orçamento diário.
5. Landing de destino.
6. Restrições regulatórias e promessas proibidas.

## Entrega

Propor antes de criar:

- campanhas e grupos;
- palavras-chave e negativas;
- anúncios responsivos;
- extensões;
- conversões a configurar;
- checklist de revisão.

Após aprovação, salvar em `02-marketing/campanhas/google-ads-<data>/`. Todo item deve começar com status **pausado**.

## Pesquisa externa

Mostrar termos de pesquisa e pedir aprovação antes de WebSearch. Não inventar CPC, volume ou concorrência.

## Regras

- Pode acessar conta, painel, API, MCP, Google Ads Editor ou Tag Manager quando configurados.
- Antes de importar ou ativar, mostrar resumo final e pedir OK explícito.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Tokens ficam somente em variáveis de ambiente ou `.env` ignorado.
- Não usar superlativo ou economia garantida sem prova.
