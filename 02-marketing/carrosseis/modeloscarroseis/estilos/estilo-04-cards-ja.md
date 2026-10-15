# Estilo 04 — Cards JA (adaptação do Modelo 3)

**Status:** criado em 14/10/2026 a pedido do Octavio: "mesmos textos, estética e imagens do Modelo 3, com as cores da JA". Primeira aplicação: `../../modelo3-temas-contabeis/` (rascunho).
**Referência:** `../Modelo3/` (4 cards; cada imagem do grid é uma página).

## Quando usar

Carrossel "4 dúvidas": quatro temas independentes, um por página, com chamada "LEIA A LEGENDA" e respostas na legenda. Também serve para posts avulsos de capa forte. Bom para conteúdo evergreen entre posts de notícia.

## Composição por card (prancheta 432×540)

| Card | Fundo | Composição |
|---|---|---|
| Escuro A ("regularizar") | `#0A0A0A` + foto de prédio em P&B (`opacity .6`) | Site no topo central; título em caixa com borda dourada fina (raio 7 px), palavra-chave em dourado; botão "LEIA A LEGENDA" com borda; palavra gigante vertical na lateral direita (dourado a 20%); listras douradas no canto inferior esquerdo; assinatura JA centralizada embaixo. |
| Claro A (pessoa) | `#F2F2F2` | Triângulos sobrepostos no canto superior esquerdo (preto 8–13% e dourado 28%); ícone chevron em círculo; título DM Sans 700 com palavra em **DM Serif itálico sobre marca-texto dourado**; subtítulo 15 px; botão; pessoa recortada à direita (sem fundo); assinatura JA à esquerda. |
| Claro B (animal/objeto + alerta) | `#F2F2F2` | Igual ao Claro A, com foto à direita fundida por máscara em degradê e triângulos de alerta dourados com "!" (canto superior direito e inferior esquerdo). |
| Escuro B (pergunta) | radial `#171717` → `#0A0A0A` | Site no topo; assinatura JA centralizada acima do título; título em caixa com borda dourada (linha 1 regular, linha 2 em 700 com palavra dourada); balões "?" dourados 3D; moedas recortadas no canto inferior direito; listras no canto inferior esquerdo. |

## Mapeamento de cores (Modelo 3 → JA)

| Modelo 3 | JA |
|---|---|
| Azul-marinho `#0b1737` | `#0A0A0A` / `#171717` |
| Mostarda `#cd8d03` | Dourado `#C8A55C` / `#A8894A` |
| Cinza-claro `#f2f2f2` | `#F2F2F2` (exceção aprovada para este estilo) com texto `#1A1A1A` |
| Balões "?" azuis | Balões dourados em degradê |
| Logo da outra marca | Logo JA + "JA Contabilidade" + "Contabilidade \| Perícia \| Estratégia" |
| "www.seusite.com.br" | `www.jacontabilidadeepericias.com.br` |

## Tipografia

- Títulos: DM Sans 600/700 (aproxima a Open Sauce do modelo).
- Palavra destacada em marca-texto: DM Serif Display itálico (assinatura editorial da JA).
- Botões, site e assinatura: DM Sans.

## Elementos fixos JA

Linha dourada de 4 px no topo e barra de 3 px embaixo; assinatura completa em todos os cards.

## Imagens

- Equivalentes do Pexels, não extraídas da referência.
- Recorte de fundo local com ImageMagick: floodfill com `-fuzz` de 14% (pessoa em fundo de estúdio) a 32% (moedas em fundo branco), depois `-morphology Erode Disk:1.5` no canal alfa para tirar a borda.
- Animal/objeto com fundo complexo: máscara em degradê (`mask-image: linear-gradient(90deg, transparent, #000 34%)`).
- Blocos com texto em inglês ("TAX") foram omitidos.
