# Design system

O site institucional é a fonte de verdade. Carrosséis e vídeos podem usar variações já existentes, mas não substituir a paleta principal.

Fonte: briefing do Octavio, 2026-10-14; `04-projetos/landing-page/src/App.css`.

## Paleta

| Papel | Cor | Uso confirmado |
|---|---:|---|
| Principal/fundo | `#0A0A0A` | Fundo do site, link hub e carrosséis |
| Apoio escuro | `#111111` / `#0D0D0D` | Gradientes e cards web |
| Dourado principal | `#C8A55C` | CTA, links, números, linhas e destaques |
| Dourado secundário | `#A8894A` | Gradientes dos carrosséis |
| Texto forte | `#FFFFFF` | Títulos e texto sobre fundo escuro |
| Texto de corpo | `#CCCCCC` | Parágrafos em fundo escuro |
| Texto suave | `#BBBBBB` / `#999999` | Apoio e descrições |
| Texto secundário | `#888888` / `#666666` | Metadados e assinatura secundária |
| Linha/borda | `#1E1E1E` / `#222222` / `#2A2A2A` | Separadores e cards |
| Texto sobre fundo claro | `#1A1A1A` | Legendas e gráficos claros de vídeo |

Fontes: `04-projetos/landing-page/src/App.css`, linhas 13–15 e 120–148; `02-marketing/carrosseis/ibs-e-cbs/design-system/tokens.css`; `03-edicao-ia/08_processo/ESTILO.md`, seção “Legendas”.

O dourado `#C5A55A` aparece no guia de vídeo como aproximação de render da marca, mas novas interfaces e peças estáticas devem usar `#C8A55C`, que é a cor do site.

Fontes: `03-edicao-ia/08_processo/ESTILO.md`, tabela “Identidade visual”; `04-projetos/landing-page/src/App.css`.

## Tipografia

### Web e carrosséis

- Fontes oficiais de web e carrosséis (decisão do Octavio, 14/10/2026): **Inter, Poppins, Creato Display e Montserrat**. Sugestão de base: Montserrat (700–800) ou Creato Display em títulos; Inter ou Poppins (400–600) em corpo, labels, botões e assinatura. Variar o peso mais que a família.
- DM Serif Display e DM Sans aparecem só no site atual e nos carrosséis clássicos já publicados (ibs-e-cbs, simples-nacional); não usar em peças novas.
- Site: hero entre 40 e 52 px; corpo 17 px; títulos de cards 20 px; texto de cards 14 px.
- Carrossel na prancheta 432×540: título principal 30–34 px; secundário 24–26 px; corpo 12–13 px; label 10–12 px. A exportação é 2,5 vezes maior.

Fontes: `04-projetos/landing-page/src/App.css`, linhas 1, 12–14 e 282–299; `02-marketing/carrosseis/ibs-e-cbs/design-system/README.md`, seções 3–5.

### Vídeos

- `Creato Display Medium`, 52 px em 1080×1920, é a fonte final de legenda.
- `Creato Display Bold/ExtraBold` existe para gráficos já produzidos.
- Montserrat Bold/ExtraBold foi teste antigo e não deve ser usada em novas legendas de vídeo (vale só para vídeo).

Fontes: `03-edicao-ia/08_processo/ESTILO.md`, seções “Tipografia” e “Legendas”; `03-edicao-ia/08_processo/LOG_EDICOES.md`, Revisão 3.

Arquivos canônicos: `01-identidade/fontes/`. Arquivos locais disponíveis: Creato Display e Montserrat. Inter e Poppins entram via Google Fonts (ou baixar para `01-identidade/fontes/`): **[PREENCHER]** pacote local.

## Espaçamento

- Site: largura máxima de header 1200 px; padding `16px 40px`; hero `140px 40px 60px`; gaps recorrentes de 14, 16, 24, 32 e 40 px.
- Carrossel 432×540: padding horizontal 36 px, superior 54–60 px e inferior 30–36 px.
- Link hub: padding lateral 20 px; links com gap 12 px e padding `14px 18px`.

Fontes: `04-projetos/landing-page/src/App.css`, linhas 88–95, 127–139 e 233–247; `02-marketing/carrosseis/ibs-e-cbs/design-system/tokens.css`; `04-projetos/link-direciona/index.html`, linhas 21 e 62–65.

## Bordas, raios e sombras

- Botões web: raio 6 px no header e 8 px no hero.
- Cards de serviço: raio 16 px; cards “Quem somos?”: 20 px.
- Carrosséis: raio 4 px em labels e 8 px em caixas; o slide principal não arredonda.
- Link hub: raio 8 px.
- CTA hero: sombra dourada `0 4px 24px #C8A55C33`; hover `0 8px 32px #C8A55C44`.
- Legenda de vídeo: sombra preta 38%, blur 4 px, deslocamento de 1–1,5 px; sem contorno.

Fontes: `04-projetos/landing-page/src/App.css`, linhas 181–192 e 310–325; `04-projetos/landing-page/src/content/sections/section-servicos.html`, linhas 67–68; `02-marketing/carrosseis/ibs-e-cbs/design-system/tokens.css`; `03-edicao-ia/08_processo/ESTILO.md`.

## Botões e movimento

- CTA primário: fundo dourado, texto escuro, geometria compacta, verbo de ação.
- CTA secundário: fundo escuro, borda dourada translúcida.
- Site: `fadeUp`, `float`, `countUp` e `glowPulse`; respeitar `prefers-reduced-motion`.
- Link hub: somente transição de hover e escala 1.02.

Fontes: `04-projetos/landing-page/src/App.css`, linhas 35–74, 181–192 e 964–970; `04-projetos/link-direciona/index.html`, linhas 65–70 e 91–92.

## Biblioteca de modelos de carrossel (composição variável)

Decisão do Octavio, 14/10/2026: **identidade fixa, composição livre.** Cores, fontes, logo, rodapé e tom da JA nunca mudam; a composição muda a cada post.

Fonte da biblioteca: `02-marketing/carrosseis/modeloscarroseis/` (índice em `README.md`, estilos em `estilos/`, histórico em `registro-de-uso.md`).

Modelos válidos (todos podem ser usados e combinados):

| Origem | Modelo | Uso |
|---|---|---|
| Estilo JA | 01 Clássico (3 slides, padrão ibs-e-cbs) | Educativo/institucional |
| Estilo JA | 02 Manchete | Notícia com números fortes |
| Estilo JA | 03 Dossiê | Aviso, obrigação, prazo, golpe |
| Estilo JA | 04 Cards | Várias dúvidas, um card por página |
| Referência | Modelo 2 | Ritmo alternado, palavra-título gigante, objeto recortado, cartão-papel |
| Referência | Modelo 3 | Pessoa recortada em meia tela, palavra vertical em marca-d'água, botão "Leia a legenda" |
| Referência | Modelo 4 | Foto em tela cheia escurecida, palavra quebrada em duas linhas gigantes, marca-texto |
| Referência | Modelo 5 | Gancho direto ao público, selo, slides limpos com kicker, slide de ressalva |
| Referência | Storytelling | Só narrativa: gancho, tensão, virada, payoff, pergunta final |

Regras de uso:

0. **A biblioteca cresce:** o Octavio vai colocar modelos novos em `02-marketing/carrosseis/modeloscarroseis/` a qualquer momento. Antes de criar QUALQUER carrossel, listar a pasta inteira (imagens de referência, `estilos/` e subpastas), abrir o que for novo ou ainda não analisado e considerá-lo como opção válida. Modelo novo é analisado, entra na tabela do README e passa a poder ser combinado.
1. **Sempre consultar** `README.md` e `registro-de-uso.md` antes de criar um carrossel.
2. **Nunca repetir** o mesmo estilo em dois posts seguidos.
3. **Misturar e recombinar**: capa de um modelo, miolo de outro, fechamento de um terceiro (ex.: capa tela cheia do Modelo 4 + dado gigante + cartão-papel do Modelo 2 + CTA do Modelo 5). Cada post deve parecer novo.
4. Quando surgir uma combinação nova, **salvá-la** como `estilos/estilo-NN-nome.md` e registrar o uso.
5. Cores das referências nunca entram. Fundo claro só como elemento (cartão, faixa) em slide escuro, salvo exceção aprovada pelo Octavio (estilo 04).
6. Das referências externas, copiar apenas composição e ritmo; nunca texto, logo ou arte.
7. Fluxo de notícia: skill `/carrossel-noticia`.

### Eixos de variação (o que muda a cada post)

Identidade fixa: cores, logo, rodapé e tom de voz. **Fontes dos carrosséis (decisão do Octavio, 14/10/2026): Inter, Poppins, Creato Display e Montserrat.** DM Serif Display e DM Sans ficam só nos carrosséis clássicos já publicados; não são usados nos novos. O resto é livre, sempre com coesão e dentro da proposta da marca.

- **Tipografia:** escolher entre Inter, Poppins, Creato Display e Montserrat (Creato Display: arquivos em `01-identidade/fontes/`; as demais via Google Fonts). Variar **principalmente os pesos** (ex.: 300 a 800), além de tamanho, caixa e posição, mais do que trocar de família. Usar no máximo duas famílias por post, com coesão entre slides. Fora desta lista, só com aprovação do Octavio. A restrição de Montserrat vale apenas para legenda de vídeo.
- **Posição do texto:** topo, centro, rodapé, lateral, vertical, marca-d'água, palavra gigante cortada na borda, palavra quebrada em duas linhas.
- **Fundo:** preto liso, foto, gradiente preto/dourado, textura sutil.
- **Imagem:** tela cheia, meia tela, terço, recorte; posição centro ou lateral; fade ou gradiente para o preto; escurecida, duotone dourado ou P&B. Slide 1 pode ser imagem grande e os seguintes em metades ou recortes.
- **Formas de destaque:** faixas, círculos, linhas, selos, setas, caixas e marca-texto em volta das palavras-chave.
- **Ritmo da sequência:** alternar slides de imagem, texto, dado gigante, lista e respiro; mudar a ordem a cada post.

Checagem antes de exportar: o post difere do anterior em pelo menos três eixos, mantém coesão entre slides e continua legível no celular (contraste do texto sobre foto, sem colidir com o rodapé).

## Logo

Versões canônicas:

- `01-identidade/logos/logo-dourado.jpeg`: emblema dourado sobre preto; uso em carrosséis e fundos escuros.
- `01-identidade/logos/logo-preto.png`: versão limpa usada na revisão final de vídeo.
- `01-identidade/logos/logo-com-handle.png`: versão antiga com identificação social; não é a versão final de vídeo.

Fontes: `03-edicao-ia/05_assets/logo/`; `03-edicao-ia/08_processo/ESTILO.md`; `03-edicao-ia/08_processo/LOG_EDICOES.md`, Revisão 3.

Regras confirmadas:

- Não distorcer; escalar uniformemente.
- Em carrosséis, usar círculo de 28–32 px na prancheta 432×540 e acompanhar com “JA Contabilidade” + “Contabilidade | Perícia | Estratégia”.
- Em vídeo final, preferir a versão preta limpa e não adicionar sombra ao arquivo, salvo necessidade comprovada de contraste.

Fontes: `02-marketing/carrosseis/ibs-e-cbs/Carrossel IBS e CBS.dc.html`, linhas 48–57 e 98–105; `03-edicao-ia/04_planos_de_cena/relatorio_reel_simples.md`, Revisão 3.

- Área mínima de respiro oficial: **[PREENCHER]**
- Tamanho mínimo fora dos exemplos atuais: **[PREENCHER]**
- Versão para fundo dourado: **[PREENCHER]**
