---
name: criar-pacote-conteudo
description: "Use when: transformar tema em artigo, carrossel e legendas, criar pacote de conteúdo ou pedir /criar-pacote-conteudo."
---

# Pacote de conteúdo em rascunho

Adaptação segura da skill `publicar-tema` do MazyOS. O nome foi alterado porque esta skill nunca publica.

## Entregas

- Artigo em Markdown.
- Carrossel de três slides no padrão da JA.
- Legenda para Instagram/Facebook.
- Versão de texto para LinkedIn, quando solicitada.
- Lista de fontes e pontos que exigem validação.

## Fluxo

1. Ler todo `00-contexto/`, `_memoria/` e referências do tema em `02-marketing/`.
2. Confirmar tema, objetivo, público, CTA e fontes disponíveis.
3. Se pesquisa web for necessária, mostrar consultas e pedir aprovação.
4. Produzir primeiro o plano:
   - tese do artigo;
   - headings;
   - texto dos três slides;
   - CTA;
   - direção da legenda.
5. Esperar aprovação.
6. Criar `02-marketing/conteudo/<tema>-<data>/` com:
   - `artigo.md`, marcado claramente como rascunho;
   - `texto-carrossel.md`;
   - `legenda-instagram-facebook.md`;
   - `texto-linkedin.md`, se pedido;
   - `fontes.md`.
7. Se o usuário pedir arte, seguir a skill `/carrossel`; não executar render.

## Regras

- Não escrever dentro de `04-projetos/`.
- Não alterar frontmatter de blog, copiar assets para site ou aguardar deploy.
- Não publicar em site, Instagram, Facebook ou LinkedIn.
- Não chamar `/aprovar-post`, API, script, Node, Playwright ou MCP.
- Não instalar, fazer push ou criar remoto.
- Todo dado contábil/tributário precisa de fonte e data.
