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

Fonte das regras: briefing do Octavio, 2026-10-14.
