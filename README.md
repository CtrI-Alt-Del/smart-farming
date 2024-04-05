
## Backlog do produto 🎯

### Sprint - 1️⃣ 

#### Requisitos funcionais ✅

- [ ] **Cadastro de dados dos sensores via arquivo CSV**

*Contexto:*

> Atualmente, os dados coletados coletados pelos sensores da estufa estão armazenados em um arquivo do tipo [CSV](https://www.freecodecamp.org/portuguese/news/o-que-e-um-arquivo-csv-e-como-abrir-esse-formato-de-arquivo/).

*História de usuário:*

> Como mantenedor da estufa, quero fazer o upload de dados contidos nos meu arquivo CSV no sistema para armazená-los de forma mais segura.

*Critérios de aceitação:*

- O upload deve aceitar arquivos CSV tanto em formato de texto, quanto de Excel.
- O sistema deve validar os dados contidos no arquivo antes de concluir o upload, ou seja, deve haver conformidade com as colunas presentes nos arquivos CSV do cliente, assim como o tipo de dado registrado.

---

- [ ] **Geração do gráfico dos dados de sensores**

*Contexto:*

> Atualmente, eu gero um gráfico no excel a partir dos arquivo CSV referente aos dados coletados pelos sensores.

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema gere um gráfico de linha referente os dados coletados pelos sensores com relação a um período de dias a fim de facilitar minha análise acerca do andamento da estufa ao longo do tempo.

*Critérios de aceitação:*

- O gráfico deve exibir os dados:
  - Umidade do solo.
  - Umidade do ambiente.
  - Temperatura.
  - Volume de água.
- O usuário deve poder escolher comparar todos os dados dos sensores ou apenas dois ou mais.
- O usuário deve poder alterar o períodos de dias utilizado no gráfico para:
  - 7 dias
  - 30 dias
  - 90 dias
- O período de 7 dias deve ser o campo selecionado por padrão

---

### Requisitos não funcionais ☑️

- [ ] **Pré-cadastro de dados dos sensores**

*Contexto:*

> Atualmente, eu já possuo vários dados coletados pelos sensores desde o começo da estufa

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema já contenha os dados que eu já tenho para que eu precise apenas inserir dados novos.

*Critérios de aceitação:*

- Todos os dados coletados pelos sensores devem estar cadastros no site quando ele chegar na mão do cliente

---

### Sprint - 2️⃣

#### Requisitos funcionais ✅

- [ ] **Cadastro automatizado dos dados coletados pelos sensores**

*Contexto:*

> Atualmente, os dados coletados pelos sensores da estufa são inseridos em um cartão microSD de forma automática por meio de uma placa (microcontrolador) Wemos D1 R32.

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema consiga receber os dados inseridos no cartão microSD de forma automatizada para que eu não tenha que ficar retirando o cartão microSD para fazer o registro dos dados contidos nele.

*Critérios de aceitação:*

- Os dados devem ser cadastrados no sistema assim que o cartão SD receber dados dos sensores da estufa.
- Os dados enviados pelo microcontrolador devem ser validados no sistema.
- Os sistema deve abortar a comunicação caso algum dado não esteja no formato correto.

---

- [ ] **Cadastro de dados de check-list via arquivo CSV**

*Contexto:*

> Atualmente, eu tenho os dados de check-list contidos em um arquivo CSV.

*História de usuário:*

> Como mantenedor da estufa, quero fazer o upload de dados de check-list contidos em um arquivo CSV no sistema para armazená-los de forma mais segura.

*Critérios de aceitação:*

- O upload dos dados de check-list deve serguir o mesmo procedimento do upload dos dados coletado pelos sensores.  

---

- [ ] **Geração de gráficos acerca dados de check-list**

*Contexto:*

> Atualmente, eu gero vários gráficos no excel a partir do arquivo CSV referente aos dados de check-list.

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema gere gráficos referente os dados de check-list com relação a um período de dias a fim de facilitar minha comparação com os dados coletados pelos sensores.

*Critérios de aceitação:*

- Deve haver 3 gráficos:
  - PH do solo x Dias.
  - Coloração das Plantas x Dias.
  - Estado das folhas x Dias.
- Os três gráficos deve ser do tipo pizza.

---

- [ ] **Cadastro de dados de check-list via formulário**

*Contexto:*

> Atualmente, eu insiro em um Form's dados de check-list a fim de fazer a comparação com os dados coletados pelos sensores.

*História de usuário:*

> Como mantenedor da estufa, quero poder fazer o cadastro de dados de check-list via formulário para mantê-los salvo dentro do sistema.

*Critérios de aceitação:*

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
- Apenas os campos "IAF" e "Algum desvio detectado durante o processo?" podem ser nulos.

---

- [ ] **Tabela de exibição de registros**

*História de usuário:*

> Como mantenedor da estufa, quero visualizar os registros tanto referente aos dados coletados pelos sensores quanto ao check-list em respectivas tabelas a fim de que eu possa visualizar esses dados de forma escrita.

*Critérios de aceitação:*

- Cada linha da tabela deve exibir um registro contendo seus respectivos dados para cada coluna presente no arquivo CSV.
- Os registros deve ser ordenados por ordem descrescente com relação à data de cadastro.

---

- [ ] **Cadastro de dados dos sensores via formulário**

*História de usuário:*

> Como mantenedor da estufa, quero poder fazer o cadastro de dados coletos pelos sensores no sistema por meio de um formulário, com o objetivo de fazer o cadastramento de uma forma mais manual caso eu queira.

*Critérios de aceitação:*

- O formulário deve conter os seguintes campos:
  - Data (dd/mm/aaaa).
  - Horário (Horas:Minutos).
  - Umidade do solo (%).
  - Umidade Ambiente (%).
  - Temperatura Ambiente (°C).
  - Volume de água (ml).
- O sistema deve validar os dados vindo do formulário, ou seja, se os campos estão condizentes com os dados armazenados no arquivo CSV.
- Nenhum campo pode ser nulo.

---

#### Requisitos não funcionais ☑️

- [ ] **Mensagens de erro**

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema exiba mensagens quando alguma ação minha não for realizada com sucesso para que eu tenha consciência de fato que algo ocorreu de errado.

*Critérios de aceitação:*

- O sistema deve exibir mensagens de error referente à má formatação dos dados inseridos pelo usuário nos formulários em cada campo má formatado, assim como exibir uma mensagem de erro na página caso o erro não esteja relacionado a um campo de formulário mas a algum erro interno do sistema.
- As mensagens deve estar bem destacadas do resto dos elementos da página.

---

### Sprint - 3️⃣

#### Requisitos funcionais ✅

- [ ] **Usuário administrador**

*História de usuário:*

> Como mantenedor da estufa, quero que haja um usuário administrador para gerenciar o sistema para que nem todos os usuários que venham a acessar o site possam alterar os dados cadastrados.

*Critérios de aceitação:*

- Só pode haver um usuário administrador.
- Um usuário administrador deve vir pré-cadastro no sistema.
- O administrador deve possuir os seguintes dados:
  - nome.
  - email.
  - senha.
- Somente o administrador deve poder acessar e executar recursos desenvolvidos para o administrador e o sistema deve validar isso.
- O administrador deve poder fazer tudo que um usuário comum faz.

---

- [ ] **Edição de registros**

*História de usuário:*

> Como administrador, quero pode editar qualquer campo de qualquer registro referente aos dados coletados pelos sensores para que eu possa corregir eventuais erros de cadastro.*

*Critérios de aceitação:*

- O usuário deve poder editar por meio de formulário que conterá por padrão todos os dados atuais daquele registro.
- Os sistema deve validar os novos dados cadastrado.

- [ ] **Deleção de registros**

*História de usuário:*

> Como administrador, quero pode deletar qualquer registro referente aos dados coletados pelos sensores para poder remover os repetidos ou os incongruentes.*

*Critérios de aceitação:*

- O usuário deve poder selecionar um ou mais registros para deletar.

- [ ] **Filtragem de registros**

*História de usuário:*

> Como mantenedor da estufa, quero pode filtrar registros exibidos nas tabelas por período compreendido entre duas datas.

*Critérios de aceitação:*

- O usuário deve selecionar uma data de início e uma data de fim (as duas datas são inclusas no filtro).
- Apenas os registros compreendidos entre essas duas datas devem ser exibidos nas suas respectivas tabelas.

- [ ] **Paginação de registros**

*História de usuário:*

> Como administrador, quero que as tabelas possuem páginas onde cada página tenha no máximo 20 registros para que nem todos os registros cadastrados nos sistema seja exibidos.

*Critérios de aceitação:*

- Deverá haver uma navegação composta por botões embaixo de cada tabela para que o usuário possa nagevar entre as páginas.
- Deve haver um indicativo de qual página o usuário está.
- A nevegação deve exibir no máximo 5 botões, ou seja, a numeração dos botões deve ser dinâmica com base na quantidade.

#### Requisitos não funcionais ☑️

- [ ] **Mensagens de alerta**

*História de usuário:*

> Como mantenedor da estufa, quero poder se avisado que estou fazendo uma ação que pode afetar o sistema como um todo para eu não cometer equívicos e ter certeza do que eu estou fazendo.

> Critérios de aceitação

- O usuário deve ser avisado por mensagem de texto ao tentar editar ou deletar qualquer registro do sistema (seja referente aos dados dos sensores ou do check-list).
- O usuário deve poder confirmar ou cancelar a ação por botões presentes abaixo da mensagem.

---

### Sprint - 4️⃣

#### Requisitos funcionais ✅

- [ ] **Login**

*História de usuário*

> Como administrador, quero que haja a funcionalidade de login de e-mail e senha para que apenas eu possa acessar os recursos do sistema que estão disponíveis para o usuário administrador.

*Critérios de aceitação*

- Login deve exigir um e-mail e senha a partir de um formulário contendo esses campos.
- O sistema deve validar o formato do e-mail e senha fornecidos.
- A senha deve conter pelos menos 6 caracteres.
- E-mail deve serguir o formato de e-mail do g-mail.
- O sistema deve redirecionar o usuário para a página de login caso ele tente acessar alguma rota protegida
- O sistema deve adaptar as páginas quando o administrador estiver logado no sistema, como a exibição de um botão para adicionar um registro, por exemplo.

--- 

- [ ] **Redefinição de senha**

*História de usuário:*

> Como administrador, quero pode redefinir minha senha caso eu tenha esquecido.

*Critérios de aceitação:*

- Deve ser enviado um e-mail ao administrador que conterá um link que o levará para página de digitar uma nova senha.
- O formulário de redefinição de senha deve conter os campos:
  - Senha.
  - Confirmação de senha.
- Nenhum campo pode ser nulo e devem ser exatamente iguais.
- O usuário deve ser redirecionado para a página de login uma vez concluído a redefinição de senha.

#### Requisitos não funcionais ☑️

- [ ] **Criptografia de senha**

*História de usuário*

> Como administrador, quero que minha senha sempre esteja criptografada para aumentar a segurança de acesso ao sistema.

*Critérios de aceitação:*

- A senha deve ser criptografada utilizando o método bcrypt.

---

- [ ] **Persistência de sessão de login**

*História de usuário:*

> Como administrador, quero que o sistema persista minha sessão uma vez após feito o login mesmo que o navegadro feche para que no próximo dia eu não tenha que fazer o procedimento de login novamente.

*Critérios de aceitação:*

- Deve haver um campo chamado "Lembre-se de mim" no formulário de login.
- O administrador deve poder escolher ou não manter sua sessão mesmo que o navegador feche.

- [ ] **Responsividade**

*História de usuário:*

> Como mantenedor da estufa, quero que o site seja responsivo para que eu possa usá-lo por qualquer tipo de dispositivo.

*Critérios de aceitação:*

- Todas a páginas devem se adaptar de acordo com o tamanho do dispositivo do usuário, tanto de forma visual, quanto comportamental.

---