---
name: salvar
description: "Use when: criar commit local no hub, salvar alterações localmente ou pedir /salvar."
---

# Salvar localmente no Git do hub

Cria commit local somente no repositório raiz. Esta skill nunca sincroniza com GitHub.

## Pré-checagem obrigatória

1. Ler todos os arquivos de `00-contexto/` e as regras de `CLAUDE.md`.
2. Confirmar que o diretório Git raiz é o hub e que a branch não é `main`.
3. Se o comando estiver sendo executado dentro de `04-projetos/`, parar imediatamente.
4. Rodar `git status --short` no hub.
5. Confirmar com `git check-ignore` que todos os repositórios de `04-projetos/` continuam ignorados.

## Fluxo

1. Se não houver mudanças, informar e parar.
2. Mostrar arquivos staged e unstaged.
3. Se já houver arquivos staged, commitar apenas esses arquivos.
4. Se nada estiver staged, propor exatamente o que será incluído e pedir aprovação.
5. Verificar segredos, `.env`, tokens, caches e artefatos indevidos.
6. Preparar somente os arquivos aprovados.
7. Confirmar que nenhum caminho de `04-projetos/` entrou.
8. Criar commit no formato:

```text
HUBJA - (tema feito e modificado)
```

9. Incluir o trailer de coautoria configurado para o hub.
10. Mostrar `git status --short` e `git log --oneline -1`.

## Proibições absolutas

- Nunca executar `git push`.
- Nunca criar, adicionar, trocar ou remover remoto.
- Nunca usar `gh repo create` ou outra forma de envio ao GitHub.
- Nunca executar `git init`.
- Nunca executar Git dentro de `04-projetos/`.
- Nunca fazer commit na `main`; parar se a branch atual for `main`.
