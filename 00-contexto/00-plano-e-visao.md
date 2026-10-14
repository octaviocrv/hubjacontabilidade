# Plano e visão

## Objetivo

Manter um hub único de contexto, identidade e marketing que retroalimenta site, carrosséis, posts e vídeos. O acervo existente é a referência; novas peças devem repetir padrões comprovados, não criar uma identidade paralela.

Fonte: briefing do Octavio, 2026-10-14.

## Estrutura

| Pasta | Função |
|---|---|
| `00-contexto/` | Regras e decisões confirmadas para criação |
| `01-identidade/` | Logos e fontes canônicas já presentes no acervo |
| `02-marketing/` | Carrosséis, posts, destaques e referências |
| `03-edicao-ia/` | Pipeline completo de vídeo, do original ao render |
| `04-projetos/` | Repositórios de código independentes, somente leitura pelo hub |
| `_memoria/` | Síntese operacional e prioridades atuais; não substitui `00-contexto/` |
| `.claude/skills/` | Workflows locais adaptados, sem push ou publicação automática |
| `99-arquivo/` | Diagnósticos, itens não classificados e estruturas preservadas |

Fonte: inventário do hub em 2026-10-14; `03-edicao-ia/README.md`; integração seletiva do MazyOS aprovada em 2026-10-14.

## Relação com os projetos web

- `04-projetos/landing-page/` é o site institucional e a fonte de verdade para cores e textos. Tem Git e deploy Vercel próprios.
- `04-projetos/link-direciona/` é o link hub usado na bio do Instagram e na assinatura de e-mail. Tem Git e deploy Vercel próprios.
- `04-projetos/landing-page-duplicada/` é uma segunda cópia Git encontrada no inventário, apontando para o mesmo remoto da landing principal. Preservar até Octavio decidir seu destino.
- Nenhum desses repositórios entra em commits do hub.

Fontes: briefing do Octavio, 2026-10-14; `04-projetos/landing-page/.git/config`; `04-projetos/link-direciona/.git/config`; `.gitignore`.

## Link hub

O código atual mostra dez links visíveis na lista principal. Oito são CTAs de atendimento via WhatsApp com mensagem pré-preenchida; os outros dois levam ao site e às avaliações:

1. Agende sua Consultoria.
2. Entre em contato.
3. Nossa localização.
4. Nosso site.
5. Abertura de Empresa.
6. Regularização de MEI.
7. Planejamento Tributário.
8. Perícia Contábil.
9. Orientações IRPF.
10. Avaliações de Clientes.

Assim, a expressão “8 links principais” do briefing corresponde aos oito links de atendimento por WhatsApp, não ao total de âncoras visíveis.

Fonte: `04-projetos/link-direciona/index.html`, linhas 39–137; briefing do Octavio, 2026-10-14.

Todos os CTAs usam `553131509984`. As oito mensagens confirmadas são:

- “Olá, quero falar com a JA”
- “Olá, quero agendar uma consultoria”
- “Olá, gostaria da localização da JA”
- “Olá, quero abrir minha empresa”
- “Olá, preciso regularizar meu MEI”
- “Olá, quero saber sobre planejamento tributário”
- “Olá, preciso de perícia contábil”
- “Olá, quero receber orientações de IRPF”

Fonte: `04-projetos/link-direciona/index.html`, linhas 32–129.
