# JA Contabilidade e Perícia — Edição de Vídeos

Projeto de edição automatizada de vídeos para redes sociais (Reels/TikTok/Shorts)
do escritório **JA Contabilidade e Perícia**.

## Estrutura de pastas

```
JaContabilidadeEdicao/
│
├── 01_originais/          ← Vídeos brutos (.MOV) direto do celular
├── 02_audio/              ← Áudio extraído dos vídeos (.wav 16kHz mono)
├── 03_transcricoes/       ← Transcrição palavra a palavra com timestamps
├── 04_planos_de_cena/     ← Plano de cenas detalhado por vídeo
├── 05_assets/             ← Recursos reutilizáveis
│   ├── fontes/            ← Montserrat Bold/ExtraBold
│   ├── logo/              ← Logo JA Contabilidade (PNG/SVG)
│   └── sons/              ← Efeitos sonoros (whoosh, click, alert)
├── 06_legendas/           ← Arquivos .ass (legendas animadas)
├── 07_renderizados/       ← Vídeos finais prontos para postar
└── 08_processo/           ← Documentação do workflow
    ├── WORKFLOW.md         ← Receita de bolo completa
    ├── ESTILO.md           ← Guia de estilo visual
    ├── CHECKLIST.md        ← Checklist de qualidade
    └── LOG_EDICOES.md      ← Registro de cada edição feita
```

## Como usar

1. Coloque o vídeo bruto em `01_originais/`
2. Siga o [WORKFLOW.md](08_processo/WORKFLOW.md) — passo a passo
3. O vídeo final sai em `07_renderizados/`

## Ferramentas necessárias

- **ffmpeg** — extração de áudio, renderização de vídeo
- **Python 3.12 + faster-whisper** — transcrição com timestamps
- **Fonte Montserrat** — já incluída em `05_assets/fontes/`
- **Node.js + GSAP + Puppeteer** (opcional) — preview interativo

## Primeiro vídeo editado

- `IMG_2168.MOV` → `IMG_2168_renderizado.mp4`
- Data: 2026-10-13
