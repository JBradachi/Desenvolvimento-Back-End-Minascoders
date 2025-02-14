# Desenvolvimento-Back-End-Minascoders

Repositório dedicado a prova de conceito do Back-End do site do minascoders

## Descrição das tarefas

Iremos criar 3 paginas

### Notícias

Que irá conter uma lista de notícias (mesmo do dever de casa passado)
data da notícia, titulo resumo
imagem?

link pra voltar pra pagina inicial

### Pagina inicial

manter o que já havia pedido (patrocinadores[colocar link])
contendo uma lista de participantes do projeto de vocês;
fotinhas
link para a pagina de notícia e dashboard

### Dashboard

link pra voltar pra pagina inicial

login simplificado
inserir e remover notícias
inserir e remover participantes

remoção: mostrar no site os titulos das notícias/ nome dos participantes
e remover tudo a partir disso.

localhost:5000/Dashboard/
opção de modificar aba de notícia ou pagina inicial

localhost:5000/Dashboard/Noticia
botoes: inserir / remover

localhost:5000/Dashboard/Noticia/Inserir

localhost:5000/Dashboard/Noticia/Remover

localhost:5000/Dashboard/MainPage/
inserir participante
inserir patrocinador
remover participante
remover patrocinador

### Banco de dados

tabelas:

- noticia
  - titulo
  - data de publicação
  - resumo da notícia
  - outras colunas relevantes (autor, )
  - imagem? (caminho da imagem)
  
- patrocinadores
  - nome
  - nivel
  - link pro site
  - imagem? (caminho da imagem)

- participantes
  - nome
  - imagem? (caminho da imagem)
  - email
  - link pro github

### EXTRA

Dockerizar tudo

### Divisão

- Aba notícias [Rafaella]
- Aba Home [Ingred]
- Dashboard/notícias [Pamela]
- Dashboard/home [Bradas]
- criação do banco [Rafaella]
- dockerizar [Bradas]
