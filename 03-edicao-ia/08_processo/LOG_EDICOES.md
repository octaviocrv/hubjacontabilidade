# LOG DE EDIÇÕES — JA Contabilidade

> Registro de cada vídeo editado. Um bloco por vídeo, mais recente primeiro.

---

## #001 — Reel Simples Nacional / Pintor

**Data:** 2026-10-13
**Duração final:** 56,683s (56,7s)
**Resolução:** 1080×1920 (vertical) @ 60fps
**Codec:** H.264 High, CRF ~14-16
**Áudio:** AAC estéreo 48kHz 320kbps, master −14,0 LUFS

### Conteúdo

> Reel completo sobre exclusão do Simples Nacional: 1,1 milhão de CNPJs em risco,
> caso real de um pintor regularizado pela JA Contabilidade.

### Fontes de vídeo (6 MOVs usados)

| MOV | Conteúdo | Trechos |
|-----|----------|---------|
| IMG_2168 | Gancho "quase 1,5 milhão" | S01, S03 |
| IMG_2170 | "cliente nos procurou" | S06 |
| IMG_2171 | "pintor, mas tinha empresa" | S06 (cont.) |
| IMG_2172 | "todas as pendências" | S11 |
| IMG_2173 | "a empresa dele agora" | S16 (CTA) |
| IMG_2174 | "Faz parte do time JA" | S16 (cont.) |

### Estrutura (16 trechos)

| # | Início | Fim | Layout | Conteúdo |
|---|--------|-----|--------|----------|
| S01 | 0,000 | 5,917 | B | Gancho + notícia + carimbo EXCLUSÃO |
| S02 | 5,917 | 10,350 | C | CNPJ digitado + rolo de tinta + guias DAS |
| S03 | 10,350 | 13,583 | A | "cliente nos procurou..." |
| S04 | 13,583 | 16,117 | B | Agenda de obras + selo "tudo certo" |
| S05 | 16,117 | 19,967 | C | Calculadora DAS + valores |
| S06 | 19,967 | 24,767 | A | "pintor, mas tinha empresa..." |
| S07 | 24,767 | 28,317 | B | Selo JA + 3 blocos numerados |
| S08 | 28,317 | 31,717 | C | Painel de obrigações |
| S09 | 31,717 | 35,600 | A | "verificamos..." |
| S10 | 35,600 | 38,783 | B | Status pendências |
| S11 | 38,783 | 42,217 | A | "todas as pendências" |
| S12 | 42,217 | 44,817 | C | Planilha preenchendo |
| S13 | 44,817 | 48,183 | B | Contador de economia |
| S14 | 48,183 | 50,317 | C | Análise final |
| S15 | 50,317 | 52,467 | A | Portal e-CAC |
| S16 | 52,467 | 56,683 | A | CTA: "Procure a JA Contabilidade" |

### Histórico de revisões

#### Revisão 1 → `final.mp4` (47,7 MB)
- Primeira versão com HDR→SDR via libplacebo (tonemapping mobius, 203 nits)
- Fonte Creato Display Medium 66px com contorno 3px preto
- Destaques coloridos (amarelo/vermelho/ciano)
- SFX básicos
- **Problema:** cores lavadas pelo tonemapping, brancos claros demais

#### Revisão 2 → `VideoEditado2.mp4` (50,4 MB)
- Removeu tonemapping mobius (zscale direto BT.709)
- Contorno de legenda mantido 3px
- Destaques amarelos mantidos
- Logo `ja logooo.png` com @handle
- **Melhoria:** cores mais naturais, mas contorno ainda pesado

#### Revisão 3 → `VideoEditado3.mp4` (51,3 MB) — VERSÃO FINAL
- Removeu QUALQUER conversão de cor (pixels originais, só 10→8 bits + dithering)
- Legenda: fonte 52px (reduzida de 66), contorno removido, sombra 38% blur 4px
- Destaques coloridos removidos (tudo branco)
- Logo `ja logo preta.png` (versão limpa sem @handle)
- **47 efeitos sonoros** (vs SFX básicos na v1):
  - Carimbo "EXCLUSÃO" no S01 (substituiu som genérico)
  - Contador de dinheiro no S05 e S13
  - Sons de teclas/digitação
  - Whooshes em transições
  - Sinais de confirmação (2 notas)
- Animação de entrada do card S01 (slide + bounce)
- Animação do selo JA no S07 (3 blocos entrando sequencialmente)
- Sombra de legenda corrigida (era outline, virou drop shadow)

### Áudio (4 stems)

| Stem | LUFS | Pico dBTP |
|------|------|-----------|
| voice.wav | −14,0 | −2,2 |
| sfx.wav (47 eventos) | −24,3 | −11,1 |
| riser.wav | −26,9 | −16,2 |
| music.wav (110 BPM) | −23,9 | −12,1 |

**Master final:** −14,0 LUFS, pico −1,1 dBTP

### Ferramentas usadas

- ffmpeg 9.0.2 (HDR→SDR, composição, render final)
- Python 3.12 + faster-whisper medium (transcrição)
- HyperFrames (motion graphics 240fps→60fps com motion blur)
- u2net_human_seg (recorte de cabeça para layout B)
- audio_rev5.py (mixagem de stems)
- build_gfx.py + compose.py (composição de cenas)

### Aprendizados

1. Tonemapping HDR→SDR muda cores — para iPhone HLG, melhor NÃO converter
2. Contorno de legenda é desnecessário quando há sombra sutil
3. Reduzir fonte de 66→52px melhora leitura (menos obstrução visual)
4. Destaques coloridos (amarelo/vermelho) distraem — branco único é mais limpo
5. 47 SFX com timing preciso (< 0,1ms) cria ritmo profissional
6. Carimbo sonoro específico > som genérico (buscar o efeito certo faz diferença)
7. Layout alternado A→B→C→A nunca repete o mesmo tipo em sequência

### Arquivos

| Tipo | Caminho |
|------|---------|
| EDL | `03_transcricoes/edl_reel_simples.json` |
| Relatório | `04_planos_de_cena/relatorio_reel_simples.md` |
| Tabela de trechos | `04_planos_de_cena/tabela_trechos_reel_simples.md` |
| SFX timing | `05_assets/sons/sfx_events.json` |
| Versão 1 | `09_versoes_anteriores/edit/final.mp4` |
| Versão 2 | `09_versoes_anteriores/edit/VideoEditado2.mp4` |
| **Versão 3 (final)** | `07_renderizados/VideoEditado3.mp4` |
| Stems v3 | `09_versoes_anteriores/edit/stems/` |
| Stems v5 | `09_versoes_anteriores/edit/stems5/` |

---

## #000 — IMG_2168 (teste de pipeline)

**Data:** 2026-10-13
**Duração:** 8,71s
**Resolução:** 1080×1920

### Conteúdo

> Teste com um único clipe do Reel Pintor. Usado para validar o pipeline
> de transcrição + ASS + ffmpeg. NÃO é uma edição de produção.

### O que foi testado

- ✅ Extração de áudio (ffmpeg → WAV 16kHz mono)
- ✅ Transcrição palavra a palavra (faster-whisper medium, português BR)
- ✅ Legendas ASS com karaokê (\k tags)
- ✅ Cores por tipo (amarelo/vermelho/ciano) — descartadas na produção
- ✅ Banner de alerta no topo
- ✅ Render ffmpeg com `subtitles=` + `fontsdir=`
- ❌ Zoom (não aplicado)
- ❌ SFX (não adicionados)
- ❌ HyperFrames (não usado)

### Diferenças vs produção

| Aspecto | Teste (#000) | Produção (#001) |
|---------|-------------|-----------------|
| Fonte | Montserrat Bold | Creato Display Medium |
| Contorno | 4px preto | Nenhum |
| Sombra | 50% 2px | 38% 4px blur |
| Destaques | Amarelo/vermelho/ciano | Branco único |
| Composição | ffmpeg + ASS apenas | HyperFrames + composição multicamada |
| SFX | Nenhum | 47 eventos |
| Áudio | Original do MOV | 4 stems masterizados a −14 LUFS |

### Arquivos

| Tipo | Caminho |
|------|---------|
| Transcrição | `03_transcricoes/IMG_2168_palavras.txt` |
| Plano | `04_planos_de_cena/IMG_2168_plano_de_cenas.md` |
| ASS | `06_legendas/IMG_2168.ass` |
| Render | `07_renderizados/IMG_2168_renderizado.mp4` (3,9 MB) |

---

## #002 — Video Politica ("Quem ganhar a eleição muda o seu imposto?")
**Data:** 2026-10-13/14 · **Projeto:** `09_motion/politica-eleicoes/` · **Saída:** `07_renderizados/VideoPolitica_Editado1.mp4`
**Formato:** 1080×1920, 60 fps, H.264 High CRF 16, AAC 320 kbps · 32,183 s (1931 quadros) · 22,5 MB · master −14,0 LUFS / −1,3 dBTP

### Tomadas (11 MOV, várias repetições)
| Fala | Tentativas | Usada |
|---|---|---|
| João: "E aí, Malu… pra presidente?" | 2222 | 2222 |
| Malu: "Não sei ainda… votar em…" | 2223, 2224 | 2223 (termina em suspense e liga com a virada) |
| "Independente do candidato… quem se planeja" | 2227, 2230, 2231, 2232, 2233 | 2232 (texto completo; 2233 diz "dependente", 2230 perde "continuar") |
| "Sem planejamento… dívidas desconhecidas" | 2236, 2237 | 2236 |
| "Não adianta esperar… do seu caixa" | 2236, 2237 | 2237 ("problema do seu caixa") |
| CTA | 2239 | 2239 |

### Trechos (layouts A/B/C sem repetição)
S01 B gancho (calendário 25/10, carimbo 2º turno) · S02 C urna digitando "PRESIDENTE" · S03 A Malu · S04 B apuração A×B · S05 C "Se A vencer = Se B vencer" (mesmo imposto) · S06 A · S07 B NF-e "ERRADA" + dívidas embaralhadas · S08 C "Esperar a política?" × "Seu caixa" despencando · S09 B checklist (responde aos 3 problemas) + "Empresa preparada" · S10 C logo + medidor de carga tributária · S11 A CTA @jacontabilidade_

### Pipeline
`montar_edl60.py` (cortes, câmera rev3, voz) → `enquadrar.py` (rosto) → `09_motion/politica-eleicoes/build.py` (index/gfx/ovl) → render gfx 240 fps + tmix → 60 fps; ovl 60 fps MOV alfa → `mixar_audio.py` (4 stems, 55 SFX) → `compor_final.py` (trecho a trecho + concat)

### Aprendizados
1. Pastas com várias tomadas da mesma fala: comparar transcrições palavra a palavra; misturar tomadas entre frases (2236+2237) funciona com J-cut.
2. Rastreio facial (YuNet) + crop interpolado no ffmpeg reenquadra o cartão B mesmo com a apresentadora levantando (S04).
3. Camisa branca: legenda branca some → grafite com halo claro nos trechos A.
4. Uma raiz HyperFrames por pasta (`layers/gfx`, `layers/ovl`), senão o lint acusa raízes múltiplas.
5. Compor trecho a trecho (como o compose.py) evita buffer enorme no ffmpeg.
6. Render gfx 240 fps: ~7,5 min para 32 s.

### Revisão 2 → `07_renderizados/VideoPolitica_Editado2.mp4` (2026-10-14)
32,483 s (1949 quadros, +0,30 s) · 25,8 MB · H.264 High 60 fps, tags BT.709 · master −14,0 LUFS / −1,5 dBTP · capa separada `VideoPolitica_Editado2_capa.png`
Backup da rev1 (fontes, scripts, EDL, camadas): `09_versoes_anteriores/politica_editado1/`

| Pedido | O que foi feito |
|---|---|
| Exposição/cor (pessoas estouradas, pele lavada) | Causa: pixels HLG/BT.2020 exibidos como SDR (curva log achatada + gamut 2020 lido como 709). Agora libplacebo com curva fixa (spline, sem detecção de pico, sem DV) dentro do `montar_edl60.py`. Overlays verificados: não alteravam a câmera (diferença < 1 nível). Pele ganhou densidade, blusa branca recuperou dobras/listras, pretos firmes, parede segue clara. |
| S01 igual ao original (0–3 s) | Layout A: só a câmera do João. Saíram calendário, card da urna, carimbo, etiqueta "Eleições 2026", 7 SFX e o riser. Legenda branca (padrão "sobre vídeo" do ESTILO): a grafite sumiria na camiseta preta. Capa do quadro 0 virou PNG separado. |
| Legenda sobre a urna | Bug: a 1ª legenda do S02 ("Tá pensando") nascia no quadro do corte e herdava a posição do S01 (y 1040, em cima da urna). Busca do trecho agora +20 ms. Legendas do S02 em y 1475. |
| Visor "atravessando" a urna | O texto "LARANJA para CORRIGIR" vazava pela moldura. Visor com `overflow:hidden`, instruções em 2 linhas (VERDE/LARANJA nas cores das teclas), urna entra como objeto rígido (desliza, sem escala), visor liga dentro da moldura. |
| Som da urna | Bipe eletrônico quando o visor liga (3,36 s, 13 dB abaixo do pico da voz) + blips por letra de "PRESIDENTE". |
| Legenda da Malu (blusa branca/parede clara) | S03: legenda grafite na parede acima da cabeça (y 735; ~110 px de folga do cabelo, abaixo do letreiro), só nesse trecho. |
| Suspense | +0,30 s de imagem real após "votar em…" (ela segura a pose, mão no queixo). Zoom progressivo 1,00→1,14 ancorado no rosto (ease-in). Música perde o ar (passa-baixa + silêncio no fim da fala), cama grave com batimento lento + riser sutil. |
| Virada | Zoom-through: nos últimos 0,20 s o zoom acelera com motion blur (obturador 180°, subamostras); o S04 (Malu em pé) chega a 1,40× e assenta em 0,45 s. Whoosh + impacto grave no corte; música reancorada no corte (1º tempo forte = impacto) com palmas leves. Etiqueta/selo do S04 entram depois do assentamento. |

Preservado: todos os gráficos S04–S11 (conferidos quadro a quadro contra a rev1 nos tempos +0,30 s), os 101 tempos de palavra (iguais ou +0,30 s exatos), posições/estilo das legendas fora do S01–S03.

### Decisões a validar
- Layout B invertido (apresentador em cima, gráficos embaixo), pedido explícito para este vídeo; o Reel Pintor usava o contrário.
- Valores de imposto (R$ 18.430), NF-e, CNPJ 12.345.678/0001-90 e saldos são ilustrativos. Candidatos genéricos A/B, sem partido (neutralidade).
- Música e SFX sintetizados localmente (sem licença de terceiros).

---

## #003 — (próximo vídeo)
*pendente*
