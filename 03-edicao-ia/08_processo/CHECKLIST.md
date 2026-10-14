# CHECKLIST DE QUALIDADE — Edição JA Contabilidade

> Usar antes de postar. Cada vídeo deve passar em TODOS os itens.
> Baseado na revisão 3 do Reel Pintor.

---

## Pré-edição

- [ ] Vídeos organizados em `01_originais/(nome do tema)/`
- [ ] Áudio extraído em mono 16kHz para `02_audio/`
- [ ] Transcrição revisada (termos técnicos: CNPJ, MEI, DAS, PGDAS, e-CAC)
- [ ] EDL gerado com timestamps por palavra (`03_transcricoes/edl_*.json`)
- [ ] Tabela de trechos (S01–SNN) com layouts A/B/C definidos

## Legendas

- [ ] Fonte: **Creato Display Medium** (NÃO Montserrat)
- [ ] Tamanho: 52px
- [ ] Contorno: nenhum (0px)
- [ ] Sombra: preta 38%, desfoque 4px, deslocamento 1–1,5px
- [ ] Cor: branco sobre vídeo, grafite (#1A1A1A) sobre fundo branco
- [ ] Sem destaques coloridos (tudo branco)
- [ ] 1–3 palavras por bloco (ritmo de Reel)
- [ ] Sincronização com a fala (±100ms de tolerância)
- [ ] Fade in/out suave (120ms/150ms)

## Posicionamento

- [ ] Layout A (câmera): legenda em y=1401px
- [ ] Layout B (dividido): legenda em y=985px
- [ ] Layout C (visual): legenda em y=1401px
- [ ] Encerramento: legenda em y=1171px
- [ ] Legendas NÃO cobrem o rosto do apresentador
- [ ] Posição muda no frame exato do corte entre layouts

## Layouts

- [ ] Layouts A, B, C nunca repetem em sequência
- [ ] Layout B: cabeça recortada (u2net_human_seg), dissolve 40px na borda
- [ ] Layout B: vídeo em escala 1,2× na janela do cartão

## Motion / HyperFrames

- [ ] Composições renderizadas a 240fps → 60fps (motion blur natural)
- [ ] Quadro 0 e último quadro: sem desfoque (sigma 0)
- [ ] Máximo 1 whoosh por trecho
- [ ] Movimentos rápidos: SFX no ponto médio exato

## Cor / Imagem

- [ ] Cores do apresentador idênticas à gravação original
- [ ] iPhone HLG convertido com o libplacebo de curva fixa (WORKFLOW 1.2) — NUNCA pixels HLG crus
- [ ] Mesmo take comparado lado a lado (MOV convertido × render): pele, blusa branca, parede, pretos
- [ ] Arquivo final com tags BT.709 (ffprobe: color_primaries/transfer/space = bt709)
- [ ] Tom de pele, camisa, exposição visualmente iguais ao MOV original

## Áudio

- [ ] 4 stems: voice, sfx, riser, music
- [ ] Voz: comprimida (2,2:1), −14,0 LUFS
- [ ] SFX alinhados ao evento visual (desvio < 0,1ms)
- [ ] Whoosh: −9 dB vs voz
- [ ] Impacto: −10 dB vs voz
- [ ] Teclas/digitação: −16 dB vs voz
- [ ] Riser apenas no gancho (S01)
- [ ] Música começa no frame 1 (não frame 0)
- [ ] J-cut de 50ms em cada nova frase
- [ ] Pausas entre frases: máx 120ms

## Master / Render

- [ ] Master: −14,0 LUFS (±0,5 LU)
- [ ] Pico: ≤ −1,0 dBTP
- [ ] 1080×1920, 60fps, H.264 High
- [ ] CRF 14–20
- [ ] AAC estéreo 48kHz 320kbps
- [ ] Sem quadro branco/preto no início ou fim
- [ ] Tamanho < 50MB (limite Instagram)
- [ ] Arquivo salvo em `07_renderizados/VideoEditadoN.mp4`
- [ ] NUNCA sobrescrever versão anterior

## Divergências fala × fatos

- [ ] Se a fala cita número divergente de fontes oficiais: manter a fala
- [ ] Gráficos e textos visuais usam o número oficial (não o da fala)
- [ ] Divergências documentadas no relatório

## Pós-edição

- [ ] Registrar no `LOG_EDICOES.md`
- [ ] Relatório em `04_planos_de_cena/relatorio_*.md`
- [ ] Verificação por prancha (1 frame/s) completa
- [ ] Anotar aprendizados para próximas edições
