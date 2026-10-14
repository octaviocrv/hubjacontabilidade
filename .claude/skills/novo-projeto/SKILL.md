---
name: novo-projeto
description: "Use when: criar iniciativa interna, campanha, projeto de marketing ou pedir /novo-projeto."
---

# Novo projeto no hub JA

Cria estrutura local sem repositório e sem fugir das pastas numeradas.

Antes de começar, ler todos os arquivos de `00-contexto/` e `_memoria/`.

## Fluxo

1. Coletar nome, objetivo, tipo de entrega e referências existentes.
2. Propor destino:
   - contexto duradouro: `00-contexto/`;
   - identidade: `01-identidade/`;
   - marketing: `02-marketing/`;
   - edição e IA: `03-edicao-ia/`;
   - código: usar `04-projetos/` somente após decisão explícita;
   - não classificado: `99-arquivo/`.
3. Mostrar árvore proposta e esperar aprovação.
4. Criar somente pastas e arquivos aprovados.
5. Adicionar `briefing.md` quando houver contexto específico suficiente.

## Regras

- Nomes em minúsculo, sem acento, sem espaço e com hífen, salvo arquivo externo que precise manter o nome.
- Não criar repositório Git aninhado. Projetos de código já independentes mantêm seus próprios repositórios.
- Não copiar template genérico de agência/freelancer.
- Dependências podem ser instaladas na raiz do hub após listar o que será instalado; nunca instalar dentro de `04-projetos/`.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Publicação exige OK explícito do Octavio para cada peça.
