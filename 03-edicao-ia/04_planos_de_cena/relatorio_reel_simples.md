# Relatório de edição — Reel "Seu CNPJ vai sair do Simples?"

Entregas em `edit/`: `final.mp4` (1080×1920, 60 fps, H.264 High CRF 14, AAC estéreo 48 kHz 320 kb/s, 3401 quadros), `stems/voice.wav`, `stems/sfx.wav`, `stems/riser.wav`, `stems/music.wav`. Os quatro stems são WAV PCM 24-bit/48 kHz estéreo, todos com exatamente 2 720 800 amostras (= END) e sincronizados a partir de t = 0. Somados com um ajuste de master de −0,5 dB, eles reproduzem o master.


## Revisão 3 (substitui os itens correspondentes das revisões anteriores)
- **Imagem da câmera sem nenhuma alteração**: removi qualquer tonemapping ou conversão de cor. Os valores de pixel são os do arquivo original; só a profundidade caiu de 10 para 8 bits (com dithering, para não criar faixas) e a matriz YUV foi convertida para BT.709 mantendo o mesmo RGB. Não há glow, brilho, contraste, saturação ou filtro.
- **Legendas iguais à referência**: Creato Display Medium, 52 px (antes 66), branco, sem contorno, com sombra suave e leve (preta a 38%, desfoque 4 px, deslocamento de 1–1,5 px), centro em y = 1402 (posição medida na imagem de referência). As palavras deixaram de ser destacadas em amarelo. A legenda fica longe do rosto em todas as cenas: o queixo está, no máximo, em ≈1290 no layout dividido e em ≈950 na câmera cheia. Exceção: nas cenas só de animação, com fundo branco, o mesmo padrão aparece em grafite (#1A1A1A), porque o texto branco ficaria invisível ali.
- **Logo**: substituída pela versão preta (`ja logo preta.png`), na mesma posição e escala, sem alterações no arquivo e sem sombra adicional.

## Revisão 2: identidade visual, legendas e cor (substitui os itens correspondentes abaixo)
- **Logo oficial** (`ja logooo.png`, logo + "JA Contabilidade" + "@jacontabilidade_"): o arquivo foi aplicado sem alterar cores, proporções ou transparência, só com escala uniforme de 0,599 (647×809 em x = 276, y = 1100). Assim o círculo fica centrado em (410, 1518) e reproduz a posição da imagem de referência. Ela aparece em todos os trechos com o João Pedro (A e B: S01, S03, S04, S06, S07, S09, S11, S12, S14, S16) e some nos trechos só de animação (C). Recebeu a mesma sombra suave das legendas, porque o texto branco do arquivo some contra a camisa clara.
- **Legendas**: Creato Display Medium (a fonte instalada no sistema), 66 px, branco, posição única em todo o vídeo: X central e Y = 1356 px, que equivale a Y −792 no CapCut, considerando 2 unidades do CapCut por pixel em 1080×1920. Sombra preta a 49%, desfoque 15, distância 5, ângulo −45° (3,5 px para a direita e para baixo). Acrescentei um contorno preto fino de 3 px, porque só com a sombra o texto branco ficava ilegível sobre a parede branca, a camisa e os fundos claros. As palavras de destaque continuam em amarelo, mas na mesma fonte (sai a serifada itálica).
- **Cor**: removi a conversão anterior (tonemapping mobius com branco de referência de 203 nits), que clareava os brancos e esfriava a imagem. Agora a conversão HDR→SDR usa o libplacebo com tonemapping padrão BT.2390, sem nenhum ajuste de brilho, saturação, glow ou filtro. Paredes, camisa e tons de pele ficam como na gravação.
- **Layout dividido**: o vídeo no cartão subiu para y = 100 (antes 254). Com a legenda em y = 1356, o rosto fica inteiro acima dela (queixo ≈ 1290) e a cabeça recortada passa a sobressair mais do cartão (topo entre ≈ 906 e 954, abaixo da área gráfica, que termina em 900).
- **CTA**: a caixa de comentário subiu para y = 1080–1356 para não ficar sobre a legenda e a logo.
- Animações, gráficos, áudio, cortes e END (56 683 ms) não mudaram. Master: −14,0 LUFS e −1,1 dBTP.

## 1. END
**END = 56 683 ms** (quadro 3401 a 60 fps, término exclusivo da faixa de voz). Vídeo, voz, efeitos, riser, música e master terminam exatamente em END.

## 2. Trechos

| # | Início (ms) | Fim (ms) | Layout | Conteúdo |
|---|---|---|---|---|
| S01 | 0 | 5 917 | B dividido | Gancho: "Quase um milhão e meio de CNPJs vão perder o Simples Nacional em janeiro, e a empresa desse pintor era uma delas." Captura real da notícia do Portal do Simples Nacional, carimbo "EXCLUSÃO 01/01/2027" e cartão da empresa de pintura. Capa no quadro 0. |
| S02 | 5 917 | 10 350 | C visual | "Funciona assim. Você cria o CNPJ, toca seu negócio e os tributos vão ficando pra trás." |
| S03 | 10 350 | 13 583 | A câmera | "Esse cliente nos procurou, pois já estava há dois anos sem pagar nenhum tributo." |
| S04 | 13 583 | 16 117 | B dividido | "Trabalhava normalmente e pensava que estava tudo certo." |
| S05 | 16 117 | 20 733 | C visual | "Porém, ao analisar sua situação, sua dívida já estava muito alta e com juros e multa em cima." |
| S06 | 20 733 | 23 367 | A câmera | "Ele chegou ao nosso escritório pensando que não tinha saída." |
| S07 | 23 367 | 26 550 | B dividido | "Portanto, em nossa consultoria, levantamos três pontos." |
| S08 | 26 550 | 29 367 | C visual | "Primeiro, levantamos todas as pendências do CNPJ." |
| S09 | 29 367 | 32 667 | B dividido | "Segundo, regularizamos todas as obrigações que estavam atrasadas." |
| S10 | 32 667 | 35 300 | C visual | "E terceiro, montamos um plano para quitar sua dívida." |
| S11 | 35 300 | 38 450 | A câmera | "E o melhor, conseguimos um desconto de 50% do valor." |
| S12 | 38 450 | 41 367 | B dividido | "Após analisar a situação do cliente, chegamos à seguinte conclusão." |
| S13 | 41 367 | 45 900 | C visual | "Sua dívida, que estava em aproximadamente R$ 108 mil, reduzimos para R$ 54 mil," |
| S14 | 45 900 | 49 517 | B dividido | "e o melhor, podendo ser dividida em até 145 prestações." |
| S15 | 49 517 | 52 467 | C visual | "Milhões de empresas estão nessa situação e não sabem." |
| S16 | 52 467 | 56 683 | A câmera | Encerramento/CTA: "E a sua? Como está? Procure a JA Contabilidade para fazer sua consultoria." + cartão de comentário. |

Os três layouts aparecem no vídeo e nunca se repetem em sequência. O trecho mais longo tem 5,9 s. O gancho usa o layout dividido e o encerramento usa câmera em tela cheia.

## 3. Tomadas
A pasta continha 8 arquivos MOV (iPhone, HEVC 10-bit HLG/Dolby Vision, vertical por rotação de metadados). Eles formam um único roteiro gravado em partes. O arquivo anexado (IMG_2168) é a primeira tentativa do gancho.

| Frase | Tentativas | Usada | Descartada / removido |
|---|---|---|---|
| Gancho ("Quase um milhão e meio…") | IMG_2168, IMG_2171 | **IMG_2171** (última, sem defeito) | IMG_2168: mesma frase completa ("Quase um milhão e meio de CNPJs vão perder o Simples Nacional em janeiro, e a empresa desse pintor era uma delas.") |
| Três pontos ("Primeiro… Segundo… E terceiro… E o melhor…") | IMG_2196, IMG_2200 | **IMG_2200** (última, completa até "50% do valor") | IMG_2196: lista inteira terminando em "…desconto de 50% do valor em até 145 prestações". Em 2200 foram removidos "Pode ir? Pode." (preparação). |
| "Funciona assim… juros e multa em cima" | só IMG_2186 | IMG_2186 | Removidos a repetição gaguejada de "sua" (15,81–15,96 s, entre "situação," e "sua dívida") e ruídos antes da fala |
| "Ele chegou… três pontos" | só IMG_2189 | IMG_2189 | — |
| "Após analisar… 145 prestações" | só IMG_2206 | IMG_2206 | Ruídos/murmúrios antes de 4,3 s |
| "Milhões de empresas… consultoria" | só IMG_2208 | IMG_2208 | — |

**Substituições por tomada anterior: nenhuma.** As últimas tomadas não tinham defeito audível de palavra. O final "em até 145 prestações" de 2196 não foi reaproveitado porque a mesma informação está em 2206.

Corte de áudio aplicado: pré-roll de 40 ms antes da primeira palavra, final real medido por RMS em janelas de 10 ms (≥ −35 dBFS, com checagem de trechos > 150 ms abaixo de −32 dB), pausas > 250 ms reduzidas para 120 ms (junções entre 113 e 127 ms, ajustadas ao quadro), J-cut de 50 ms em cada nova frase, cauda em volume normal até o ruído de fundo e fade de até 170 ms sem invadir o próximo som. A maior pausa medida na voz final é de 120 ms.

Contato visual: inspecionei de 8 a 22 quadros por tomada e, nas inclinações de cabeça de IMG_2189 (1,6–3,3 s), quadros a cada 100 ms. Os olhos ficam na lente o tempo todo; a única exceção é uma piscada numa pausa já cortada. Nenhum trecho precisou virar visual por desvio de olhar.

## 4. Composições gráficas (HyperFrames, 240 fps → 60 fps por mistura de 4 quadros)
- **S01**: recorte real da notícia "Receita Federal emite Termo de Exclusão para devedores do Simples Nacional, incluindo MEI" (Portal do Simples Nacional, 01/04/2026) como documento. Em "janeiro" entra o carimbo vermelho "EXCLUSÃO 01/01/2027"; em "pintor" chega o cartão "Pintura & Acabamentos" e em "delas" aparece a etiqueta "Termo de Exclusão". A câmera faz um deslocamento suave.
- **S02**: o número do CNPJ é digitado com cursor e o selo "Ativa" confirma. A câmera passa ao cartão de obra, onde um rolo pinta a parede, e as guias DAS "Em aberto" deslizam para trás do cartão. Um recuo revela a pilha.
- **S04**: "Agenda de obras" com as obras marcadas como concluídas uma a uma, depois o selo verde em "tudo certo".
- **S05**: uma lupa varre o relatório "Situação fiscal". Um movimento rápido (único do trecho) leva ao bloco da dívida, que conta até R$ 72.400; os blocos "+ Juros" e "+ Multa" caem em cima e o total vai a R$ 108.000.
- **S07**: o selo JA, grande e centralizado, recua e três blocos numerados (1, 2, 3) chegam.
- **S08**: "Relatório de pendências", com uma faixa de varredura que marca cada item como "Pendente".
- **S09**: janela "Obrigações acessórias" ampliada de 1,0 para 1,15× (0,5 s, power2.inOut, câmera parada). O cursor clica em "Transmitir" e as obrigações passam de "Atrasada" para "Entregue".
- **S10**: "Plano de quitação", com parcelas encaixando em sequência até "Quitação".
- **S12**: planilha "Análise do débito" preenchida, linha do total destacada com a faixa #FBEEE8 e confirmação.
- **S13**: barra "Dívida inicial" enche e mostra "R$ 108 mil". Um movimento rápido leva a "Após a negociação", onde o valor conta até R$ 54 mil, a barra cai pela metade e aparece "−50%".
- **S14**: uma barra de saldo se divide em 145 fatias e a câmera se aproxima (1,6 s até 1,75×) do recorte real da Legisweb, com a faixa de destaque em "em até 145 meses".
- **S15**: página real do Portal do Simples Nacional em moldura fixa (24, 200, 1032×1040, raio 36) sobre a cópia desfocada (40 px, saturação 0,7, brilho 1,05, branco 72%). Um movimento rápido interno leva à frase "Foram notificados 1.102.924 maiores devedores", destacada.
- **Sobreposição**: capa "Seu CNPJ vai / sair do Simples?" (Poppins Bold 110, caixa y 262–603) só no quadro 0; legendas com 1 a 3 palavras a partir de 17 ms; cartão de CTA que digita "Consultoria" com cursor piscante e clica em "Publicar".

Prancha de frames inspecionada para cada composição. O desfoque de movimento usa sigma = 0,29·v·0,75/60 (máx. 40 px) e só existe durante os movimentos: o quadro 0 e o último quadro de cada trecho têm sigma 0.

## 5. Fatos verificados e fontes
| Dado na fala | Verificação | Fontes |
|---|---|---|
| Empresas perderão o Simples "em janeiro" | ✔ A exclusão produz efeitos em **01/01/2027** para quem não regularizar | Portal do Simples Nacional / Receita Federal, notícia de 01/04/2026; Ministério da Fazenda (gov.br, mar/2026); Seu Dinheiro, 06/04/2026 |
| "Quase um milhão e meio de CNPJs" | ✘ Fonte oficial: **1.102.924** CNPJs notificados (404.368 MEI + 698.556 ME/EPP; ~R$ 12,9 bi) | Portal do Simples Nacional (01/04/2026); Seu Dinheiro ("mais de 1,1 milhão") |
| "Em até 145 prestações" | ✔ A Lei 13.988/2020 (transação) permite a ME/EPP prazo de até 145 meses e desconto de até 70% | Legisweb / Fenacon-Sebrae (15/04/2020); Agência Gov/PGFN (jan/2024: "até 145 vezes, desconto de até 70%") |
| "Desconto de 50%" e "R$ 108 mil → R$ 54 mil" | Caso do cliente, sem fonte pública. Os números são coerentes entre si (54/108 = 50%) e ficam dentro do teto legal de 70% | — |
| "Dois anos sem pagar" | Caso do cliente, sem fonte pública | — |

URLs: <https://www8.receita.fazenda.gov.br/simplesnacional/noticias/NoticiaCompleta.aspx?id=b47f0c13-23f9-43a6-a84d-1ab91e29cc66> · <https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/marco/receita-federal-emite-termo-de-exclusao-para-devedores-do-simples-nacional-incluindo-mei> · <https://www.seudinheiro.com/2026/seu-negocio/alerta-ao-empreendedor-mais-de-11-milhao-de-meis-micro-e-pequenas-empresas-podem-ser-excluidos-do-simples-nacional-por-dividas-como-consultar-giov/> · <https://www.legisweb.com.br/noticia/?id=23865> · <https://agenciagov.ebc.com.br/noticias/202401/pgfn-oferece-novas-possibilidades-de-pagamento-de-dividas-para-pessoas-fisicas-e-juridicas>

## 6. Divergências entre fala e fontes
1. **"Quase um milhão e meio de CNPJs"**: o dado oficial é 1.102.924 (~1,1 milhão). A gravação foi mantida, mas os gráficos não repetem o número falado: S01 mostra só a manchete e a data, S15 destaca o número oficial, e as palavras "milhão e meio" não recebem destaque amarelo na legenda.
2. **"Milhões de empresas estão nessa situação"**: a fonte registra 1,1 milhão de notificadas, não "milhões". A fala foi mantida e o gráfico mostra o número oficial; "Milhões" também não foi destacado.
3. **Prazo**: segundo a Receita, quem recebeu o termo em março tinha 90 dias para regularizar. Esse prazo provavelmente já terminou na data da gravação (09/10/2026), mas a exclusão em 01/01/2027 continua correta.

## 7. Efeitos sonoros (tempos no vídeo final)
| Tempo | Trecho | Efeito | Evento |
|---|---|---|---|
| 3,430 s | S01 | impacto abafado | carimbo "EXCLUSÃO" bate |
| 4,573 s | S01 | impacto abafado | cartão da empresa chega |
| 7,047 s (+0,69 s) | S02 | sequência de teclas (11) | digitação do CNPJ |
| 7,819 s | S02 | sinal de duas notas | selo "Ativa" |
| 9,617 s | S02 | impacto abafado | guias DAS chegam |
| 15,493 s | S04 | sinal de duas notas | "tudo certo" |
| 17,570 s | S05 | **whoosh A** | ponto médio exato do movimento rápido |
| 19,750 / 20,270 s | S05 | impactos | blocos "Juros" e "Multa" |
| 25,997 s | S07 | impacto abafado | blocos 1-2-3 chegam (o logotipo não tem efeito) |
| 27,253 s (+1,5 s) | S08 | sequência de dados (21) | varredura das pendências |
| 30,310 s | S09 | clique | botão "Transmitir" pressionado |
| 30,610 s (+1,28 s) | S09 | sequência de dados (18) | transmissão das obrigações |
| 31,940 s | S09 | sinal de duas notas | todas entregues |
| 33,483 s (+1,17 s) | S10 | sequência de dados (16) | parcelas encaixando |
| 38,800 s (+1,06 s) | S12 | sequência de teclas (16) | valores digitados |
| 40,820 s | S12 | sinal de duas notas | conclusão |
| 44,350 s | S13 | **whoosh B** | ponto médio exato do movimento rápido |
| 45,390 s | S13 | sinal de duas notas | "−50%" |
| 50,267 s | S15 | **whoosh C** | ponto médio exato do movimento rápido |

São 3 whooshes no total (variações A, B e C), no máximo um por trecho. O pico de energia de cada um, medido no stem, cai no ponto médio do movimento (desvio < 0,1 ms). Não há efeitos em mudanças de layout, deslocamentos suaves, aproximações, logotipo ou CTA. O riser soa de 3,435 s a 5,917 s e termina exatamente na junção S01→S02. A primeira batida da música está no quadro 1 (16,7 ms), a 110 BPM.

## 8. Loudness (filtro ebur128 do FFmpeg)
| Faixa | LUFS integrado | Pico verdadeiro |
|---|---|---|
| voice.wav | −14,0 | −2,2 dBTP |
| sfx.wav | −24,3 | −11,1 dBTP (pico da voz −2,2 → whoosh −9 dB; impactos/cliques/sinais −10 dB; teclas/dados −16 dB) |
| riser.wav | −26,9 | −16,2 dBTP (−14 dB do pico da voz) |
| music.wav | −23,9 | −12,1 dBTP (≈10 LU abaixo da voz, nível único sem automação) |
| **Master (final.mp4, AAC)** | **−14,0** | **−1,1 dBTP** |

A soma das faixas deu −13,5 LUFS; apliquei um único ajuste de master de −0,5 dB, sem mexer no equilíbrio entre os stems. O limitador do master não foi necessário.

## 9. Reconstruções, alternativas e decisões
- **Escopo**: usei os 8 MOV da pasta como gravação bruta (o roteiro completo e a CTA só existem somando os arquivos), não só o IMG_2168 anexado.
- **Áudio limpo**: não havia arquivo de voz separado. A única fonte de voz é a trilha AAC dos próprios MOV (microfone de lapela visível na camisa). Mesmo assim rodei a correlação cruzada (mono 16 kHz) entre o AAC da câmera e o PCM extraído: deslocamento 0 amostras e pico normalizado 1,00 em todas as tomadas. A verificação é trivial porque as fontes são a mesma.
- **HDR**: as fontes HLG/Dolby Vision foram convertidas para SDR BT.709 (zscale + tonemap mobius) e para 60 fps exatos, preservando o tempo real.
- **Voz**: com −14 LUFS a voz original teria picos de +3,6 dBFS. Apliquei compressão suave (2,2:1) e um limitador com look-ahead de 4 ms, teto −2,2 dBFS, só na voz. O ruído de fundo subiu proporcionalmente.
- **Transcrição**: faster-whisper (modelo medium, pt) com tempos por palavra; o finais foram refinados por RMS. Corrigi "ajoutar" → "a JA".
- **Layout dividido com fonte vertical**: vídeo em escala 1,2 (1296×2304) em x = −108, y = 254, recortado pela janela do cartão 1210×864 em (−65, 1200), com raio 200 em superelipse (n = 5), sombra de 3 camadas e contorno de 10% de opacidade. A cabeça recortada (remove-background do HyperFrames, u2net_human_seg) usa só o alfa da máscara sobre o MESMO quadro e a mesma geometria. Fica opaca até a borda e se dissolve em 40 px dentro do cartão (y 1200–1240), então não aparece emenda nem nos movimentos rápidos (conferido a cada 100 ms em S01, 3,0–4,1 s). Topo da cabeça entre y = 1060 e 1108. A cabeça não sobe mais porque, acima disso, as legendas obrigatórias (941–1114) cobririam o rosto; centralizei-as em y = 985.
- **Legendas**: posição única por trecho (B 985, A/C 1401, encerramento 1171). Blocos que atravessam um corte mudam para a posição do novo trecho no quadro do corte. Os destaques foram escolhidos manualmente e nunca são consecutivos: em geral há 2 ou 3 blocos normais entre eles, com uma exceção de 4 antes de "JA Contabilidade". O negrito do Instrument Serif é sintético, porque a fonte não tem peso bold.
- **Logotipo JA**: reconstruído a partir do adesivo na parede do escritório (recorte, alfa por luminância, correção de rotação). Não foi usado arquivo oficial.
- **Interfaces e dados ilustrativos**: "Obrigações acessórias", "Relatório de pendências", "Análise do débito", "Agenda de obras" e "Plano de quitação" são representações genéricas, não capturas de sistemas reais (o e-CAC/PGDAS exigem login). Também são fictícios e ilustrativos: o CNPJ 12.345.678/0001-90, o nome "Pintura & Acabamentos", os valores das guias DAS e a divisão principal/juros/multa (R$ 72.400 / 21.700 / 13.900), escolhida só para somar os R$ 108 mil falados.
- **Fontes**: a página do gov.br/Receita exigiu login na captura headless, então usei o texto idêntico no Portal do Simples Nacional. A página da Agência Gov estava "temporariamente indisponível", então usei a Legisweb. Ocultei banners de anúncio; nenhum consentimento foi aceito.
- **Capa**: "Seu CNPJ vai sair do Simples?", derivada do gancho e sem repetir o número divergente.
- **Palavra da CTA**: "Consultoria", a palavra-chave da chamada falada (a fala não pede um comentário específico). Sem efeito sonoro no CTA.

## 10. Verificação final
- ✔ Formato: 1080×1920, 60/1 fps, 3401 quadros; H.264 + AAC 48 kHz estéreo; duração 56,683 s = END.
- ✔ Cortes: os 15 cortes conferidos nos quadros f0−1 e f0. A nova tomada aparece desde o primeiro quadro previsto e a anterior vai até o último.
- ✔ A cabeça recortada está presente desde o primeiro quadro de cada trecho dividido (as máscaras têm o mesmo número de quadros dos clipes: 355/152/191/198/175/217) e se mantém alinhada ao cartão em movimento rápido.
- ✔ Prancha do vídeo inteiro (1 quadro/s): legendas fora do rosto e da borda do cartão; amarelos alternados; conteúdo nas áreas seguras; sem grades nem áreas escuras; capa limpa só no quadro 0; sem erro de máscara.
- ✔ Áudio: efeitos nos eventos visuais; whooshes no ponto médio dos 3 movimentos rápidos; riser termina em 5,917 s; maior silêncio em junção de 120 ms (≤ 150 ms); voz −14,0, música −23,9 e master −14,0 LUFS (tolerância ±0,5 LU); pico verdadeiro do master −1,1 dBTP.
- ✔ Último quadro: câmera com CTA, sem quadro branco, cabeça congelada ou silêncio sobrando.
- Defeitos encontrados e corrigidos antes da entrega: faixa clara na emenda cabeça/cartão (degradê), borda do cartão invisível (contorno), carimbo cobrindo a manchete, selos sem posicionamento absoluto (S04/S12), cursor parado no quadro 0 (S09), faixas de destaque desalinhadas (S14/S15), legendas na posição errada após cortes e whooshes com até 49 ms de desvio do ponto médio.
