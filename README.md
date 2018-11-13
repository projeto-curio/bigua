
<img alt="Bingua_Projeto_Curio" width="400" align="left" src="https://raw.githubusercontent.com/AliferSales/bigua/master/imagens/bigua.jpg" />

# Biguá

> Oi! Sou o Biguá ;) Eu me alimento de dados e para consegui-los, mergulho no mar das APIs para capturá-los. O Curió é meu primo distante e me convidou pra essa missão de disponibilizar os dados do Brasil, meu país natal, de forma acessível e clara para que todos possam conhecer melhor as atividades das nossas instituições. Óbvio que aceitei! ajudar nessa missão e ainda sair de barriga cheia de dados, quem não quer?!

Este é o repositório em que fazemos as capturas para alimentar o banco de dados do [Projeto Curió](https://github.com/projeto-curio). Abaixo, listamos as capturas que já estão sendo realizadas:

### Versão 1 da API da Câmara
- Proposições
- Deputados
- Partidos
- Votações

# Faça você mesmo

Para montar o ambiente e capturas no seu computador faça os seguinte:

1. Forke o projeto
2. Clone para seu computador
3. Rode `make prepare` - tem que ter docker instalado
4. Crie um arquivo chamado `dbconfig.txt` com a conexão para seu Postgre dentro
de `bigua`. 
Por exemplo, 
`postgresql://<user>:<password>@<server-ip>:<port>/<db>`
5. Rode todo o conteudo do que existe em `bigua/Model` em ordem.
6. No arquivo `Makefile` tem uma série de comandos com terminação em `*-historico`.
Rode todos eles uma só vez. Tenha paciência, pode demorar alguns dias - sério -
a API da câmara é sensível.
7. Agora, rode `cat crontab.txt | crontab -` para ativar o crontab e pronto!

### Desenvolva

Agora, se quiser fazer capturas, escreva um issue. Podemos dar acesso direto à 
base de dados. Assim, conseguirá colocar seu código em produção.

O processo de captura é bem simples e repetitivo. Em breve escreverei um 
tutorial sobre como fazer.







