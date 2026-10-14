---
name: instalar
description: "Use when: revisar ou completar a configuração do hub JA, configurar o MazyOS ou pedir /instalar."
---

# Revisar configuração do MazyOS na JA

Esta skill não faz instalação inicial destrutiva. Ela revisa a configuração existente e complementa somente o que o Octavio aprovar.

## Fontes obrigatórias

1. Ler todos os arquivos de `00-contexto/`.
2. Ler `CLAUDE.md`, `README.md`, `_memoria/` e `01-identidade/`.
3. Listar as skills em `.claude/skills/`.

## Diagnóstico

Comparar:

- fatos de `_memoria/` com `00-contexto/`;
- regras do `CLAUDE.md` com o estado do hub;
- identidade canônica com `01-identidade/`;
- dependências requeridas pelas skills com as disponíveis na raiz;
- lacunas `[PREENCHER]`.

Apresentar:

```text
Configurado:
- ...

Incompleto:
- ...

Proposta:
- arquivo → adição ou ajuste
- dependência → motivo, pacote e local
```

## Aplicação

1. Esperar o OK do Octavio sobre cada grupo de mudanças.
2. Editar cirurgicamente; nunca sobrescrever arquivos completos.
3. Nunca substituir ou apagar `CLAUDE.md`, `00-contexto/` ou `01-identidade/`.
4. Antes de instalar dependências, listar nome, versão ou faixa, finalidade, arquivos que serão criados e comando.
5. Instalar somente na raiz do hub, nunca dentro de `04-projetos/`.
6. Registrar dependências em manifesto apropriado na raiz quando necessário.

## Segurança

- Nunca fazer push, criar remoto, trocar remoto, usar `gh repo create` ou enviar conteúdo ao GitHub.
- Nunca copiar token ou chave para arquivo rastreado.
- Segredos ficam somente em variáveis de ambiente ou `.env` ignorado.
- Não executar outra skill automaticamente ao terminar.
