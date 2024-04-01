<h1 align="center">✨CTRL ALT DEL✨</h1>

<p align="center">An Application about our API from Fatec Sao Jose dos Campos.🚀</p>

<h3 align="center">Coming Soon!!</h3>

<h4 align="center"> 
	🚧  Space In Development  🚧
</h4>

## Backlog

### Sprint 1

#### Requisitos funcionais

- [ ] **Cadastro de dados via arquivo CSV**

> Contexto

*Atualmente, para acompanhar a saúde da planta e a ocorrência de falhas eu registro esses dados em arquivos do tipo [CSV](https://www.freecodecamp.org/portuguese/news/o-que-e-um-arquivo-csv-e-como-abrir-esse-formato-de-arquivo/).*

> História de usuário

*Como mantenedor da estufa, quero fazer o upload de dados contidos nos meus arquivos CSV no sistema para armazená-los de forma mais segura.*

> Critérios de aceitação

- Mais de arquivo CSV pode ser lido de uma vez.
- O upload deve aceitar arquivos CSV tanto em formato de texto, quanto de Excel.
- O sistema deve validar os dados contidos no arquivo antes de concluir o upload.

---

- [ ] **Cadastro de dados via formulário**

> Contexto

*Atualmente, eu insiro os dados em um Google Forms para então gerar os arquivos CSV.*

> História de usuário

*Como mantenedor da estufa, quero poder fazer o cadastro de dados no sistema por meio de um formulário caso não seja possível via arquivo CSV, com o objetivo de fazer o cadastramento de uma forma mais manual.*

> Critérios de aceitação

- O formulário deve ter uma página própria no sistema.
- Os campos do formulário deve estar condizentes com as colunas dos arquivos CSV.
- O sistema deve validar os dados vindo do formulário.
- O formulário deve conter os seguintes campos:

---

- [ ] **Geração de gráficos**

> Contexto

*Atualmente, eu gero gráficos no excel a partir dos arquivos CSV.*

> História de usuário

*Como mantenedor da estufa, quero que o sistema gere gráficos com base nos dados cadastros para tornar minha tomada de decisão mais assertiva com relação ao andamento da estufa.*

> Critérios de aceitação

- 
- 

---

### Requisitos não funcionais

- [ ] **Pré-cadastro de dados**

> Contexto

*Atualmente, eu já possuo vários arquivos CSV contendo os dados coletados desde o início da estufa*

> História de usuário

*Como mantenedor da estufa, quero que o sistema já contenha os dados que eu já tenho para que eu precise apenas inserir dados novos.*

> Critérios de aceitação

- Os dados pré-cadastrados devem ser referente aos que estão em arquivo CSV e no cartão SD.

---

### Sprint 2

#### Requisitos funcionais

- [ ] **Cadastro automatizado de dados contidos no cartão SD**

> Contexto

*Atualmente, os dados coletados pelos sensores da estufa são inseridos em um cartão SD de forma automárica e isso acontece já algum tempo.*

> História de usuário

*Como mantenedor da estufa, quero que o sistema consiga receber os dados inseridos no cartão SD de forma automatizada para eu não ter que cadastrar de forma manual todos esses dados que eu já tenho.*

> Critérios de aceitação

- Os dados deve ser cadastrados no sistema assim que o cartão SD receber dados dos sensores da estufa.

- [ ] **Login de usuários**

> História de usuário

*Como mantenedor da estufa, quero que o sistema possua funcionalidade login de e-mail e senha para que apenas usuários que eu confie tenham acesso ao sistema também.*

> Critérios de aceitação

- O sistema deve validar o formato do e-mail e senha do usuário cadastrados.
- A senha deve conter pelos menos 6 caracteres
- Um usuário não deve ter o mesmo e-mail de outro usuário.
- O sistema deve manter a sessão do usuário mesmo que o navegador feche.

#### Requisitos não funcionais

- [ ] **Mensagens de Erro**

> História de usuário

*Como mantenedor da estufa, quero que o sistema exiba mensagens quando alguma ação minha não for realizada com sucesso, por exemplo um erro de login ou erro de upload de arquivo para que eu tenha consciência que estou inserindo uma informação errada.*

> Critérios de aceitação

- O sistema deve exibir erros de login mal sucedido
- O sistema deve exibir mensagens de error referente à formatação dos campos dos formulários do sistema, seja campo de texto ou de upload de arquivo.
- As mensagens deve estar bem destacadas na página.





