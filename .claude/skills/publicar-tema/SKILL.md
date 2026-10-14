---
name: publicar-tema
description: "Use when: transformar um tema em artigo, carrossel e legendas com opção posterior de publicação, ou pedir /publicar-tema."
---

# Publicar tema

Orquestra artigo, carrossel e textos sociais. O nome representa o pipeline completo, mas nenhuma publicação ocorre sem o OK explícito do Octavio para a peça e os canais.

## Fontes obrigatórias

1. Ler todos os arquivos de `00-contexto/`.
2. Ler `_memoria/`.
3. Consultar pesquisas existentes em `02-marketing/seo/`.
4. Consultar exemplos aprovados em `02-marketing/`.

## Fluxo

### 1. Tema e evidência

- Confirmar tema, público, objetivo, CTA e prazo.
- Para pesquisa externa, mostrar consultas planejadas antes de usar WebSearch/WebFetch.
- Exigir fonte oficial e data para fatos contábeis, tributários e regulatórios.

### 2. Plano editorial

Apresentar para aprovação:

- tese e título do artigo;
- estrutura de headings;
- texto resumido dos três slides;
- legenda Instagram/Facebook;
- abordagem para LinkedIn;
- CTA e destinos.

### 3. Produção local

Após aprovação, criar:

```text
02-marketing/conteudo/<tema>-<data>/
├── artigo.md
├── fontes.md
├── legenda-instagram-facebook.md
├── texto-linkedin.md
└── carrossel/
```

- O artigo começa marcado como rascunho.
- O carrossel segue a skill `/carrossel` e os padrões da JA.
- Pode usar Playwright, Node e APIs de imagem quando aprovados.
- Dependências são instaladas somente na raiz, depois de listadas.

### 4. Preparação para publicação

1. Mostrar todos os arquivos finais e o resumo por canal.
2. Perguntar se o Octavio quer apenas o pacote local ou iniciar `/aprovar-post`.
3. Se escolher publicar, `/aprovar-post` deve pedir novo OK explícito para aquela peça e os canais.

## Regras

- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Nunca registrar tokens ou chaves; usar variável de ambiente ou `.env` ignorado.
- Nunca publicar apenas porque o pacote foi produzido.
- Alterações locais em `04-projetos/` exigem aprovação específica e não incluem comandos Git.
- O visual da JA prevalece; não usar Inter, laranja ou templates genéricos do MazyOS.
- `criar-pacote-conteudo` permanece como alternativa que termina no pacote local.
