# Integrações e renderizadores

Destino para novas integrações de mídia compartilhadas pelo hub, como Playwright, Node, ffmpeg e Python.

## Regras

- Reusar o pipeline existente antes de criar ferramenta nova.
- Listar dependências e comandos antes da primeira instalação ou execução.
- Instalar dependências na raiz do hub; nunca dentro de `04-projetos/`.
- Manter entradas e saídas explícitas.
- Não sobrescrever render anterior.
- Não incluir segredo em código ou log.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.

Os scripts existentes permanecem em seus caminhos atuais em `03-edicao-ia/`; esta pasta é destinada apenas a integrações futuras compartilhadas.
