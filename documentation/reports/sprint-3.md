# Sprint - 3️⃣

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

- [ ] **Mensagens de alerta**

*História de usuário:*

> Como mantenedor da estufa, quero poder se avisado que estou fazendo uma ação que pode afetar o sistema como um todo para eu não cometer equívicos e ter certeza do que eu estou fazendo.

> Critérios de aceitação

- O usuário deve ser avisado por mensagem de texto ao tentar editar ou deletar qualquer registro do sistema (seja referente aos dados dos sensores ou do check-list).
- O usuário deve poder confirmar ou cancelar a ação por botões presentes abaixo da mensagem.

## Gráfico Burndown 📈
