# WORKFLOW — Receita de Bolo da Edição JA Contabilidade

> Processo completo: do vídeo bruto ao Reel pronto para postar.
> Documentado a partir da edição real do "Reel Simples Nacional / Pintor".

---

## Visão geral do pipeline

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ 1.IMPORT │──▶│ 2.ÁUDIO  │──▶│3.TRANSCR.│──▶│ 4.PLANO  │──▶│ 5.MOTION │──▶│6.OVERLAY │──▶│ 7.RENDER │
│ + HDR→SDR│   │ extrair  │   │ Whisper  │   │ de cenas │   │ HyperFr. │   │ legendas │   │  final   │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
 01_originais   02_audio      03_transcri    04_planos      gfx/S01-S16   06_legendas    07_render
```

---

## ETAPA 0 — Organizar os vídeos brutos

Os MOVs do iPhone vêm nomeados como IMG_XXXX.MOV. Organizá-los em `01_originais/` por tema:

```
01_originais/
├── Video Pintor/         ← Reel do Simples Nacional (8 MOVs)
├── Video Politica/       ← Próximo reel (11 MOVs)
└── (próximo tema)/
```

**Importante:** os MOVs do iPhone são HEVC 10-bit HLG/Dolby Vision. Precisam de
conversão HDR→SDR antes de editar (ver Etapa 1).

---

## ETAPA 1 — Extrair áudio + converter HDR→SDR

### 1.1 Extrair áudio para transcrição
```bash
ffmpeg -y -i "01_originais/VIDEO.MOV" -vn -ac 1 -ar 16000 "02_audio/VIDEO.wav"
```

### 1.2 Converter HDR→SDR (para edição)

Os vídeos do iPhone são HEVC 10-bit **HLG BT.2100 (primárias BT.2020) + Dolby Vision 8.4**.
Conversão oficial (desde o Reel Política rev2 — feita dentro do `montar_edl60.py`):

```bash
ffmpeg -y -i "VIDEO.MOV"   -vf "libplacebo=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:tonemapping=spline:gamut_mode=perceptual:peak_detect=0:contrast_recovery=0:apply_dolbyvision=0:dithering=blue:format=yuv420p"   -c:v libx264 -preset medium -crf 10 -color_primaries bt709 -color_trc bt709 -colorspace bt709   "VIDEO_sdr.mp4"
```

- `peak_detect=0`: curva FIXA. Com detecção de pico por quadro o brilho muda de take para take
  (medido: parede da Malu 146 vs 174 no mesmo cenário).
- `apply_dolbyvision=0`: os metadados DV esfriam a parede (azulada) e escurecem a pele.
- Resultado medido: pele com densidade e calor, dobras da blusa branca preservadas, pretos firmes,
  parede clara com textura (não é escurecimento geral — os 1% mais claros ficam iguais).

**Lições aprendidas:**
- Reel Pintor rev1: tonemapping mobius com branco de 203 nits clareou os brancos e esfriou a imagem.
- Reel Pintor rev3 / Política rev1: "manter os pixels HLG" (só trocar a matriz) parecia neutro, mas
  exibido como SDR o trecho logarítmico do HLG achata médios e altas luzes e as primárias 2020 lidas
  como 709 perdem saturação → **pele lavada, sem contraste, áreas claras quase brancas**. Não usar mais.
- Uma LUT própria BT.2408 (branco SDR 330–470 nits) foi testada e descartada: estourava parede e blusa.
- Conferir sempre lado a lado: quadro do MOV convertido × quadro do render, em todos os takes.

**Regra:** a imagem do apresentador (camisa, tom de pele, exposição, brilho e
contraste) deve ficar visualmente IDÊNTICA à gravação original.

---

## ETAPA 2 — Transcrever palavra a palavra

```python
import sys, wave, numpy as np
from faster_whisper import WhisperModel

w = wave.open(sys.argv[1])
a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
m = WhisperModel("medium", compute_type="int8")
segs, info = m.transcribe(a, language="pt", word_timestamps=True)

for s in segs:
    for x in s.words:
        print(f"{x.start:6.2f} -> {x.end:6.2f}  {x.word.strip()}")
```

**Pós-processamento:**
- Revisar termos técnicos (CNPJ, MEI, DAS, IRPJ, e-CAC, PGDAS)
- Corrigir erros comuns: "ajoutar" → "a JA" (Reel Pintor)
- Refinar finais por análise RMS (janelas de 10ms, ≥ −35 dBFS)
- Pausas > 250ms reduzidas para 120ms nas junções

**Saída:** `edl.json` com timestamps por palavra alinhados à timeline do vídeo final.

---

## ETAPA 3 — Montar a tabela de trechos

Cada vídeo (Reel) é dividido em trechos numerados (S01, S02, ...) com layout alternado:

| Layout | Código | Descrição |
|--------|--------|-----------|
| **A — Câmera** | `A câmera` | Apresentador em tela cheia, sem gráficos |
| **B — Dividido** | `B dividido` | Tela dividida: gráfico em cima, vídeo em baixo recortado com cabeça saliente |
| **C — Visual** | `C visual` | Tela inteira de animação/motion graphic, sem apresentador |

**Regra:** os layouts A, B e C nunca se repetem em sequência.

### Tabela modelo (do Reel Pintor, 16 trechos, 56,7s):

| # | Início | Fim | Layout | Conteúdo |
|---|--------|-----|--------|----------|
| S01 | 0,000 | 5,917 | B | Gancho + notícia + carimbo EXCLUSÃO |
| S02 | 5,917 | 10,350 | C | CNPJ digitado + rolo de tinta + guias DAS |
| S03 | 10,350 | 13,583 | A | "cliente nos procurou..." |
| S04 | 13,583 | 16,117 | B | Agenda de obras + selo "tudo certo" |
| ... | ... | ... | ... | ... |
| S16 | 52,467 | 56,683 | A | CTA: "Procure a JA Contabilidade" |

---

## ETAPA 4 — Motion Design (HyperFrames / GSAP)

Composições gráficas renderizadas a 240 fps e reduzidas para 60 fps (mistura de 4 quadros para motion blur natural).

### 4.1 Tipos de composição já criados:

| Tipo | Exemplo | Elementos |
|------|---------|-----------|
| Documento/Notícia | S01 | Captura real de site, carimbo animado |
| Interface simulada | S02, S08, S09, S10 | CNPJ, pendências, obrigações |
| Dados financeiros | S05, S13 | Contador de valores, barras animadas |
| Planilha/Análise | S12, S14 | Linhas preenchendo, faixas de destaque |
| Portal/Site real | S15 | Moldura fixa, fundo blur, aproximação |
| Logo + blocos | S07 | Selo JA centralizado, 3 blocos numerados |

### 4.2 Regras de motion

- **Zoom:** câmera suave com desfoque de movimento (sigma = 0,29·v·0,75/60, máx. 40px)
- **Movimentos rápidos (whoosh):** máximo 1 por trecho, com SFX no ponto médio exato
- **Quadro 0 e último quadro:** SEMPRE sem desfoque (sigma 0)
- **Layout B (dividido):** vídeo em escala 1,2× na janela do cartão, cabeça recortada (u2net_human_seg), dissolve em 40px na borda

### 4.3 Transições "saída do ser humano"

**Conceito central:** nos momentos-chave, a câmera "sai" do apresentador para
uma tela gráfica (animação de dados, interface, documento), e depois "volta".

```
Layout A (câmera) → corte para Layout C (visual) → corte para Layout B (dividido)
                                                    ↑ apresentador volta, menor
```

Padrão ABC que alterna: nunca duas câmeras seguidas, nunca dois visuais seguidos.

---

## ETAPA 5 — Legendas

### 5.1 Especificações (do Reel Pintor — Revisão 3)

| Propriedade | Valor |
|-------------|-------|
| **Fonte** | Creato Display Medium |
| **Tamanho** | 52px (revisão 3; era 66px na revisão 2) |
| **Cor** | Branco (#FFF) — sobre vídeo; Grafite (#1A1A1A) — sobre fundo branco |
| **Sombra** | Preta 38%, desfoque 4px, deslocamento 1–1,5px |
| **Contorno** | Nenhum (removido na revisão 3; era 3px preto na revisão 2) |
| **Destaques** | Removidos na revisão 3 (era amarelo na revisão 2) |
| **Posição Y** | Layout B: 985px / Layout A e C: 1401px / Encerramento: 1171px |

**Nota:** O Reel Pintor passou por 3 revisões de legenda. O estilo final é
minimalista — sem contorno, sem amarelo. Para novos Reels, seguir a revisão 3.

### 5.2 Regras de posicionamento

```
┌─────────────────────────┐
│  y=100 ── topo gráfico  │  ← Área do motion (layout B)
│  y=900 ── fim gráfico   │
│  y=985 ── legenda (B)   │  ← Acima do cartão
│  y=1060-1108 ── topo    │  ← Cabeça recortada
│    da cabeça             │
│  y=1200 ── borda cartão │
│  y=1401 ── legenda(A/C) │  ← Na metade inferior
│  y=1518 ── centro logo  │
└─────────────────────────┘
```

- Legendas NUNCA cobrem o rosto
- Em cortes, a posição muda no frame do corte
- 1-3 palavras por bloco de legenda (ritmo rápido)

---

## ETAPA 6 — Áudio (4 stems)

O áudio final é composto por 4 stems sincronizados:

| Stem | Conteúdo | LUFS | Pico |
|------|----------|------|------|
| `voice.wav` | Voz do apresentador, comprimida (2,2:1) | −14,0 | −2,2 dBTP |
| `sfx.wav` | Efeitos sonoros (47 eventos) | −24,3 | −11,1 dBTP |
| `riser.wav` | Riser de tensão (S01, 3,4–5,9s) | −26,9 | −16,2 dBTP |
| `music.wav` | Música de fundo (110 BPM) | −23,9 | −12,1 dBTP |

**Master:** −14,0 LUFS, pico −1,1 dBTP. Ajuste de −0,5dB sem alterar equilíbrio.

### 6.1 SFX por tipo

| Tipo | Volume (vs voz) | Quando |
|------|-----------------|--------|
| Whoosh | −9 dB | Movimentos rápidos (máx 1/trecho) |
| Impacto | −10 dB | Elementos chegando (carimbo, cartão) |
| Sinal (2 notas) | −10 dB | Confirmações (selo, conclusão) |
| Teclas/dados | −16 dB | Digitação, varredura |
| Contador | variável | Valores subindo/descendo |

### 6.2 Regras de áudio

- Voz SEMPRE prioridade
- SFX alinhado ao evento visual (desvio < 0,1ms do ponto médio)
- Riser só no gancho (S01), termina no corte S01→S02
- Música começa no frame 1 (não no frame 0)
- Pausas entre frases: máx 120ms
- J-cut de 50ms em cada nova frase

---

## ETAPA 7 — Render + versionamento

### 7.1 Render final

```bash
ffmpeg -y -i base.mp4 \
  -i overlay.mov -i master.wav \
  -filter_complex "[0:v][1:v]overlay=format=auto" \
  -map "[out]" -map 2:a \
  -c:v libx264 -preset medium -crf 14 -pix_fmt yuv420p \
  -c:a aac -b:a 320k \
  "VideoEditadoN.mp4"
```

### 7.2 Versionamento

**Regra:** NUNCA sobrescrever. Sempre criar nova versão:

| Versão | Arquivo | O que mudou |
|--------|---------|-------------|
| v1 | `final.mp4` | Primeira entrega |
| v2 | `VideoEditado2.mp4` | Cor HDR→SDR corrigida, fonte/logo/legendas |
| v3 | `VideoEditado3.mp4` | SFX novos (47), sombra legendas, animação S01/S07 |
| vN | `VideoEditadoN.mp4` | Próxima versão |

### 7.3 Checklist de entrega

- [ ] 1080×1920, 60 fps, H.264 High
- [ ] CRF 14-20 (qualidade alta)
- [ ] AAC estéreo 48kHz 320kbps
- [ ] Master: −14,0 LUFS (±0,5 LU), pico ≤ −1,0 dBTP
- [ ] Sem quadro branco/preto no início ou fim
- [ ] Legendas não cobrem o rosto
- [ ] Cores iguais ao original (sem conversão HDR indevida)
- [ ] Verificação por prancha (1 frame/s) completa

---

## Apêndice — Divergências entre fala e fatos

O Reel Pintor contém duas divergências documentadas:

1. **"1,5 milhão"** → dado oficial: 1.102.924 (~1,1 milhão). Fala mantida; gráficos mostram o número oficial.
2. **"Milhões de empresas"** → fonte registra 1,1 milhão. Fala mantida; gráfico mostra número oficial.

**Regra:** quando a fala diverge de fontes oficiais, manter a fala mas NUNCA repetir
o número errado nos gráficos ou legendas destacadas. Usar o dado oficial nos visuais.
