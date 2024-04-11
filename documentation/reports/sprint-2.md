# Sprint - 2️⃣

## Requisitos funcionais ✅

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

- [ ] **Destaque do último registro.**

*História de usuário:*

> Como mantenedor da estufa, quero visualizar os dados do último registro cadastrado referente ao sensores ao abrir o sistema para saber de imediato como está o estado atual da estufa.

*Critérios de aceitação:*

- Cada capo do último registro deve ser exibido em um widget separadamente.
- Os dados do último registro deve ser exibidos na página principal do site.


---

- [ ] **Cálculo de médias**

*História de usuário:*

> Como mantenedor da estufa, quero visualizar a média de cada dado referente ao registros relacionados aos sensores para eu ter uma visão geral a respeito dessas informações.

*Critérios de aceitação:*

- As médias devem ser visualizadas na página do gráfico referente aos dados coletados pelos sensores.
- Os médias devem refletir o filtro aplicado ao gráfico, ou seja, a média deve ser calculada considerando apenas os registros que correspondem o período de dias selecionado no gráfico.

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

## Requisitos não funcionais ☑️

- [ ] **Mensagens de erro**

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema exiba mensagens quando alguma ação minha não for realizada com sucesso para que eu tenha consciência de fato que algo ocorreu de errado.

*Critérios de aceitação:*

- O sistema deve exibir mensagens de error referente à má formatação dos dados inseridos pelo usuário nos formulários em cada campo má formatado, assim como exibir uma mensagem de erro na página caso o erro não esteja relacionado a um campo de formulário mas a algum erro interno do sistema.
- As mensagens deve estar bem destacadas do resto dos elementos da página.

---

## Gráfico Burndown 📈
