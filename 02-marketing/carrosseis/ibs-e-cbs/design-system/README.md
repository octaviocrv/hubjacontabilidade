# Design System - Carrosseis JA

Este design system define um padrao visual para manter todos os carrosseis com a mesma identidade da JA.

## 1. DNA visual (nao negociar)

- Estetica premium: fundo escuro + acento dourado.
- Mistura editorial: titulo em serif, texto em sans-serif.
- Bloco de marca fixo no rodape do slide.
- Linha dourada no topo e barra de progresso dourada embaixo.
- Composicao com bastante respiro e contraste alto.

## 2. O que e fixo e o que pode variar

Fixo em todos os carrosseis:
- logo `Logo.jpeg`
- nome `JA Contabilidade`
- linha secundaria `Contabilidade | Pericia | Estrategia`
- paleta principal e tipografia
- proporcao do slide 4:5

Pode variar sem perder identidade:
- fotos e imagens
- copy de titulo e descricao
- ordem de argumentos
- detalhes decorativos leves (faixa, watermark, textura)

## 3. Tokens de cor

| Token | Valor | Uso |
|---|---|---|
| `--ja-bg-canvas` | `#1A1A1A` | fundo da pagina de edicao |
| `--ja-bg-slide` | `#0A0A0A` | fundo base do slide |
| `--ja-accent-500` | `#C8A55C` | destaque principal |
| `--ja-accent-600` | `#A8894A` | gradiente secundario |
| `--ja-text-strong` | `#FFFFFF` | titulos fortes |
| `--ja-text-body` | `#CCCCCC` | texto de corpo |
| `--ja-text-soft` | `#BBBBBB` | subtitulos |
| `--ja-text-muted` | `#888888` | texto secundario |
| `--ja-text-faint` | `#666666` | texto terciario |
| `--ja-line-weak` | `#1E1E1E` | separadores |
| `--ja-line-mid` | `#222222` | bordas de apoio |

## 4. Tipografia

- Serif de destaque: `DM Serif Display`
- Sans de leitura: `DM Sans`

Escala recomendada:
- titulo principal do slide: 30-34px
- titulo secundario: 24-26px
- texto de corpo: 13px
- metadados/labels: 10-12px

## 5. Formato e espacamento

- Formato final Instagram feed: `1080x1350` (4:5)
- Formato de edicao: `432x540` (escala 2.5x)
- Area segura horizontal: 36px
- Area segura superior: 54-60px
- Area segura inferior: 30-36px
- Linha topo: 4px
- Barra inferior: 3px

## 6. Estrutura padrao de slide

1. Top line dourada.
2. Conteudo principal (kicker, titulo, copy).
3. Bloco visual/foto com overlay para legibilidade.
4. Bloco de marca no rodape.
5. Barra de progresso inferior.

## 7. Regras para foto e imagem

- Priorizar foto com contraste medio/alto.
- Aplicar tratamento para manter legibilidade:
  - `filter: grayscale(0.1 a 0.2)`
  - `brightness(0.65 a 0.9)`
- Sempre usar overlay escuro quando houver texto sobre imagem.
- Evitar fundo com muito detalhe atras de paragrafo longo.

## 8. Modelos de conteudo por slide

Slide 1 (Capa):
- promessa principal
- contexto curto
- chamada de continuidade (`ARRASTE ->`)

Slide 2 (Argumentacao):
- titulo de impacto
- lista numerada 01/02/03
- cada item com separador leve quando necessario

Slide 3 (Fechamento/CTA):
- frase de conclusao
- bloco CTA destacado em dourado
- reforco de assinatura da marca

## 9. Variacao sem repeticao visual

Para nao ficar tudo igual:
- alternar foto em destaque (direita, faixa central, fundo total)
- alternar estilo de apoio (numero grande, quote, box)
- alternar ritmo tipografico (titulo mais curto x mais longo)

Sem quebrar a identidade:
- manter paleta base
- manter lockup da marca no rodape
- manter hierarquia serif + sans

## 10. Checklist antes de exportar

- [ ] Titulo legivel no celular
- [ ] Nenhum texto encostando no rodape da marca
- [ ] Foto com contraste suficiente
- [ ] Barra inferior coerente com o progresso
- [ ] Logo com tamanho correto e sem distorcao
- [ ] Saida em `1080x1350` PNG

## 11. Arquivos deste kit

- `tokens.css`: tokens e componentes base
- `template-carrossel.html`: estrutura pronta para novos carrosseis

Uso rapido:
1. Copie `template-carrossel.html`.
2. Troque textos e imagens.
3. Mantenha os blocos de marca.
4. Exporte com `./export`.
