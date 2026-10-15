# Biblioteca de modelos de carrossel — JA

Esta pasta guarda:

1. **Referências externas** (`Modelo2/`, `Modelo3/`, `Modelo 4/`, `Modelo 5/`, `Modelo-Story-Telling/`): prints de carrosséis de outros perfis. Servem só para estudar composição e narrativa. Nunca copiar texto, cor, logo ou arte.
2. **Estilos JA** (`estilos/`): composições próprias da JA, criadas a partir das referências e sempre com a identidade fixa da marca.
3. **Registro de uso** (`registro-de-uso.md`): qual estilo cada post usou, para nunca repetir o mesmo estilo em dois posts seguidos.

Decisão do Octavio, 14/10/2026: carrosséis de notícia podem variar composição, fundo, imagens e quantidade de slides; cores, fontes e tom da JA são fixos.

## Identidade fixa (vale para todo estilo)

- Cores: `#0A0A0A` (base), `#111111`/`#0D0D0D` (apoio escuro), dourado `#C8A55C` e `#A8894A`, branco `#FFFFFF`, cinzas `#CCCCCC`, `#BBBBBB`, `#888888`, `#666666` e linhas `#1E1E1E`/`#222222`/`#2A2A2A`. Nada de vermelho, azul, bege ou outra cor das referências.
- Fundo claro só como **elemento** (cartão-papel, faixa) dentro de slide escuro, com texto `#1A1A1A`. A base do carrossel continua escura (`00-contexto/identidade-visual.md`).
- Fontes: DM Serif Display (títulos, números grandes) e DM Sans (corpo, labels, botões).
- Marca: logo circular `Logo.jpeg` + "JA Contabilidade" + "Contabilidade | Perícia | Estratégia" em todo slide. Nunca só `@usuario`.
- Formato: 1080×1350 (prancheta 432×540, exportação 2,5×). Linha dourada de 4 px no topo e barra de 3 px embaixo.
- Tom: `00-contexto/tom-de-voz.md`. Sem promessa de resultado, sem alarmismo, sem juridiquês.

Fontes: `00-contexto/design-system.md`, `00-contexto/carrosseis.md`, `00-contexto/referencias/guia-padrao-carrosseis-ja.md`.

## O que aproveitar de cada referência

| Referência | Aproveitar | Não usar |
|---|---|---|
| **Modelo 2** (5 slides) | Alternância de ritmo entre slides (escuro, cor, papel claro, círculo recortado); palavra-título enorme e condensada com subtítulo menor; objeto recortado (clipe, relógio) invadindo o texto; cartão-papel com lista; CTA "salve este post / chame na DM com palavra". | Vermelho e bege; fonte condensada (substituir por DM Serif em tamanho grande); `@` como única assinatura. |
| **Modelo 3** (capas) | Capa com pessoa recortada ocupando metade; palavra gigante vertical em marca-d'água; título curto em caixa com palavra-chave destacada; botão "Leia a legenda". | Azul-marinho e mostarda; Open Sauce; triângulos decorativos. |
| **Modelo 4** (capas) | Foto em tela cheia com escurecido e título centralizado; palavra quebrada em duas linhas gigantes ("econo/mizar"); destaque de palavra com marca-texto. | Paleta azul e amarela; telefone e site fictícios. |
| **Modelo 5** (6 slides) | Capa com gancho direto ao público ("Ei, Médico."), selo em faixa colorida com o benefício e objeto fotográfico; slides internos limpos com ponto + kicker + título + parágrafo curto; números destacados na cor de acento; slide de "ressalva" antes do CTA; seta circular discreta. | Fundo branco como base; vermelho; promessa numérica sem fonte ("60% a menos"). |
| **Storytelling** (5 slides, outro ramo) | **Só a narrativa:** gancho com fato surpreendente → contexto ("só tinha suporte para…") → obstáculo/tensão → virada (quem fez e como) → payoff → pergunta que puxa comentário. Cada slide termina deixando uma pergunta aberta. | Visual estilo tweet, foto de pessoa, conteúdo e assunto. |

## Estilos JA disponíveis

| Estilo | Arquivo | Quando usar | Slides |
|---|---|---|---|
| 01 — Clássico JA | `estilos/estilo-01-classico-ja.md` | Tema educativo/institucional, evergreen | 3 |
| 02 — Manchete JA | `estilos/estilo-02-manchete-ja.md` | Notícia com números fortes e várias medidas | 6 |
| 03 — Dossiê JA | `estilos/estilo-03-dossie-ja.md` | Aviso, obrigação, fiscalização, prazo ou golpe em que a pessoa precisa conferir e agir | 7 |
| 04 — Cards JA | `estilos/estilo-04-cards-ja.md` | "4 dúvidas": quatro temas, um por página, resposta na legenda (adaptação direta do Modelo 3) | 4 |

### Ideias ainda não criadas (criar quando a notícia pedir)

- **Linha do tempo:** prazos e cronogramas (ex.: transição IBS/CBS, datas de opção).
- **Mito × verdade:** boato ou interpretação errada circulando.
- **Pergunta e resposta:** dúvida recorrente de cliente com resposta curta por slide.
- **Caso anonimizado:** situação real tratada com sigilo (problema → análise → caminho).

## Tipo de notícia → estilo sugerido

| Tipo de notícia | Composição sugerida |
|---|---|
| Pacote/medida com números grandes | 02 — Manchete JA |
| Mudança de regra (antes/depois) | Manchete JA ou novo "Antes e depois" |
| Prazo/cronograma | Novo "Linha do tempo" |
| Obrigação nova, aviso ou fiscalização | 03 — Dossiê JA (ou novo "Checklist") |
| Golpe/fraude | 03 — Dossiê JA, se não for o último usado; senão novo "Mito × verdade" |
| Boato/confusão | Novo "Mito × verdade" |
| Tema educativo sem data | 01 — Clássico JA |
| Várias dúvidas evergreen em um post | 04 — Cards JA |

## Como criar um estilo novo

1. Ler `registro-de-uso.md` e não repetir o estilo do último post.
2. Combinar composições das referências acima; nunca as cores delas.
3. Salvar `estilos/estilo-NN-nome.md` com nome, quando usar, composição slide a slide, regras de cor, tipografia e arquivo-fonte de referência.
4. Adicionar o estilo à tabela "Estilos JA disponíveis".
5. Depois de produzir, registrar em `registro-de-uso.md`.
