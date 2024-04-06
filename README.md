
## Visão geral do produto 🖥️

Smart Farming é um **dashboard web** que visa facilitar o trabalho de monitoramento da estufa inteligente de mesmo nome mantida dentro da [FATEC de São José dos Campos](https://fatecsjc-prd.azurewebsites.net/). 

## Problema do cliente 👔

Atualmente a estufa é monitorada de maneira arcaica utilizando-se primariamente de [arquivos do tipo CSV](https://www.freecodecamp.org/portuguese/news/o-que-e-um-arquivo-csv-e-como-abrir-esse-formato-de-arquivo/) para registrar e armazenar informações a partir dos dados coletados pelos sensores da estufa, assim como as informações obtidas de uma Form's para realizar o check-list, isto é, uma lista de itens que servem para validar os dados obtidos por esses sensores.

Os dados colhidos pelos sensores são armazenados em um cartão *microSD*. Para fazer o registro desses dados é preciso retirar o cartão, o que acaba não se tornado prático e até perigoso em virtude da fragilidade dessa peça.


## Objetivo do produto 🎯

Posto o ploblema do cliente analisado, cabe ao dashboard registrar esses dados de forma automatizada e exibí-las tanto em forma de tabela, quanto de gráfico, bem como a funcionalidade de adicionar, editar e deletar esses registros, em que apenas um usuário com permissão (administrador) poderá fazer esse tipo de gerenciamente, bastando apenas que ele acesse o sitema via e-mail e senha. 

## Metodologia empregada 💡

Para a confecção do produto foi empregado o framework de [Metodologia Ágil Scrum](https://aws.amazon.com/pt/what-is/scrum/#:~:text=O%20Scrum%20%C3%A9%20um%20framework,uma%20entrega%20eficiente%20de%20projetos.), um método ágil adaptativo, iterativo, flexível e eficaz. Entre as ferramentas utilizadas no Scrum, uma é a divisão do projeto em Sprints. Para selecionar quais seriam as entregas das nossas Sprints, primeiro foi definido o [MVP](https://rockcontent.com/br/blog/o-que-e-mvp/), que consiste em uma versão do produto que prioriza as tarefas que teazem maior entrega de valor para o cliente. Então, a partir das Tarefas foi construído o Backlog do Produto, o qual foi aprovado pelo cliente e dividido em 4 Backlog de Sprint.


## Backlog do produto 🎯

<table>
 <thead>
    <tr>
      <th>Requisito</th>
      <th>História de usuário</th>
      <th>Prioridade</th>
      <th>Estimativa</th>
    </tr>
 </thead>
 <tbody>
    <tr>
      <td>Cadastro de dados dos sensores via arquivo CSV.</td>
      <td>Como mantenedor da estufa, quero fazer o upload de dados coletados pelos sensores contidos em um arquivo CSV para armazená-los no sistema.</td>
      <td>ALTA</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Geração de gráfico dos dados de sensores.</td>
      <td>Como mantenedor da estufa, quero que o sistema gere um gráfico de linha referente os dados coletados pelos sensores com relação a um período de dias a fim de facilitar minha análise acerca do andamento da estufa ao longo do tempo.</td>
      <td>ALTA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Cadastro automatizado dos dados coletados pelos sensores.</td>
      <td>Como mantenedor da estufa, quero que o sistema consiga receber os dados inseridos no cartão microSD de forma automatizada para que eu não tenha que ficar retirando o cartão microSD para fazer o registro dos dados contidos nele.</td>
      <td>ALTA</td>
      <td>13</td>
    </tr>
    <tr>
      <td>Cadastro de dados de check-list via arquivo CSV.</td>
      <td>Como mantenedor da estufa, quero fazer o upload de dados de check-list contidos em um arquivo CSV no sistema para armazená-los de forma mais segura.</td>
      <td>ALTA</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Geração de gráficos acerca dos dados de check-list.</td>
      <td>Como mantenedor da estufa, quero que o sistema gere gráficos referente os dados de check-list com relação a um período de dias a fim de facilitar a comparação com os dados coletados pelos sensores.</td>
      <td>ALTA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Cadastro de dados de check-list via formulário.</td>
      <td>Como mantenedor da estufa, quero poder fazer o cadastro de dados de check-list via formulário para mantê-los salvo dentro do sistema.</td>
      <td>ALTA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Tabelas de registros.</td>
      <td>Como mantenedor da estufa, quero visualizar os registros tanto referente aos dados coletados pelos sensores quanto ao check-list em respectivas tabelas a fim de que eu possa visualizar esses dados de forma escrita.</td>
      <td>ALTA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Usuário administrador.</td>
      <td>Como mantenedor da estufa, quero que haja um usuário administrador para gerenciar o sistema para que nem todos os usuários que venham a acessar o site possam adicionar, editar ou deletar os dados cadastrados no sistema.</td>
      <td>ALTA</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Edição de registros.</td>
      <td>Como administrador, quero poder editar as informações de um registro usuário para corrigir eventuais erros de cadastro.</td>
      <td>ALTA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Login.</td>
      <td>Como administrador, quero que haja a funcionalidade de login de e-mail e senha para que apenas eu possa acessar os recursos do sistema que estão disponíveis para o usuário administrador.</td>
      <td>ALTA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Filtragem de registros</td>
      <td>Como mantenedor da estufa, quero pode filtrar registros exibidos nas tabelas por período compreendido entre duas datas.</td>
      <td>MÉDIA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Paginação de registros.</td>
      <td>Como administrador, quero que as tabelas possuem páginas onde cada página tenha no máximo 20 registros a fim de que nem todos os registros cadastrados nos sistema sejam exibidos para mim.</td>
      <td>MÉDIA</td>
      <td>13</td>
    </tr>
    <tr>
      <td>Mensagens de alerta.</td>
      <td>Como administrador, quero poder se avisado que estou fazendo uma ação que pode afetar o sistema como um todo, como uma deleção de um registro, por exemplo, para eu não cometer equívocos e ter certeza do que eu estou fazendo.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Redefinição de senha.</td>
      <td>Como administrador, quero que minha senha sempre esteja criptografada para aumentar a segurança de acesso ao sistema.</td>
      <td>MÉDIA</td>
      <td>13</td>
    </tr>
    <tr>
      <td>Criptografia de senha.</td>
      <td>Como administrador, quero poder filtrar os registros de modo que apenas os registros que atendam um determinado período de dias sejam visualizadas em suas respectivas tabelas.</td>
      <td>MÉDIA</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Responsividade.</td>
      <td>Como mantenedor da estufa, quero que o site seja responsivo para que eu possa usá-lo por qualquer tipo de dispositivo.</td>
      <td>MÉDIA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Mensagens de erro.</td>
      <td>Como mantenedor da estufa, quero que o sistema exiba mensagens quando alguma ação minha não for realizada com sucesso para que eu tenha consciência de fato que algo ocorreu de errado.</td>
      <td>MÉDIA</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Pré-cadastro de dados dos sensores.</td>
      <td>Como mantenedor da estufa, quero que o sistema já contenha os dados que eu já tenho para que eu precise apenas inserir dados novos.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Cadastro de planta.</td>
      <td>Como administrador quero poder cadastrar uma planta para associá-la a um registro referente aos dados coletados pelos sensores para então o mantenedor da estufa saber quais registros são associados a quais plantas.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Cálculo de médias.</td>
      <td>Como administrador quero poder cadastrar uma planta para associá-la a um registro referente aos dados coletados pelos sensores para então o mantenedor da estufa saber quais registros são associados a quais plantas.</td>
      <td>MÉDIA</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Destaque do último registro.</td>
      <td>Como mantenedor da estufa, quero visualizar a média de cada dado referente ao registros relacionados aos sensores para eu ter uma visão geral a respeito dessas informações.</td>
      <td>MÉDIA</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Cadastro de dados coletados pelos sensores via formulário.</td>
      <td>Como mantenedor da estufa, quero poder fazer o cadastro de dados no sistema por meio de um formulário, com o objetivo de fazer o cadastramento de uma forma mais manual caso eu queira.</td>
      <td>BAIXA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Persistência de sessão de login.</td>
      <td>Como administrador, quero que o sistema persista minha sessão uma vez após feito o login mesmo que o meu navegador feche para que no próximo dia eu não tenha que fazer o procedimento de login novamente.</td>
      <td>BAIXA</td>
      <td>2</td>
      </tr>

## Relatório de cada Sprint 📅

- Sprint 1: [Acessar]()

- Sprint 2: [Acessar]()

- Sprint 3: [Acessar]()

- Sprint 4: [Acessar]()
