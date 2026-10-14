---
name: responder-avaliacoes
description: "Use when: rascunhar resposta para avaliação do Google, review de cliente ou pedir /responder-avaliacoes."
---

# Responder avaliações

Gera rascunhos; nunca publica.

## Contexto

Ler todos os arquivos de `00-contexto/` e `_memoria/preferencias.md`.

## Fluxo

1. Extrair primeiro nome, nota e conteúdo da avaliação.
2. Para quatro ou cinco estrelas:
   - agradecer;
   - mencionar um ponto concreto da avaliação;
   - responder em uma ou duas frases;
   - usar no máximo um emoji e somente se combinar com o tom.
3. Para três estrelas ou menos:
   - não responder automaticamente;
   - apresentar análise do risco;
   - pedir orientação sobre fatos e canal de resolução;
   - produzir versão cuidadosa após confirmação.
4. Entregar em formato pronto para copiar.

## Regras

- Não inventar contexto ou providência.
- Não expor dados de cliente.
- Não admitir responsabilidade jurídica sem orientação.
- Não repetir respostas idênticas.
- Pode usar Google Business, API, navegador ou script quando configurado, mas publicar cada resposta exige OK explícito do Octavio.
- Salvar histórico somente se solicitado e em destino aprovado de `02-marketing/`.
- Nunca fazer push, criar remoto ou enviar conteúdo ao GitHub.
- Tokens ficam somente em variáveis de ambiente ou `.env` ignorado.
