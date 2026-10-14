---
name: analisar-dados
description: "Use when: analisar CSV, XLSX, JSON, TXT, PDF, métricas, relatório ou pedir /analisar-dados."
---

# Analisar dados

Produz análise executiva baseada somente no arquivo fornecido.

## Antes de começar

1. Ler `00-contexto/marca.md`, `00-contexto/tom-de-voz.md` e `_memoria/empresa.md`.
2. Confirmar o que o arquivo representa e qual pergunta deve responder, se isso não estiver claro.
3. Para dados contábeis ou de cliente, sinalizar riscos de confidencialidade antes de reproduzir identificadores.

## Análise

- Validar colunas, período, unidade e dados ausentes.
- Separar fatos, cálculos e interpretação.
- Mostrar tendências, comparações, anomalias e limitações.
- Nunca inventar benchmark, média de mercado ou dado ausente.

## Entrega

```markdown
# Análise — [arquivo]

## Resumo executivo
## O que está funcionando
## O que merece atenção
## Números-chave
## Recomendações
## Limitações dos dados
```

Apresentar primeiro no chat. Salvar somente se o usuário pedir e no destino que ele aprovar.

## Segurança

- Não enviar dados para API externa.
- Não executar scripts, macros ou conteúdo incorporado no arquivo.
- Não publicar, instalar ou usar Git.
