# Automações de marketing

Destino para scripts de publicação, integrações sociais e utilitários de campanhas.

## Convenções

- Um subdiretório por integração.
- Cada integração deve ter README com entradas, saídas, dependências, variáveis exigidas e efeitos externos.
- Tokens ficam somente em variável de ambiente ou `.env` ignorado.
- Logs rastreados não podem conter credenciais ou dados pessoais.
- Toda publicação exige OK explícito do Octavio para a peça e os canais.
- Nenhum script pode fazer push, criar remoto ou enviar conteúdo ao GitHub.

## Integrações previstas

- Meta Graph API para Instagram/Facebook.
- Google Ads e relatórios.
- Deploy por API/CLI que não dependa de GitHub.

Nenhum script foi copiado do MazyOS porque o repositório de origem contém apenas documentação e espera que os scripts sejam criados conforme a integração real.
