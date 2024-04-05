# Sprint - 1️⃣ 

## Requisitos funcionais ✅

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

## Requisitos não funcionais ☑️

- [ ] **Pré-cadastro de dados dos sensores**

*Contexto:*

> Atualmente, eu já possuo vários dados coletados pelos sensores desde o começo da estufa

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema já contenha os dados que eu já tenho para que eu precise apenas inserir dados novos.

*Critérios de aceitação:*

- Todos os dados coletados pelos sensores devem estar cadastros no site quando ele chegar na mão do cliente