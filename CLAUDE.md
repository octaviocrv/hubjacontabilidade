# JA Contabilidade e Perícias — regras do projeto

Este repositório é o hub único de contexto, identidade e marketing da JA. Os repositórios em `04-projetos/` continuam independentes e são apenas referências de leitura para este hub.

## Mapa

- `00-contexto/`: fonte operacional para marca, design, tom, carrosséis, banners, vídeos e briefing.
- `01-identidade/`: cópias canônicas de logos e fontes já existentes no acervo. `canva/` e `referencias-visuais/` aguardam material confirmado.
- `02-marketing/`: carrosséis, posts, destaques e referências de vídeo.
- `03-edicao-ia/`: originais, transcrições, planos, assets, legendas, renderizados e processo de edição.
- `04-projetos/landing-page/`: site institucional; repositório Git independente e fonte de verdade para textos e cores.
- `04-projetos/link-direciona/`: link hub; repositório Git independente.
- `04-projetos/landing-page-duplicada/`: cópia Git independente da landing encontrada no inventário; não confundir com a fonte principal.
- `_memoria/`: síntese operacional do negócio, preferências permanentes e foco atual. Não substitui as fontes detalhadas de `00-contexto/`.
- `.claude/skills/`: workflows locais adaptados do MazyOS para a JA.
- `99-arquivo/`: itens não classificados, diagnósticos e estruturas preservadas.

Fonte do mapa: inventário do hub em 2026-10-14 e `.gitignore`.

## Regras invioláveis

1. Antes de criar qualquer peça — carrossel, banner, vídeo, post, texto ou página — leia **todos** os arquivos de `00-contexto/`.
2. Siga os padrões documentados. Não invente cor, fonte, layout ou tom. Se faltar informação, pergunte.
3. Os textos e as cores de `04-projetos/landing-page/` são a fonte de verdade.
4. O código em `04-projetos/` é referência de leitura. Alterações nesses projetos são commitadas dentro de cada repositório, nunca pelo Git do hub.
5. Nunca fazer push e nunca rodar testes, linters, builds ou instalações; Octavio valida e faz push.
6. Trabalhar sempre em branch na própria pasta, nunca com `git worktree`. Commitar somente no Git do hub no formato `HUBJA - (tema feito e modificado)`, um commit por etapa concluída, não por arquivo. O merge na `main` é do Octavio.
7. Ao terminar uma peça nova aprovada, oferecer adicioná-la como exemplo na pasta e no `.md` correspondente.
8. Nunca executar `git add`, `git commit` ou outro comando que altere o estado dos repositórios em `04-projetos/`.
9. Não apagar arquivos. O que não puder ser classificado vai para `99-arquivo/`.
10. O que não estiver comprovado pelos arquivos deve permanecer como `[PREENCHER]`.
11. Skills podem criar rascunhos e arquivos locais, mas nunca publicar, enviar, instalar dependências, executar scripts ou chamar API externa sem pedido e aprovação explícitos.
12. Nenhuma skill pode executar `git push`, criar ou trocar remotos, atuar na `main`, ou alterar o estado Git de `04-projetos/`.
13. Toda entrega de marketing começa como rascunho. Octavio revisa e realiza a publicação manualmente.

Fonte das regras: briefing do Octavio, 2026-10-14.

## Uso das skills locais

Antes de usar uma skill em `.claude/skills/`:

1. Ler todos os arquivos de `00-contexto/` e os arquivos preenchidos de `_memoria/`.
2. Tratar `00-contexto/` e o site principal como fontes de verdade quando houver divergência.
3. Mostrar texto, estrutura ou plano antes de criar a entrega final.
4. Salvar materiais nos caminhos numerados já existentes; não criar `marketing/`, `identidade/`, `site/`, `dados/` ou `saidas/` paralelos.
5. Não usar defaults visuais do MazyOS. A identidade da JA sempre prevalece.

As skills `/instalar`, `/salvar` e `/aprovar-post` não fazem parte deste hub por serem incompatíveis com as regras acima.

Fonte: integração seletiva do MazyOS aprovada pelo Octavio em 2026-10-14.
