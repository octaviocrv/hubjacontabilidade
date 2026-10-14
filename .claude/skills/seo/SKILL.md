---
name: seo
description: "Use when: pesquisar SEO local, palavras-chave, concorrência, Google Meu Negócio, GEO ou pedir /seo."
---

# SEO e GEO da JA

Produz pesquisa e recomendações; nunca modifica o site ou plataformas.

## Contexto

Ler `00-contexto/`, `_memoria/` e, somente para referência, o conteúdo textual de `04-projetos/landing-page/`.

## Escopo

Pode executar um ou mais módulos:

1. Demanda e intenção de busca.
2. Concorrência local.
3. Google Business Profile.
4. Recomendações on-page.
5. Estratégia de conteúdo.
6. Briefing para Google Ads.
7. Monitoramento.
8. GEO e respostas de IA.

## Fluxo

1. Confirmar módulo, região, serviço e objetivo.
2. Mostrar as consultas externas planejadas.
3. Pedir aprovação antes de qualquer WebSearch/WebFetch.
4. Citar URL, data de acesso e separar evidência de estimativa.
5. Salvar somente após aprovação em `02-marketing/seo/`, com arquivo numerado por módulo.
6. Para alterações no site, mostrar o patch proposto e editar `04-projetos/landing-page/` somente após aprovação específica, sem executar Git no repo.

## Regras

- Não inventar volume, CPC, posição ou concorrente.
- Pode acessar painel, Search Console, Ads, Perfil da Empresa, API, MCP ou script quando houver credenciais e finalidade aprovada.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Publicação exige OK explícito do Octavio para cada alteração.
- Tokens ficam somente em variáveis de ambiente ou `.env` ignorado.
- Dados tributários usados em conteúdo devem ter fonte oficial e data.
