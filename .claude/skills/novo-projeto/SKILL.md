---
name: novo-projeto
description: "Use when: criar iniciativa interna, campanha, projeto de marketing ou pedir /novo-projeto."
---

# Novo projeto no hub JA

Cria estrutura local sem repositório e sem fugir das pastas numeradas.

## Fluxo

1. Coletar nome, objetivo, tipo de entrega e referências existentes.
2. Propor destino:
   - contexto duradouro: `00-contexto/`;
   - identidade: `01-identidade/`;
   - marketing: `02-marketing/`;
   - edição e IA: `03-edicao-ia/`;
   - código: não criar dentro do hub sem decisão explícita;
   - não classificado: `99-arquivo/`.
3. Mostrar árvore proposta e esperar aprovação.
4. Criar somente pastas e arquivos aprovados.
5. Adicionar `briefing.md` quando houver contexto específico suficiente.

## Regras

- Nomes em minúsculo, sem acento, sem espaço e com hífen, salvo arquivo externo que precise manter o nome.
- Nunca criar `.git`, remoto, worktree ou projeto dentro de `04-projetos/`.
- Não copiar template genérico de agência/freelancer.
- Não instalar ou executar ferramenta.
