# Comando de Exportacao PNG

Este projeto possui um comando curto para exportar os 3 slides em PNG para Instagram.

## Comando principal

No diretorio Carroseis, execute:

./export

Esse comando:
- abre cada slide em modo de exportacao (`exportSlide=1`, `2`, `3`)
- renderiza em 1080x1350 (formato 4:5)
- salva os arquivos em `Carroseis/exports/`

Arquivos gerados:
- `slide-01.png`
- `slide-02.png`
- `slide-03.png`

## Requisitos

- `google-chrome-stable` instalado
- servidor local ativo em `http://localhost:5500`

Para iniciar servidor local na raiz do projeto:

python3 -m http.server 5500

## Comando avancado

Tambem e possivel passar URL e pasta de saida:

./export "http://localhost:5500/Carroseis/Carrossel%20IBS%20e%20CBS.dc.html" "./minha-pasta"

## Script base

O comando `./export` chama internamente:

./exportar_png_instagram.sh
