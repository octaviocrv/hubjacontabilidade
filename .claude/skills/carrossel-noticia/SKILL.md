---
name: carrossel-noticia
description: "Use when: criar carrossel a partir de notícia quente contábil/tributária (reforma tributária, Receita Federal, Simples, MEI, IR, prazos) ou pedir /carrossel-noticia."
---

# Carrossel de notícia da JA

Transforma a notícia contábil/tributária mais relevante da semana em roteiro de storytelling e, após aprovação, em carrossel com estilo da biblioteca da JA.

## REGRA INVIOLÁVEL: aprovação do roteiro

Depois de escrever o roteiro/texto dos slides, **PARAR e esperar a aprovação explícita do Octavio**. Proibido, em qualquer circunstância (inclusive modo autônomo, ausência dele ou "continue trabalhando"): gerar HTML, imagens ou PNGs, baixar fotos ou registrar o post como feito antes dessa aprovação. Silêncio não é aprovação. Se o Octavio pedir mudanças, ajustar o roteiro e pedir aprovação de novo. Só salvar o `roteiro.md`.

## Fontes obrigatórias

1. Todos os arquivos de `00-contexto/` e `_memoria/`.
2. `02-marketing/carrosseis/modeloscarroseis/README.md`: biblioteca, identidade fixa e o que aproveitar de cada referência.
3. `02-marketing/carrosseis/modeloscarroseis/registro-de-uso.md`: último estilo usado.
   **Antes de qualquer carrossel, listar a pasta `modeloscarroseis/` inteira**: o Octavio adiciona modelos novos ao longo do tempo. Abrir os novos, analisar e incluir como opção.
4. `02-marketing/carrosseis/modeloscarroseis/estilos/*.md`.

## Fluxo

1. **Pesquisar** amplamente, sem se prender a uma fonte ou tema. Áreas de interesse de um escritório de contabilidade e perícias:
   - tributário, fiscal e mudanças de legislação;
   - trabalhista, previdenciário e eSocial;
   - societário, abertura/encerramento de empresa, MEI e Simples;
   - finanças e gestão para pequenas empresas;
   - perícia contábil e judicial;
   - tecnologia, IA e automação na contabilidade;
   - golpes e fraudes fiscais, prazos e obrigações, tendências do mercado.
   **Radar internacional:** olhar também a seção de economia/negócios da BBC (bbc.com/portuguese e bbc.com/news/business), além de Reuters, Agência Brasil e similares, procurando curiosidades ou tendências do mundo ligadas a contabilidade, impostos, trabalho, fraudes, IA e pequenas empresas. Não precisa ter ligação direta com o Brasil: uma curiosidade internacional interessante pode virar post sozinha, desde que seja relevante e atrativa para o público da JA. Quando fizer sentido, comentar o que isso significa para o empresário brasileiro, sem forçar. Parafrasear e citar link e data da matéria no último slide.
   **Playwright:** usar sempre que possível e sempre que precisar validar algo (página renderizada, tabela, aviso oficial, número, data). Se não estiver disponível, usar Chrome headless.
   **Prints e dados como material do carrossel:** quando um print do site, um gráfico ou um dado visual for interessante e combinar com o layout, **trazê-lo para o slide** (recortado, tratado nas cores da JA quando fizer sentido, com crédito da fonte). Só capturar e trazer se for realmente usado na renderização final; não acumular prints sem uso. Salvar o material usado na pasta do tema. Para prints de terceiros (BBC, portais), manter recorte curto, crédito visível e link; preferir dado ou gráfico a matéria inteira.
   Fontes possíveis: gov.br (Receita, Fazenda, MTE, MEMP, PGFN), Diário Oficial, tribunais (STF, STJ, TST, TRTs), CFC/CRCs, Agência Brasil/Agência Gov, portais contábeis (Contábeis, IOB), imprensa econômica e estudos (Serasa, Sebrae, IBGE). Anotar URL e data de acesso. Os temas citados aqui são exemplos, não uma lista fechada.
2. **Escolher** a mais útil e interessante para o público da JA (`00-contexto/marca.md`), de preferência ligada a um serviço comprovado e com recorte local (Minas Gerais/Contagem) quando houver. **Variar a área**: consultar "Temas já usados" em `registro-de-uso.md` e não repetir a área do post anterior. Listar as candidatas descartadas com o motivo.
3. **Conferir na fonte primária** todos os números, prazos, alíquotas e status (anunciado, proposto, aprovado, em vigor). O que não for confirmado fica marcado e fora dos slides, ou entra com ressalva.
4. **Roteiro em storytelling:** gancho forte → contexto → prova/dado → comparação ou tensão → payoff → CTA. Último slide com fontes e data.
5. **Escolher ou criar o estilo:** nunca o mesmo da última linha do registro. Todos os modelos e estilos da biblioteca são válidos: consultar `00-contexto/design-system.md` (seção "Biblioteca de modelos") e misturar elementos de vários (capa de um, miolo de outro, fechamento de outro) para sempre gerar algo novo, mantendo cores, fontes e rodapé da JA. Variar os eixos listados em "Eixos de variação" no design-system (fontes: Inter, Poppins, Creato Display e Montserrat, variando mais os pesos que a família), diferindo do último post em pelo menos três eixos. Usar a tabela "Tipo de notícia → estilo sugerido". Se criar um estilo novo, salvar `estilos/estilo-NN-nome.md` e atualizar o README da biblioteca.
6. **Salvar o roteiro** em `02-marketing/carrosseis/<tema>/roteiro.md` com tabela de conferência de dados e fontes.
7. **PARAR** e mostrar: "Olha, esse é o script". Só seguir após aprovação explícita do Octavio.
8. **Montar** o HTML `Carrossel <Tema>.dc.html` na pasta do tema, copiando a estrutura de exportação dos carrosséis existentes (`?exportSlide=N`), com `Logo.jpeg` e fotos na mesma pasta.
9. **Exportar** PNG 1080×1350 com `google-chrome-stable` headless (`--window-size=432,540 --force-device-scale-factor=2.5`, `?exportSlide=N` para cada slide), servindo `02-marketing/carrosseis/` com `python3 -m http.server` em 127.0.0.1. O script `ibs-e-cbs/exportar_png_instagram.sh` cobre só 3 slides; para mais slides, repetir o mesmo comando por slide. Conferir cada PNG visualmente: espaço vazio, quebras de linha órfãs, contraste e colisão com o rodapé.
10. **Registrar** em `registro-de-uso.md`: data, pasta, estilo, notícia, fonte e status, e a área em "Temas já usados".

## Regras de conteúdo

- Parafrasear. Trecho literal só com menos de 15 palavras, entre aspas, com fonte.
- Fonte e data sempre no último slide e na legenda ou roteiro.
- Diferenciar sempre "anunciado", "proposto", "aprovado" e "em vigor". Sem promessa de resultado e sem alarmismo.
- Neutralidade política: descrever o ato ("o Governo Federal enviou…"), sem elogio ou crítica. Em período eleitoral, preferir pautas técnicas a anúncios de governo.
- Texto revisado: acentos, vírgula decimal, "R$ 12,6 bilhões", datas dd/mm/aaaa.

## Regras de imagem

- Nunca gerar imagem de IA de pessoa real.
- Preferir Pexels (uso comercial livre) ou fotos enviadas pelo Octavio. Agência Brasil/Agência Gov só com licença verificada para uso da empresa, fotógrafo e crédito.
- Evitar foto de político ou ato partidário.
- Registrar origem, ID e licença de cada foto no roteiro.

## Regras de hub

- Cores, fontes, logo e assinatura da JA são fixos. Referências externas nunca fornecem cor.
- Não mexer em `04-projetos/`.
- Não fazer commit sem pedido do Octavio. Nunca fazer push.
- Publicação exige OK explícito por peça.
