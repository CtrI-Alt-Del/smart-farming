<div align="center">
  <img src="./src/ui/static/images/logo.svg" alt="Smart Farming" width="500" height="200" />
</div>

---

## Visão geral do produto 🖥️

Smart Farming é um site web que visa facilitar o trabalho de monitoramento da estufa inteligente de mesmo nome mantida dentro da [FATEC de São José dos Campos](https://fatecsjc-prd.azurewebsites.net/). 

A aplicação permite fazer o gerenciamento (adição, edição e deleção) dos dados coletados pela estufa, assim como apresenta um dashboard interativo, onde é possível verificar a evolução desses valores ao longo do tempo por meio de gráficos.

---

## Tecnologias 🛠️

<div align="center">
  <table>
  <tr>
    <td align="center" width="96">
      <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML">
        <img src="documentation/images/html5.svg" width="48" height="48" alt="HTML" />
      </a>
      <span>HTML</span>
    </td>
    <td align="center" width="96">
      <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/CSS">
        <img src="documentation/images/css3.svg" width="48" height="48" alt="CSS" />
      </a>
      <span>CSS</span>
    </td>
    <td align="center" width="96">
      <a target="_blank" href="https://www.figma.com/">
        <img src="documentation/images/figma.svg" width="48" height="48" alt="Figma" />
      </a>
      <span>Figma</span>
    </td>
    <td align="center" width="96">
      <a target="_blank" href="https://tailwindcss.com/">
        <img src="documentation/images/tailwindcss.jpg" width="48" height="48" alt="TypeScript" />
      </a>
      <span>TailwindCSS</span>
    </td>
    </td>
    <td align="center" width="96">
      <a target="_blank" href="https://apexcharts.com/">
        <img src="documentation/images/apexcharts.jpeg" width="48" height="48" alt="ApexCharts" />
      </a>
      <span>ApexCharts</span>
    <tr/>
    <tr>
    </td>
    <td align="center" width="96">
      <a target="_blank" href="https://www.python.org/">
        <img src="documentation/images/python.svg" width="48" height="48" alt="Python" />
      </a>
      <span>Python</span>
     </td>
    <td align="center" width="96">
      <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
        <img src="documentation/images/javascript.svg" width="48" height="48" alt="JavaScript" />
      </a>
      <span>JavaScript</span>
    </td>
      <td align="center" width="96">
      <a href="https://www.mysql.com/">
      <img src="documentation/images/mysql.png" width="48" height="48" alt="MySQL" />
      </a>
      <span>MySQL</span>
      </td>
    <td align="center" width="96">
      <a target="_blank" href="https://flask.palletsprojects.com/en/3.0.x/">
        <img src="documentation/images/flask.svg" width="48" height="48" alt="Flask"/>
      </a>
      <span>Flask</span>
    </td>
    <td align="center" width="96">
      <a target="_blank" href="https://www.docker.com/">
        <img src="documentation/images/docker.svg" width="48" height="48" alt="Docker" />
      </a>
      <span>Docker</span>
    </td>
  </tr>
</table>
</div>

---

## Problema do cliente 👔

Atualmente a estufa é monitorada de maneira arcaica utilizando-se primariamente de [arquivos do tipo CSV](https://www.freecodecamp.org/portuguese/news/o-que-e-um-arquivo-csv-e-como-abrir-esse-formato-de-arquivo/) para registrar e armazenar informações a partir dos dados coletados pelos sensores da estufa, assim como as informações obtidas de um [Google Forms](https://workspace.google.com/intl/pt-BR/lp/forms/?utm_source=google&utm_medium=cpc&utm_campaign=latam-BR-all-pt-dr-bkws-all-all-trial-e-dr-1707806-LUAC0011908&utm_content=text-ad-none-any-DEV_c-CRE_666246535618-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt-Forms-KWID_43700057676889044-kwd-10647024857&utm_term=KW_google%20forms-ST_google%20forms&gad_source=1&gclid=Cj0KCQjw2uiwBhCXARIsACMvIU0RToV-UJaKbeTi82kzMxsMZeYaZnjOi5IE7GjyBO431c9fjzVq1v8aAtrFEALw_wcB&gclsrc=aw.ds) para realizar o check-list, isto é, uma lista de itens que servem para validar os dados obtidos por esses sensores.

Os dados colhidos pelos sensores são armazenados em um cartão *microSD*. Para fazer o registro desses dados em um arquivo CSV é preciso retirar o cartão, o que acaba não se tornando prático e até perigoso em virtude da fragilidade dessa peça. Para evitar isso, atualmente o cliente converte os dados contidos nesse cartão em um único arquivo CSV de forma automatizada, porém o backup desse arquivo acaba utilizando espaço de armazenamento desnecessário. Além disso, para verificar que esses dados estão de fato sendo registrados, o cliente necessita ficar fisicamente presente dentro da FATEC, o que nem sempre é possível.

Para fazer a análise de dados a fim de obter *insights* e reduzir potenciais problemas com relação ao andamento da estufa são constrúidos gráficos no *Excel* a partir dos arquivos CSV, porém não são tão interativos e são de difícil manutenção.

---

## Objetivo do produto 🎯

Posto o problema do cliente analisado, cabe a aplicação registrar esses dados de forma automatizada e exibi-las, tanto em forma de tabela, quanto de gráfico, bem como ter as funcionalidades de adicionar, editar e deletar esses registros, em que apenas um usuário com permissão (administrador) poderá fazer esse tipo de gerenciamento, bastando apenas que ele acesse o sitema via e-mail e senha. Além disso, o site em questão deve ser acessível em qualquer lugar e aberto a todo público, como também ressaltar o andamento da estufa com base nos dados que venham a ser cadastrados no sistema. 

---

## Metodologia empregada 💡

Para a confecção do produto foi empregado o framework de [metodologia ágil Scrum](https://aws.amazon.com/pt/what-is/scrum/#:~:text=O%20Scrum%20%C3%A9%20um%20framework,uma%20entrega%20eficiente%20de%20projetos.), que consiste sumariamente dividir o desenvolvimento do projeto em Sprints, um conjunto de tarefas que devem ser executadas e desenvolvidas em um período pré-definido de tempo. Além disso, foi definido o Backlog do Produto, que são todas as funcionalidades que o software deverá ter com base nos requisitos levantados com o cliente. Uma vez aprovado por ele, para selecionar quais seriam as entregas das Sprints do projeto, primeiro foi definido o [MVP](https://rockcontent.com/br/blog/o-que-e-mvp/) de cada Sprint, que é uma versão do produto que prioriza as tarefas que trazem maior entrega de valor para o cliente. Então, a partir disso o Backlog do Produto foi dividido em 4 Backlog de Sprint.

---

## MVP'S 🏆

### Sprint - 1️⃣

https://github.com/CtrI-Alt-Del/smart-farming/assets/64440486/bfb05046-668f-4b10-84f6-30c98dae20db

### Sprint - 2️⃣

`🚧 Em desenvolvimento 🚧`

### Sprint - 3️⃣

`🚧 Em desenvolvimento 🚧`

### Sprint - 4️⃣

`🚧 Em desenvolvimento 🚧`

---

## Backlog do produto 📖

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
      <td>Como administrador, quero fazer o upload de dados coletados pelos sensores contidos em um arquivo CSV para armazená-los no sistema.</td>
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
      <td>Como administrador, quero fazer o upload de dados de check-list contidos em um arquivo CSV no sistema para armazená-los de forma mais segura.</td>
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
      <td>Como administrador, quero poder fazer o cadastro de dados de check-list via formulário para mantê-los salvos dentro do sistema.</td>
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
      <td>Como mantenedor da estufa, quero que haja um usuário administrador pré-cadastrado para gerenciar o sistema para que nem todos os usuários que venham a acessar o site possam adicionar, editar ou deletar os dados cadastrados.</td>
      <td>ALTA</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Edição de registros.</td>
      <td>Como administrador, quero poder editar as informações de um registro para corrigir eventuais erros de cadastro.</td>
      <td>ALTA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Login.</td>
      <td>Como administrador, quero que haja a funcionalidade de login via e-mail e senha para que apenas eu possa acessar os recursos do sistema que estão disponíveis para o usuário administrador.</td>
      <td>ALTA</td>
      <td>8</td>
    </tr>
     <tr>
      <td>Listagem de plantas.</td>
      <td>Como mantenedor da estufa, quero poder ver todas as plantas cadastrados no sistema.</td>
      <td>ALTA</td>
      <td>2</td>
    </tr>
     <tr>
      <td>Cadastro de plantas.</td>
      <td>Como administrador, quero poder cadastrar uma planta para que eu possa associá-la a um registro de check-list ou um registro (dos sensores ou check-list).</td>
      <td>ALTA</td>
      <td>2</td>
    </tr>
     <tr>
      <td>Edição de planta.</td>
      <td>Como administrador, quero poder editar o nome de uma planta para que eu corrija enventuais erros de digitação.</td>
      <td>ALTA</td>
      <td>2</td>
    </tr>
     <tr>
      <td>Filtragem de dados nos gráficos dos dados coletados pelos sensores por período de dias.</td>
      <td>Como mantenedor da estufa, quero poder filtrar
os dados dos sensores exibidos pelos gráficos para determinados períodos de dias a fim de que eu possa acompanhar a evolução desses valores em diferentes faixas de tempo.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
     <tr>
      <td>Filtragem de dados nos gráficos dos dados de check-list por período de dias.</td>
      <td>Como mantenedor da estufa, quero poder filtrar
os dados de checklist exibidos pelos gráficos para determinados períodos de dias a fim de que eu possa acompanhar a evolução desses valores em diferentes faixas de tempo.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Filtragem de registros nas tabelas por datas.</td>
      <td>Como mantenedor da estufa, quero pode filtrar registros exibidos nas tabelas por período compreendido entre duas datas.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Paginação de registros.</td>
      <td>
      Como administrador, quero que as tabelas possuem páginas onde cada página tenha no máximo 20 registros a fim de que nem todos os registros cadastrados nos sistema sejam exibidos para mim.
      </td>
      <td>MÉDIA</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Mensagens de alerta.</td>
      <td>Como administrador, quero poder se avisado que estou fazendo uma ação que pode afetar o sistema como um todo, como uma deleção de um registro, por exemplo, para eu não cometer equívocos e ter certeza do que eu estou fazendo.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Redefinição de senha.</td>
      <td>Como administrador, quero poder recuperar minha senha caso eu a esqueça para que eu não perca acesso total ao sistema.</td>
      <td>MÉDIA</td>
      <td>8</td>
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
      <td>3</td>
    </tr>
    <tr>
      <td>Cadastro de planta.</td>
      <td>Como administrador quero poder cadastrar uma planta para associá-la a um registro referente aos dados coletados pelos sensores para então o mantenedor da estufa saber quais registros são associados a quais plantas.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Cálculo de média dos dados coletados pelos sensores.</td>
      <td>Como mantenedor da estufa, quero que o sistema calcule a média de cada dado coletado pelo sensores ao longo do tempo para que eu possa identificar padrões ou realizar previsões a respeito desses valores.</td>
      <td>MÉDIA</td>
      <td>5</td>
    </tr>
     <tr>
      <td>Exportação de dados dos registros para arquivo CSV.</td>
      <td>Como administrador, quero poder exportar os dados dos registros (dos sensores ou check-list) para um arquivo CSV para que eu possa utilizar essa base de dados para outros fins como migração de dados para outro sistema, por exemplo.</td>
      <td>BAIXA</td>
      <td>2</td>
    </tr>
     <tr>
      <td>Backup automatizado dos dados de registros.</td>
      <td>Como mantenedor da estufa, quero que o sistema faça backup dos registros (dos sensores ou check-list) para que esses valores sejam recuperados em caso de eventual perda.</td>
      <td>BAIXA</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Exibição do último registro coletado pelos sensores.</td>
      <td>Como mantenedor da estufa, quero poder ver o último registro coletado pelos sensores para que eu tenha noção do estado atual da estufa.</td>
      <td>BAIXA</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Cadastro de dados coletados pelos sensores via formulário.</td>
      <td>Como administrador, quero poder fazer o cadastro de dados no sistema por meio de um formulário, com o objetivo de fazer o cadastramento de uma forma mais manual caso eu queira.</td>
      <td>BAIXA</td>
      <td>2</td>
    </tr>
     <tr>
      <td>Deleção de planta.</td>
      <td>Como administrador, quero poder deletar uma planta para que ela não fique mais registrada no sistema.</td>
      <td>BAIXA</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Persistência de sessão de login.</td>
      <td>Como administrador, quero que o sistema persista minha sessão uma vez após feito o login mesmo que o meu navegador feche para que no próximo dia eu não tenha que fazer o procedimento de login novamente.</td>
      <td>BAIXA</td>
      <td>1</td>
    </tr>
</table>

---

## Relatório e detalhes de cada Sprint 📅

- Sprint 1: [Acessar](https://github.com/CtrI-Alt-Del/smart-farming/blob/main/documentation/reports/sprint-1.md)

- Sprint 2: [Acessar](https://github.com/CtrI-Alt-Del/smart-farming/blob/main/documentation/reports/sprint-2.md)

- Sprint 3: [Acessar](https://github.com/CtrI-Alt-Del/smart-farming/blob/main/documentation/reports/sprint-3.md)

- Sprint 4: [Acessar](https://github.com/CtrI-Alt-Del/smart-farming/blob/main/documentation/reports/sprint-4.md)

## Como usar a aplicação? 🚀

### 🔧 Pré requisitos

- [Docker](https://www.docker.com/products/docker-desktop/) a incrivel tecnologia de gerenciar [containers](https://www.docker.com/resources/what-container/).
- [Git](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git) Para você conseguir clonar nosso repositório.
- [VSCode](https://code.visualstudio.com/) Pois as extensões dele são vitais


> Também é crucial definir as variáveis de ambiente no arquivo .env antes de executar a aplicação. Veja o arquivo [.env.example](https://github.com/CtrI-Alt-Del/smart-farming/blob/main/.env.example) para saber quais variáveis devem ser definidas

### Usando a aplicação 📟
- Abra o Git Bash previamente instaldo
```bash

# Clone esse repositório
$ git clone https://github.com/CtrI-Alt-Del/smart-farming.git.
```
- Abra o terminal no diretorio no qual você clonou o repositório
```bash
# Abra a pasta do arquivo
$ cd /smart-farming

# Abra o arquivo com o VSCode
$ code .
```

- Abra a aba de extensões no VSCode
- Baixe a extensão [Database Client](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-database-client2) do Vscode 
- Abra a extensao Database Client no VSCode e insira os dados da sua rede
- Abra o terminal
```bash
# Execute o container
$ docker compose up

```
> Provavelmente a aplicação estará sendo executada em http://127.0.0.1:5000
> Provavelmente a aplicação estará sendo executada em http://127.0.0.1:5000

---

## Time de Desenvolvimento 👷🏻

| Foto | Nome | Função | Github | Linkedin |
| :---------: | :---------: | :---------------------: | :-----------------: | :-------: |
| <img src="https://github.com/JohnPetros.png?size=50" width=50px> | Joao Pedro Carvalho | Product Owner | <a href="https://github.com/JohnPetros"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/jo%C3%A3o-pedro-carvalho-dos-santos-42a0ab222/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="https://github.com/kaufon.png?size=50" width=50px> | Kauan Fonseca do Vale | Scrum Master | <a href="https://github.com/kaufon"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/kauan-fonseca-b62188300/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="https://github.com/0thigs.png?size=50" width=50px> | Thiago Martins | Scrum Team | <a href="https://github.com/0thigs"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/desenvolvedor-frontend/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="https://github.com/FaelSantoss.png?size=50" width=50px> | Rafael dos Santos | Scrum Team | <a href="https://github.com/FaelSantoss"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="https://github.com/Tico1606.png?size=50" width=50px> | Gabriel Oliveira | Scrum Team | <a href="https://github.com/Tico1606"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/gabriel-oliveira-884ba5282/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="https://github.com/JoaoGabrielGarcia.png?size=50" width=50px> | Joao Gabriel Oliveira |  Scrum Team  | <a href="https://github.com/JoaoGabrielGarcia"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/jo%C3%A3o-gabriel-oliveira-garcia-b2563a22a/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
