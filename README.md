<h1 align="center">✨CTRL ALT DEL✨</h1>

<p align="center">An Application about our API from Fatec Sao Jose dos Campos.🚀</p>

<h3 align="center">Coming Soon!!</h3>

<h4 align="center"> 
	🚧  Space In Development  🚧
</h4>

## Backlog

### Sprint 1

#### Requisitos funcionais

- [ ] **Cadastro de dados dos sensore via arquivo CSV**

> Contexto

*Atualmente, os dados coletados coletados pelos sensores da estufa e do check-list estão armazenados em arquivos do tipo [CSV](https://www.freecodecamp.org/portuguese/news/o-que-e-um-arquivo-csv-e-como-abrir-esse-formato-de-arquivo/).*

> História de usuário

*Como mantenedor da estufa, quero fazer o upload de dados contidos nos meus arquivos CSV no sistema para armazená-los de forma mais segura.*

> Critérios de aceitação

- Mais de arquivo CSV pode ser lido de uma vez.
- O upload deve aceitar arquivos CSV tanto em formato de texto, quanto de Excel.
- O sistema deve validar os dados contidos no arquivo antes de concluir o upload, ou seja, deve haver conformidade com as colunas presentes nos arquivos CSV, assim como o tipo de dado registrado.

---

- [ ] **Cadastro de dados dos sensores via formulário**

> Contexto

*Atualmente, eu insiro de forma manual os dados coletados pela estufa.*

> História de usuário

*Como mantenedor da estufa, quero poder fazer o cadastro de dados no sistema por meio de um formulário, com o objetivo de fazer o cadastramento de uma forma mais manual caso eu queira.*

> Critérios de aceitação

- O formulário deve conter os seguintes campos:
  - Data (dd/mm/aaaa).
  - Horário (Horas:Minutos).
  - Umidade do solo (%).
  - Umidade Ambiente (%).
  - Temperatura Ambiente (°C).
  - Volume de água (ml).
- O sistema deve validar os dados vindo do formulário, ou seja, se os campos estão condizentes com os dados armazenados no cartão microSD.
- Nenhum campo pode ser nulo.

---

- [ ] **Cadastro de dados check-list via formulário**

> Contexto

*Atualmente, eu insiro em um Form's dados para fazer o check-list referente ao andamento da estufa.*

> História de usuário

*Como mantenedor da estufa, quero poder fazer o cadastro de dados no sistema via formulário para realizar o check-list.*   

> Critérios de aceitação

- O formulário deve conter os seguintes campos:
  - Qual plantio foi realizado para coletar os dados? (INTERNO OU EXTERNO).
  - Data da coleta (dd/mm/yyyy).
  - Hora da coleta (valor numérico entre 0 a 23).
  - Umidade do solo (%).
  - PH do solo (%).
  - Data de validade da adubação (dd/mm/yyyy).
  - Consumo de água (mililítro).
  - Temperatura ambiente (ºC).
  - Umidade do ar (%).
  - IAF - Índice da área Foliar (%).
  - Qual aspecto das folhas? (SAUDÁVEL OU MURCHA).
  - Qual a coloração das folhas? (VERDE ou VERDE CLARO).
  - Algum desvio detectado durante o processo? (Texto corrido).
- Os campos "IAF" e "Algum desvio detectado durante o processo?" podem ser nulos.

---

- [ ] **Geração de gráficos**

> Contexto

*Atualmente, eu gero gráficos no excel a partir dos arquivos CSV.*

> História de usuário

*Como mantenedor da estufa, quero que o sistema gere gráficos com base nos dados cadastros, tanto os coletados pelos sensores quanto pelo check-list para tornar minha tomada de decisão mais assertiva com relação ao andamento da estufa.*

> Critérios de aceitação

- Referente ao check-list devem haver os gráficos:
  - PH do solo x Dias.
  - Coloração das Plantas x Dias.
  - Coloração das Plantas x Dias.
  - Estado das folhas x Dias.
- Referente aos sensores deve haver um gráfico que compare ao longo do tempo (dias) umidade do solo, umidade do ambiente, temperatura ambiente e volume de água.
- Os gráficos devem ser interativos, por exemplo deve ser possível escolher comparar todos os dados dos sensores ou apenas dois ou mais.

---

### Requisitos não funcionais

- [ ] **Pré-cadastro de dados**

> Contexto

*Atualmente, eu já possuo vários arquivos CSV contendo os dados coletados desde o início da estufa*

> História de usuário

*Como mantenedor da estufa, quero que o sistema já contenha os dados que eu já tenho para que eu precise apenas inserir dados novos.*

> Critérios de aceitação

- Todos os dados coletados pelos sensores e check-list devem estar cadastros no site quando ele chegar na mão do cliente

---

### Sprint 2

#### Requisitos funcionais

- [ ] **Cadastro automatizado dos dados coletados pelos sensores**

> Contexto

*Atualmente, os dados coletados pelos sensores da estufa são inseridos em um cartão microSD de forma automática por meio de uma placa (microcontrolador) Wemos D1 R32.*

> História de usuário

*Como mantenedor da estufa, quero que o sistema consiga receber os dados inseridos no cartão microSD de forma automatizada para que eu não tenha que ficar retirando o cartão microSD para fazer o registro dos dados contidos nele.*

> Critérios de aceitação

- Os dados deve ser cadastrados no sistema assim que o cartão SD receber dados dos sensores da estufa.
- Os dados enviados pelo controlador devem ser validados no sistema.
- Os sistema deve abortar a comunicação caso algum dado não esteja no formato correto.

---

- [ ] **Login de usuários**

> História de usuário

*Como mantenedor da estufa, quero que o sistema possua funcionalidade login de e-mail e senha para que apenas usuários que eu confie tenham acesso ao sistema também.*

> Critérios de aceitação

- Login de exigir o e-mail institucional e senha.
- O sistema deve validar o formato do e-mail e senha fornecidos.
- A senha deve conter pelos menos 6 caracteres.
- O usuário deve poder escolher se o sistema deve manter ou não sua sessão mesmo que o navegador feche.

---

#### Requisitos não funcionais

- [ ] **Mensagens de Erro**

> História de usuário

*Como mantenedor da estufa, quero que o sistema exiba mensagens quando alguma ação minha não for realizada com sucesso, por exemplo um erro de login ou erro de upload de arquivo para que eu tenha consciência que estou inserindo uma informação errada.*

> Critérios de aceitação

- O sistema deve exibir erros de login mal sucedido.
- O sistema deve exibir mensagens de error referente à formatação dos campos dos formulários do sistema, seja campo de texto ou de upload de arquivo.
- As mensagens deve estar bem destacadas na página.

#### Lembrança de usuário

*Como mantenedor da estufa, quero poder escolher se o sistema deve manter minha sessão mesmo que o navegador feche para que eu não tenha que fazer login novamente quando eu retornar ao sistema*

> Critérios de aceitação

- Deve haver um campo de "Lembre-se de mim" no formulário de login.

---

### Sprint 3

#### Requisitos funcionais

- [ ] **Administrador de usuários**

> História de usuário

*Como mantenedor da estufa, quero haja um usuário administrador para gerenciar dados dos usários do sistema*

> Critérios de aceitação

- Só pode haver um usuário administrado.
- Um usuário administrador deve vir pré-cadastro no sistema.
- O administrador deve possuir todos os dados que um usuário comum tem.
  - nome.
  - email institucional.
  - senha.
- O administrador deve fazer login para fazer o acessar o sistema.
- Somente o administrador deve acessar e executar recursos desenvolvidos para o administrador e o sistema deve validar isso.
- O administrador deve poder fazer tudo que um usuário comum faz.

---

- [ ] **Cadastro de usuário**

> História de usuário

*Como administrador, quero poder cadastrar um usuário para que o sistema para monitorar a estufa seja de fato utilizado por alguém*

> Critérios de aceitação

- O administrador deve preencher um formulário de cadastro contendo os campos:
  - nome.
  - email institucional.
  - senha.
  - confirmação de senha.
- Nenhum campo deve ser nulo.

- [ ] **Edição de usuário**

> História de usuário

*Como administrador, quero poder editar as informações de um usuário para corrigir enventuais erros de cadastro.*

> Critérios de aceitação

- O administrador deve poder editar todos os dados de um usuário.
- O administrador pode editar mais de um campo de uma vez.

---

- [ ] **Deleção de um usuário**

> História de usuário

*Como administrador, quero poder excluir um usuário para que ele não tenha mais acesso ao sistema.*

> Critérios de aceitação

- O administrador deve poder deletar um usuário por um botão.

---

- [ ] **Listagem de usuários**

> História de usuário

*Como administrador, quero poder listar todos os usuários dos sistema para saber quais usuários estão cadastrado.*

> Critérios de aceitação

- Os usuários do sistema deve ser listados em forma de tabela exibindo seus respectivos dados.

---

- [ ] **Visualização de perfil de usuário**

> História de usuário

*Como administrador, quero poder visualizar o perfil de usuário para pode analisá-lo de forma particular.*

> Critérios de aceitação

- Os usuários do sistema deve ser listados em forma de tabela exibindo seus respectivos dados.

---

#### Requisitos não funcionais

- [ ] **Mensagens de alerta**

> História de usuário

*Como administrador, quero poder se avisado que estou fazendo uma ação que pode afetar o sistema como um todo para eu não cometer equívicos e ter certeza do que eu estou fazendo.*

> Critérios de aceitação

- O administrador deve ser avisado por mensagem de texto ao tentar editar ou deletar um usuário.
- O administrador deve poder confirmar ou cancelar a ação pela mensagem.

---

### Sprint 4 

#### Requisitos funcionais

- [ ] **Exportação de arquivo csv em formato de excel**

> História de usuário

*Como mantenedor da estufa, quero poder exportar dados cadastrados no sistema para possui-los como backup.*

> Critérios de aceitação

- Os dados referente aos sensores e check-list devem ser exportados separadamente.
- O arquivo excel gerado deve conter todos os dados cadastros no sistema até então.
- O arquivo excel gerado deve conter as colunas no mesmo formato que os dados foram cadastrados originalmente.

---

- [ ] **Filtragem de usuários**

> História de usuário

*Como administrador, quero poder filtrar usuários por nome e e-mail insitucional*

> Critérios de aceitação

- Somente os usuários com nome ou e-mail parecido devem aparecer para o usuário.
- Os filtros podem ser aplicados ao mesmo tempo.
- Deve ser indicado quais filtros estão sendo aplicados no momento.

---
