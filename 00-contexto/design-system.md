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

- `DM Serif Display`, peso 400: títulos hero e títulos editoriais.
- `DM Sans`, pesos 400, 500, 600 e 700: corpo, navegação, labels, botões e assinatura.
- Site: hero entre 40 e 52 px; corpo 17 px; títulos de cards 20 px; texto de cards 14 px.
- Carrossel na prancheta 432×540: título principal 30–34 px; secundário 24–26 px; corpo 12–13 px; label 10–12 px. A exportação é 2,5 vezes maior.

Fontes: `04-projetos/landing-page/src/App.css`, linhas 1, 12–14 e 282–299; `02-marketing/carrosseis/ibs-e-cbs/design-system/README.md`, seções 3–5.

### Vídeos

- `Creato Display Medium`, 52 px em 1080×1920, é a fonte final de legenda.
- `Creato Display Bold/ExtraBold` existe para gráficos já produzidos.
- Montserrat Bold/ExtraBold foi teste antigo e não deve ser usada em novas legendas.

Fontes: `03-edicao-ia/08_processo/ESTILO.md`, seções “Tipografia” e “Legendas”; `03-edicao-ia/08_processo/LOG_EDICOES.md`, Revisão 3.

Arquivos canônicos: `01-identidade/fontes/`. Arquivos locais de DM Sans e DM Serif Display não foram encontrados: **[PREENCHER]** quanto à licença e ao pacote local.

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
