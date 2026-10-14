---
name: aprovar-post
description: "Use when: preparar e publicar um post já aprovado no site, Instagram ou Facebook, ou pedir /aprovar-post."
---

# Aprovar e publicar uma peça

Prepara um pacote, mostra a prévia e só publica depois do OK explícito do Octavio para aquele post e para os canais escolhidos.

## Fontes obrigatórias

Ler todos os arquivos de `00-contexto/`, a pasta da peça em `02-marketing/` e a memória operacional.

## Pré-requisitos

- Peça final e legenda em `02-marketing/`.
- Canais desejados informados.
- Para Meta:
  - `META_PAGE_ACCESS_TOKEN`;
  - `META_PAGE_ID`;
  - `META_IG_USER_ID`.
- Para publicação no site: integração de deploy que não use GitHub, caso exista.

Tokens ficam em variáveis de ambiente ou `.env` ignorado. Se qualquer credencial necessária estiver ausente, avisar e parar sem criar valor fictício.

## Preparação

1. Localizar arquivos e validar dimensões, ordem e legenda.
2. Validar que dados, CTA, fontes e sigilo do cliente foram revisados.
3. Montar pacote com:
   - título;
   - canais;
   - quantidade de slides ou arquivo do post;
   - legenda completa;
   - URL ou destino final;
   - operações externas que serão realizadas.
4. Mostrar prévia e perguntar:

> “Confirma a publicação deste post nos canais [lista]?”

O OK vale somente para a peça e os canais exibidos. Alteração posterior exige nova confirmação.

## Site

1. Pode preparar ou copiar arquivos para `04-projetos/landing-page/` após aprovação, sem executar Git nesse repositório.
2. Se houver API/CLI de deploy não vinculada a push no GitHub, mostrar o comando/operação e pedir confirmação antes de executar.
3. Se o único deploy disponível depender de push, parar e entregar o pacote local para publicação manual.
4. Não aguardar deploy que não foi iniciado pela própria integração aprovada.

## Instagram e Facebook

1. Mostrar os endpoints/scripts e variáveis que serão usados.
2. Confirmar o OK do post.
3. Publicar primeiro no canal confirmado pelo Octavio.
4. Registrar IDs e respostas da API sem registrar tokens.
5. Se um canal falhar, parar antes do seguinte e relatar o erro.

## Registro

Salvar um relatório sem segredos em `02-marketing/publicacoes/<data>-<slug>.md`, contendo canais, horário, IDs públicos, resultado e pendências.

## Proibições absolutas

- Nunca executar `git push`.
- Nunca criar ou alterar remotos.
- Nunca usar `gh repo create` ou enviar conteúdo ao GitHub.
- Nunca publicar sem o OK explícito do Octavio para a peça e canais mostrados.
- Nunca registrar tokens, chaves ou conteúdo de `.env`.
