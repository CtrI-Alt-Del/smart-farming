
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
- A senha deve ser criptografa utilizando criptografia [BCrypt](https://medium.com/reprogramabr/uma-breve-introdu%C3%A7%C3%A3o-sobre-bcrypt-f2fad91a7420).
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

---

- [ ] **Responsividade**

*História de usuário:*

> Como mantenedor da estufa, quero que o site seja responsivo para que eu possa usá-lo por qualquer tipo de dispositivo.

*Critérios de aceitação:*

- Todas a páginas devem se adaptar de acordo com o tamanho do dispositivo do usuário, tanto de forma visual, quanto comportamental.

---

- [ ] **Exportação de dados dos registros para arquivo CSV**

*História de usuário:*

> Como mantenedor da estufa, quero poder exportar os dados dos registros (check-list ou sensores) para um arquivo CSV para que eu possa utilizar essa base de dados para outros fins como migração de dados para outro sistema, por exemplo.

*Critérios de aceitação:*

- Os registros referente aos sensores deve vir em um arquivo csv separado dos referente ao checklist
- As colunas do arquivo CSV devem corresponder a do arquivo csv que é utilizado para inserir dados 
- O arquivo CSV deve conter todos os dados cadastrados no sistema. 

---

- [ ] **Backup dos dados de registros**

*História de usuário:*

> Como mantenedor da estufa, quero que o sistema faça backup dos registros (check-list ou sensores) para que esses valores sejam recuperados em caso de eventual perda.

*Critérios de aceitação:*

- O backup deve ser realizado uma vez por dia à meia-noite.
- cada arquivo de backup deve ser substituído pelo anterior

---

## Gráfico Burndown 📈
