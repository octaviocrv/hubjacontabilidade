# Catálogo de ferramentas permitidas

Ferramentas são possibilidades, não dependências automáticas. Configurar somente quando uma demanda real justificar.

## Render e mídia

- **Playwright/Node:** render de HTML para PNG e validação visual.
- **ffmpeg/ffprobe:** vídeo, áudio, frames e metadados.
- **Python:** análise e automação local.

## Pesquisa

- **WebSearch/WebFetch:** pesquisa e leitura de fontes públicas.
- Registrar URL e data de acesso em pesquisa de SEO ou conteúdo regulatório.

## Imagem

- **OpenAI ou Gemini:** geração de imagens quando o Octavio aprovar o conceito e a chamada externa.
- Nunca enviar imagem ou dado confidencial de cliente sem autorização.

## Publicação

- **Meta Graph API:** Instagram e Facebook, com OK explícito por peça e canal.
- **Deploy por API/CLI sem GitHub:** permitido se configurado e aprovado.
- Deploy dependente de push deve parar no pacote local.

## Plataformas e MCPs

Podem ser configurados conforme necessidade:

- Google Ads e Meta Ads;
- Google Business Profile;
- Gmail e Calendar;
- Canva;
- Notion;
- N8N;
- armazenamento e bancos de dados.

## Segredos

- Usar variáveis de ambiente ou `.env` ignorado.
- Nunca incluir token em Markdown, script, log rastreado ou commit.
- Antes da primeira chamada, listar serviço, dados enviados e efeito esperado.

## Proibição única de transporte Git

Nenhuma ferramenta pode executar push, criar remoto, usar `gh repo create` ou enviar conteúdo ao GitHub.

Fonte: `templates/ferramentas/catalogo.md` e `scripts/README.md` do MazyOS, adaptados às regras da JA.
