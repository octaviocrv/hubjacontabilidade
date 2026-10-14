# Operação MazyOS no hub JA

O MazyOS é uma camada de workflows sobre a estrutura existente. Ele não cria uma segunda organização na raiz.

## Mapeamento de pastas

| Conceito original do MazyOS | Destino na JA |
|---|---|
| `_memoria/` | `_memoria/`, como síntese; `00-contexto/` continua como fonte detalhada |
| `identidade/` | `01-identidade/` e `00-contexto/design-system.md` |
| `marketing/conteudo/` | `02-marketing/conteudo/`, `carrosseis/`, `posts/` ou `videos/`, conforme a peça |
| `marketing/seo/` | `02-marketing/seo/` |
| `marketing/campanhas/` | `02-marketing/campanhas/` |
| scripts de marketing/publicação | `02-marketing/automacoes/` |
| scripts de mídia/render | `03-edicao-ia/10-integracoes/` |
| `dados/` | `99-arquivo/entradas-para-analise/`, apenas para arquivos temporários sem destino específico |
| `saidas/` | destino específico da entrega; se ainda não houver classificação, `99-arquivo/nao-classificados/` |
| `templates/` | `00-contexto/referencias/mazyos/`, somente referências compatíveis |
| `site/` | `04-projetos/landing-page/`, repositório independente |

## Dependências

- Instalar somente quando uma tarefa concreta exigir.
- Antes de instalar, listar pacote, finalidade, comando, versão ou faixa e arquivos que serão criados.
- Instalar na raiz do hub, nunca dentro de `04-projetos/`.
- Dependências de um script devem ser registradas em manifesto na raiz ou documentadas junto da integração.

Nenhuma dependência foi instalada durante a integração, pois as skills Markdown funcionam sem runtime adicional até serem executadas.

## Scripts

- Scripts de publicação e APIs sociais ficam em `02-marketing/automacoes/`.
- Renderizadores, transcrição, composição e mídia ficam em `03-edicao-ia/10-integracoes/` ou no projeto de edição correspondente.
- Scripts nunca contêm tokens.
- O comando e seus efeitos devem ser mostrados antes da primeira execução.

## Dados e saídas

- Dados de cliente devem ser minimizados e anonimizados.
- Não versionar segredo ou arquivo confidencial sem decisão explícita.
- Relatórios de ads ficam em `02-marketing/campanhas/relatorios/`.
- Análises que atualizam a compreensão da empresa podem virar contexto, mas somente fatos aprovados entram em `_memoria/`.
- Rascunhos e arquivos sem destino confirmado permanecem em `99-arquivo/`.

## Publicação

- Preparar não significa publicar.
- Cada peça e canal exigem um OK explícito.
- Se um deploy depender de push no GitHub, a automação deve parar e entregar o pacote local.
- IDs e resultados públicos podem ser registrados; tokens e respostas sensíveis não.

## Git

- Commits locais no hub são permitidos em branch.
- Nunca executar `git push`.
- Nunca criar ou alterar remotos.
- Nunca executar Git dentro de `04-projetos/` por meio das skills do hub.

Fonte: MazyOS, commit `83ed079d1fde51b334e9ecbee5a154f4821d59fb`, adaptado às regras da JA em 2026-10-14.
