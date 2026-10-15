---
name: carrossel
description: "Use when: criar carrossel, post educativo, conteúdo para Instagram ou pedir /carrossel."
---

# Carrossel da JA

Cria rascunho e arquivos-fonte seguindo exclusivamente o padrão já aprovado da JA.

## REGRA INVIOLÁVEL: aprovação do roteiro

Depois de escrever o roteiro/texto dos slides, **PARAR e esperar a aprovação explícita do Octavio**. Proibido, em qualquer circunstância (inclusive modo autônomo, ausência dele ou "continue trabalhando"): gerar HTML, imagens ou PNGs, baixar fotos ou registrar o post como feito antes dessa aprovação. Silêncio não é aprovação. Se o Octavio pedir mudanças, ajustar o roteiro e pedir aprovação de novo. Só salvar o `roteiro.md`.

## Fontes obrigatórias

Ler todos os arquivos de `00-contexto/`, com atenção a:

- `carrosseis.md`
- `design-system.md`
- `identidade-visual.md`
- `tom-de-voz.md`
- `briefing-rapido.md`

Consultar os exemplos em `02-marketing/carrosseis/` e **listar sempre a pasta `02-marketing/carrosseis/modeloscarroseis/` inteira**: o Octavio adiciona modelos novos ao longo do tempo; abrir os novos e usá-los/combiná-los (ver `00-contexto/design-system.md`, seção "Biblioteca de modelos"), sem repetir o estilo do último post. Não usar defaults visuais do MazyOS.

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
   - fontes Inter, Poppins, Creato Display e Montserrat (variar o peso; DM Serif/DM Sans só no estilo clássico já publicado);
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
