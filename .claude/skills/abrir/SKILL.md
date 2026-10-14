---
name: abrir
description: "Use when: iniciar uma sessão, abrir o hub JA, começar o dia ou pedir /abrir."
---

# Abrir o hub JA

Carrega o contexto sem alterar arquivos.

## Fluxo

1. Ler `CLAUDE.md`.
2. Ler todos os arquivos Markdown de `00-contexto/`.
3. Ler `_memoria/empresa.md`, `_memoria/preferencias.md` e `_memoria/estrategia.md`.
4. Informar em até seis linhas:
   - identidade da JA em uma frase;
   - prioridade atual;
   - tom e regra visual central;
   - lacunas `[PREENCHER]` relevantes para a próxima tarefa.
5. Encerrar com “Pronto. O que vamos criar ou analisar?”.

## Regras

- Não listar cada arquivo lido.
- `00-contexto/` prevalece se a memória estiver divergente.
- Não sugerir `/instalar`.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Publicação exige OK explícito do Octavio para cada peça.
- Segredos ficam somente em variáveis de ambiente ou `.env` ignorado.
