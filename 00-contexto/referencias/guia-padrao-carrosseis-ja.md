# Guia Padrao de Carrosseis JA

Este documento e a referencia oficial para criar novos carrosseis da JA com consistencia visual.

## 1. Objetivo

Manter todos os carrosseis com a mesma identidade premium da marca, mesmo quando fotos, tema e copy mudarem.

## 2. Identidade fixa da marca (nao negociar)

Itens obrigatorios em todos os carrosseis:
- Logo oficial: Logo.jpeg
- Nome: JA Contabilidade
- Linha de apoio: Contabilidade | Pericia | Estrategia
- Estetica base: fundo escuro + dourado como acento
- Hierarquia tipografica: serif para titulos, sans para corpo
- Formato final: 1080x1350 (4:5)

## 3. Paleta oficial

- Fundo principal do slide: #0A0A0A
- Fundo da area de edicao: #1A1A1A
- Dourado principal: #C8A55C
- Dourado secundario: #A8894A
- Texto forte: #FFFFFF
- Texto corpo: #CCCCCC
- Texto secundario: #888888
- Separadores: #1E1E1E / #222222

## 4. Tipografia e tamanho

- Titulos: Montserrat
- Texto de apoio e corpo: Inter

Escala sugerida:
- Titulo principal: 30px a 34px
- Titulo secundario: 24px a 26px
- Corpo: 12px a 13px
- Meta/label: 10px a 12px

## 5. Estrutura obrigatoria dos slides

Todo slide deve seguir esta base:
1. Linha superior dourada (4px)
2. Conteudo principal (kicker + titulo + texto)
3. Bloco visual (foto/faixa/apoio)
4. Rodape de marca com logo e assinatura
5. Barra inferior dourada (3px)

## 6. Assinatura de marca no rodape

Nao usar @usuario isolado.

Sempre usar bloco de duas linhas:
- JA Contabilidade
- Contabilidade | Pericia | Estrategia

Padrao visual:
- Nome da marca em branco e com maior peso
- Linha de servicos menor e com cor secundaria
- Logo circular, sem distorcer

## 7. Regras para imagens e fotos

- Pode trocar fotos para nao repetir visual.
- Manter legibilidade do texto com tratamento da imagem.

Tratamento recomendado:
- grayscale entre 0.1 e 0.2
- brightness entre 0.65 e 0.9
- overlay escuro quando houver texto sobre foto

Evitar:
- imagem muito clara atras de texto claro
- textura visual poluida no fundo do paragrafo

## 8. O que pode variar sem perder identidade

Pode variar:
- tema do carrossel
- fotos
- copy
- micro detalhes decorativos

Nao pode variar:
- paleta base (escuro + dourado)
- assinatura de marca
- formato 4:5
- hierarquia serif + sans

## 9. Espacamento e area segura

- Dimensao de edicao: 432x540
- Saida final: 1080x1350
- Padding lateral recomendado: 32px a 36px
- Padding superior: 54px a 60px
- Padding inferior: 30px a 36px

Checklist de respiro:
- Nenhum texto encostando na assinatura da marca
- Lista 01/02/03 sem colidir com rodape
- CTA com distancia minima dos elementos ao redor

## 10. Padrao de arquivos e paths

- Cada carrossel deve ter sua propria pasta.
- Imagens e logo devem ficar na mesma pasta do HTML, quando possivel.
- Referenciar assets com caminho relativo direto.

Exemplo correto:
- Logo.jpeg
- pexels-minha-imagem.jpg

Evitar:
- prefixo uploads/ quando a pasta nao existe
- path absoluto local

## 11. Processo recomendado para novos designers

1. Duplicar um carrossel base ja aprovado.
2. Trocar copy e imagens.
3. Preservar assinatura de marca e estrutura.
4. Validar checklist visual.
5. Exportar PNG 1080x1350.

## 12. Exportacao de PNG

Quando houver comando de export na pasta do carrossel:
- usar ./export para gerar os slides automaticamente

Resultado esperado:
- slide-01.png
- slide-02.png
- slide-03.png
- todos em 1080x1350

## 13. Checklist final antes de publicar

- [ ] Marca esta no padrao (nome + linha de servicos)
- [ ] Contraste esta legivel no celular
- [ ] Nao ha colisao de texto com rodape
- [ ] Barra inferior de progresso esta coerente
- [ ] Arquivos exportados em 1080x1350
- [ ] Ortografia e acentuacao revisadas

## 14. Referencias no projeto

- Carossel BSM E CSM IMpostos/design-system/README.md
- Carossel BSM E CSM IMpostos/design-system/tokens.css
- Carossel BSM E CSM IMpostos/COMANDO_EXPORT.md

---

Se um novo layout fugir dessas regras, ele deve ser justificado antes de aprovacao final.
