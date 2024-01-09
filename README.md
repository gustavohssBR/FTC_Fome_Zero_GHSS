# 1. Problema de negócio
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas

Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados! A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas é também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
 
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

### Geral	
1. Quantos restaurantes únicos estão registrados?
 2. Quantos países únicos estão registrados? 
3. Quantas cidades únicas estão registradas? 
4. Qual o total de avaliações feitas?
 5. Qual o total de tipos de culinária registrados?. 


### Pais.
1. Qual o nome do país que possui mais cidades registradas?
 2. Qual o nome do país que possui mais restaurantes registrados? 
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
 4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
 5. Qual o nome do país que possui a maior quantidade de avaliações feitas? 
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
 7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas? 
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada? 
9. Qual o nome do país que possui, na média, a maior nota média registrada? 
10. Qual o nome do país que possui, na média, a menor nota média registrada? 
11. Qual a média de preço de um prato para dois por país? 

### cidade
1. Qual o nome da cidade que possui mais restaurantes registrados? 
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4? 
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5? 
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
 7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
 8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

### Restaurantes 
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
 2. Qual o nome do restaurante com a maior nota média?
 3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas? 
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
 5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
 6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
 7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
 8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)? 

### culinária
 1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
 2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
 3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação? 
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação? 
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação? 
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
 7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação? 
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
 9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação? 
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
 11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média? 
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas? 

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez.
    O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.
 Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.
 Como é o seu primeiro trabalho, o CEO indicou um Cientista de Dados pleno para te ajudar. Ele observou os dados e te ajudou criando duas funções: 
1. Para colocar o nome dos países com base no código de cada país 
2. Criar a categoria do tipo de comida com base no range de valores. 
3. Criar o nome das cores com base nos códigos de cores 
4. Para renomear as colunas do DataFrame 


O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibem essas métricas da melhor forma possível para o CEO. 

# 2. Premissas assumidas para a análise 
* 1. A análise foi realizada em 15 Países e 125 Cidades.
* 2. Marketplace foi o modelo de negócio assumido.
* 3. As 3 principais visões do negócio foram: Visão Geral, Visão Restaurante, Visão Cidade e Visão Culinária.


# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões e uma Visão Geral do modelo de negócio da empresa: 

1. Visão Geral
2. Visão do restaurantes 
3. Visão da Cidades 
4. Visão Culinária
Cada visão é representada pelo seguinte conjunto de métricas.

### 1. Visão Geral
* a. a métrica de quantidade de entregadores. 
* b. a métrica da quantidade de Países.
* c. a métrica de quantidade de cidade. 
* d. a métrica da quantidade de avaliações. 
* e. a métrica de quantidade de culinárias.
* f. Um mapa com a localização dos restaurantes e algumas informações básicas dos restaurantes. 


### 2. Visão dos restaurantes. 
* a. Quantidade de avaliações total. 
  * 1.Fazem pedidos online / Não fazem pedidos online.
  * 2.disponibilidade nas mesas / Não tem disponibilidade nas mesas
  * 3.está entregando agora / Não está entregando agora 
* b. o custo para duas pessoas em total dollar
  * 1.Fazem pedidos online / Não faz pedidos online
  * 2.disponibilidade nas mesas / Não tem disponibilidade nas mesas
  * 3.está entregando agora / Não está entregando agora 
* c. Os restaurantes com as maiores avaliações e com o valor médio para duas   pessoas em dollar. 
* d. Os Restaurantes com a maior quantidade de votos. 
* e. Os restaurantes com o maior valor médio para duas pessoas em dollar. 
* f. Os Países que têm mais Restaurante.
* g. Restaurantes com o nível de preço menor que 2.5 com a melhor avaliação e o País.

### 3. Visão das Cidades.
* a.Top 10 cidade com mais restaurantes.
* b. Top 10 cidade com mais tipos de culinárias.
* c. Top 7 cidades com mais restaurantes com média de avaliações acima de 4.
* d. Top 7 cidades com mais restaurantes com média de avaliações abaixo de 2.5.
* e. cidade com as culinárias mais caras.
* f. cidade com as culinárias mais baratas.

### 4. Visão das culinárias.
* a. Melhores Restaurantes dos Principais tipos Culinários.
* b. Top 10 Restaurantes
* c. Top 10 Restaurantes em um mapa.
* d. Top 10 Melhores tipos de Culinárias.
* e. Top 10 piores tipos de culinárias.

# 4. Top 3 Insights de dados
1. A Índia mesmo tendo 3111 restaurantes e os Estados Unidos tendo 1374 os os Estados Unidos rende 2.8 vezes a mais que a Índia esses são os dois  países que  mais tem restaurantes.
2. Os Restaurantes que Não fazem pedidos online rende 8 vezes a mais que os Restaurantes que faz pedidos onlines 
3. O Restaurante Domino 's Pizza teve 59.749 mil votos e a média das avaliações é de 3.7 e o Restaurante AB ́ s Absolute Barbeque teve 58.875 mil votos e a média das avaliações é de 4.8 e o Restaurante Barbeque Nation teve 53.200 mil e a média das avaliações e de 4.6 e o restaurante  Barbeque Nation fica em segundo lugar do que mais rende e o Domino´s fica em terceiro e o AB ́ s Absolute Barbeque nao aparece nem entre os top 10 .
   
# 5. O produto final do projeto
 Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. 
O painel pode ser acessado através desse link: https://ftc-fome-zero-ghss.streamlit.app/

# 6. Conclusão 
O objetivo desse projeto é criar um conjunto de gráficos, mapas e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO. 
Da visão da Restaurantes, podemos concluir que os Restaurantes que está entregando agora rendem 16 vezes mais que não está entregando agora.

7. Próximo passos
Reduzir o número de métricas.
Criar novos filtros.
Adicionar novas visões de negócio.  
