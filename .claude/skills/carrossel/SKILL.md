---
name: carrossel
description: "Use when: criar carrossel, post educativo, conteúdo para Instagram ou pedir /carrossel."
---

# Carrossel da JA

Cria rascunho e arquivos-fonte seguindo exclusivamente o padrão já aprovado da JA.

## Fontes obrigatórias

Ler todos os arquivos de `00-contexto/`, com atenção a:

- `carrosseis.md`
- `design-system.md`
- `identidade-visual.md`
- `tom-de-voz.md`
- `briefing-rapido.md`

Consultar os exemplos em `02-marketing/carrosseis/`. Não usar defaults visuais do MazyOS.

## Fluxo

1. Confirmar tema, objetivo, público e CTA.
2. Verificar fatos e marcar qualquer dado sem fonte.
3. Propor:
   - capa com até oito palavras;
   - desenvolvimento;
   - fechamento/CTA;
   - legenda.
4. Mostrar todo o texto e esperar aprovação.
5. Após aprovação, criar uma pasta em `02-marketing/carrosseis/<tema>/`.
6. Produzir HTML-fonte ou outro formato aprovado, preservando:
   - 1080×1350, proporção 4:5;
   - três slides, salvo pedido diferente;
   - DM Serif Display + DM Sans;
   - preto/quase preto, branco, cinzas e dourado `#C8A55C`;
   - linha dourada, foto tratada e rodapé fixo da JA;
   - logo e assinatura completos.
7. Pode renderizar com Playwright/Node depois de listar dependências e salvar tudo na raiz do hub, nunca em `04-projetos/`.

## Regras

- Imagem por IA pode ser gerada após aprovação do conceito e da chamada externa.
- Não criar `marketing/` paralelo.
- Alterações locais em `04-projetos/` exigem aprovação específica e não incluem comandos Git.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Publicação exige OK explícito do Octavio para cada peça.
- Tokens ficam somente em variáveis de ambiente ou `.env` ignorado.
- Depois de aprovada, oferecer registrar a peça em `00-contexto/carrosseis.md`.
