# GUIA DE ESTILO — JA Contabilidade e Perícia

> Referência visual para todas as edições.
> Baseado na revisão 3 do Reel Pintor (versão final aprovada).

---

## Identidade visual

| Elemento | Valor |
|----------|-------|
| **Marca** | JA Contabilidade e Perícia |
| **Logo** | Letras "JA" dentro de coroa de louros + texto abaixo |
| **Cores da marca** | Preto (#000) + Dourado (#C5A55A) |
| **Presença no vídeo** | Logo aparece na parede do cenário + overlay animado em S07 |
| **Variantes de logo** | `ja logo preta.png` (Rev3), `ja logooo.png` (com @handle, Rev2), `logo.jpeg` (dourada, S07) |

---

## Tipografia

| Uso | Fonte | Tamanho (1080×1920) |
|-----|-------|---------------------|
| Legenda (revisão 3) | **Creato Display Medium** | 52px |
| Legenda sobre fundo branco | **Creato Display Medium** | 52px, cor grafite (#1A1A1A) |

**Histórico de fontes:**

| Revisão | Fonte | Tamanho | Notas |
|---------|-------|---------|-------|
| v1 | Creato Display Medium | 66px | Primeira versão |
| v2 | Creato Display Medium | 66px | Contorno 3px preto, destaques amarelos |
| **v3 (atual)** | **Creato Display Medium** | **52px** | Sem contorno, sem destaques coloridos |

**ATENÇÃO:** a edição simples (IMG_2168) usou Montserrat Bold como teste.
A fonte oficial da produção é **Creato Display Medium**. Montserrat NÃO deve ser
usada em novas edições.

---

## Legendas — estilo final (revisão 3)

| Propriedade | Valor |
|-------------|-------|
| **Fonte** | Creato Display Medium |
| **Tamanho** | 52px |
| **Cor sobre vídeo** | Branco (#FFFFFF) |
| **Cor sobre fundo branco** | Grafite (#1A1A1A) |
| **Contorno** | Nenhum (0px) |
| **Sombra** | Preta 38% opacidade, desfoque 4px, deslocamento 1–1,5px |
| **Destaques coloridos** | Removidos (tudo branco) |
| **Palavras por bloco** | 1–3 (ritmo rápido de Reel) |

### Evolução das legendas (para referência)

| Revisão | Contorno | Sombra | Destaques | Resultado |
|---------|----------|--------|-----------|-----------|
| v1 | 3px preto | 50% 2px | Amarelo/vermelho/ciano | Muito carregado |
| v2 | 3px preto | 50% 2px | Amarelo | Melhor, ainda pesado |
| **v3** | **Nenhum** | **38% 4px blur** | **Nenhum** | **Limpo e moderno** |

**Regra para novos Reels:** seguir revisão 3 — sem contorno, sem cores de destaque,
sombra sutil. O minimalismo é a identidade visual.

---

## Posicionamento por layout (1080×1920)

A posição Y da legenda muda conforme o layout do trecho:

```
┌─────────────────────────┐
│  y=100 ── topo gráfico  │  ← Área do motion (layout B/C)
│                          │
│  y=900 ── fim gráfico   │
│  y=985 ── LEGENDA (B)   │  ← Layout B: acima do cartão de vídeo
│  y=1060 ── topo cabeça  │  ← Cabeça recortada (layout B)
│  y=1200 ── borda cartão │
│  y=1401 ── LEGENDA(A/C) │  ← Layout A e C: na metade inferior
│  y=1171 ── LEGENDA(enc) │  ← Encerramento/CTA
│  y=1518 ── centro logo  │
└─────────────────────────┘
```

| Layout | Posição Y da legenda | Contexto |
|--------|---------------------|----------|
| **A (câmera)** | 1401px | Apresentador tela cheia |
| **B (dividido)** | 985px | Gráfico em cima, vídeo embaixo |
| **C (visual)** | 1401px | Animação tela cheia |
| **Encerramento** | 1171px | CTA final |

**Regra:** legendas NUNCA cobrem o rosto do apresentador.

**Exceções pontuais (só onde o contraste pede — configuradas em `src/ajustes.json`):**
- Roupa preta em tela cheia → legenda branca com sombra (padrão "sobre vídeo").
- Roupa branca + parede clara → legenda grafite na parede acima da cabeça, ~100 px de folga do cabelo.
- Gráfico grande no centro (urna) → legenda abaixo dele com folga da sombra.
Em cortes entre layouts, a posição muda no frame exato do corte.

---

## Zonas seguras para redes sociais

- Instagram Reels: evitar 250px superiores (ícones) e 300px inferiores (botões)
- TikTok: evitar 150px superiores e 350px inferiores
- YouTube Shorts: mais flexível, respeitar 200px inferior

---

## Efeitos de animação

### Entrada de legenda
- Fade in: 120ms
- Sem scale pop na revisão 3 (era 100%→105%→100% na v1)

### Fade out
- Fade out: 150ms
- 150ms antes do próximo bloco

### Banner de alerta (S01 — gancho)
- Aparece: 0,3s do vídeo
- Fade in: 250ms
- Fundo: retângulo colorido (vermelho ou temático)
- Duração: até ~5,2s (enquanto o dado está sendo absorvido)

### Carimbo animado (S01 — quando aplicável)
- Exemplo: "EXCLUSÃO" diagonal sobre notícia/documento
- Impacto com SFX de carimbo sincronizado ao frame de chegada

### Zoom de câmera
- Intensidade: variável, com motion blur (sigma = 0,29·v·0,75/60)
- Quadro 0 e último: SEMPRE sem desfoque (sigma 0)
- Movimentos rápidos: máximo 1 whoosh por trecho

---

## Áudio / SFX

### Volumes relativos à voz

| Tipo de SFX | Volume (vs voz) |
|-------------|-----------------|
| Whoosh | −9 dB |
| Impacto | −10 dB |
| Sinal (2 notas) | −10 dB |
| Teclas/digitação | −16 dB |
| Riser de tensão | −12 dB |
| Música de fundo | −10 dB |

### Regras

- Voz SEMPRE prioridade absoluta
- SFX alinhado ao evento visual (desvio < 0,1ms do ponto médio)
- Master: −14,0 LUFS (±0,5 LU), pico ≤ −1,0 dBTP
- Riser só no gancho (S01)
- Música começa no frame 1 (não frame 0)
- J-cut de 50ms em cada nova frase

---

## Vocabulário contábil

Mesmo sem destaques coloridos (revisão 3), estas palavras recebem
**ênfase na narração e nos gráficos**:

### Dados e números
- Valores: R$, mil, milhão, bilhão, %
- Siglas: CNPJ, CPF, MEI, CNAE, DAS, PGDAS, IRPJ, e-CAC
- Prazos: janeiro, dezembro, dia 20, 2025, 2026

### Problemas e riscos
- Ações: perder, excluir, multa, penalidade, atraso
- Situações: dívida, irregularidade, exclusão, indeferimento

### Pessoas e casos
- Profissões: pintor, eletricista, dentista, advogado
- Situações: "meu cliente", "um empresário"
- Desfechos: regularizou, economizou, conseguiu
