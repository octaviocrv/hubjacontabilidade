# Hub JA Contabilidade e Perícias

Hub único de contexto, identidade e marketing da JA. Antes de produzir qualquer peça, leia todos os documentos de [`00-contexto/`](00-contexto/).

- Identidade e assets: [`01-identidade/`](01-identidade/)
- Acervo de marketing: [`02-marketing/`](02-marketing/)
- Edição de vídeo e IA: [`03-edicao-ia/`](03-edicao-ia/)
- Sites independentes: [`04-projetos/`](04-projetos/)
- Memória operacional: [`_memoria/`](_memoria/)
- Workflows locais adaptados: [`.claude/skills/`](.claude/skills/)
- Itens não classificados: [`99-arquivo/`](99-arquivo/)

As regras de trabalho estão em [`CLAUDE.md`](CLAUDE.md). Os projetos em `04-projetos/` têm Git e deploy próprios; não são versionados pelo Git deste hub.

As skills foram adaptadas seletivamente do MazyOS. Este hub não inclui workflows de instalação, push ou publicação automática.

Fonte: inventário do hub e briefing do Octavio, 2026-10-14.

## MazyOS ampliado

O MazyOS complementa o hub com memória, skills e referências operacionais. A integração pode usar dependências locais, Playwright, Node, pesquisa web e APIs externas, mas:

- nunca faz push nem cria ou altera remotos;
- nunca executa Git dentro de `04-projetos/`;
- pede aprovação explícita antes de publicar cada peça;
- mantém segredos somente em variáveis de ambiente ou `.env` ignorado;
- sempre lê `00-contexto/` e segue a identidade da JA.

Fonte: política MazyOS vigente em `CLAUDE.md`, 2026-10-14.

Referências operacionais:

- [`00-contexto/operacao-mazyos.md`](00-contexto/operacao-mazyos.md): mapeamento de dados, scripts, templates, saídas e publicação.
- [`00-contexto/referencias/mazyos/catalogo-skills.md`](00-contexto/referencias/mazyos/catalogo-skills.md): skills disponíveis.
- [`00-contexto/referencias/mazyos/catalogo-ferramentas.md`](00-contexto/referencias/mazyos/catalogo-ferramentas.md): ferramentas e integrações permitidas.
