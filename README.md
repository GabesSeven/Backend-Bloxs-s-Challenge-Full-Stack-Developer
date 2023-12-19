# <em>Backend - Bloxs s Challenge -Full Stack Developer</em>
<br><br>
<p style="text-align: justify;">
    Interface de programação de aplicativos (API): operações bancárias básicas a partir de uma simples aplicação web. Desenvolvido em Flask.
</p>

<br>
<hr>
<br>

## Execução 🏃‍♀️
<br><br>

<p>No <strong>Terminal</strong> <em>/ <strong>Console</em></strong>:</p>
<ol>
	<li>Faça um clone do projeto na sua máquina:<br><code>git clone git@github.com:GabesSeven/credit-application-system.git</code></li><br>
	<li>Entre na pasta raiz do projeto:<br><code>cd credit-application-system/</code></li><br>
	<li>Execute o comando:<br> <code>./gradlew bootrun</code></li><br>
	<li>Em um navegador, utilize a <em>Uniform Resource Locato</em> (<em>URL</em>) para ter acesso ao <strong>Banco de Dados <em>H2</em></strong>:<br><a href='http://localhost:8080/swagger-ui/index.html'>http://localhost:8080/swagger-ui/index.html</a><br><br><em>username</em>: <strong>gabes</strong><br><em>password</em>: <strong>gabes</strong></li><br>
	<li>Em um navegador, utilize a <em>URL</em> para ter acesso a <strong>documentação</strong> e <strong>testes</strong> dos <strong><em>endpoints</em></strong> com <strong><em>Swagger</em></strong>:<br><a href='http://localhost:8080/h2-console/'>http://localhost:8080/h2-console/</a></li>
</ol>

<br>
<hr>
<br>

## Rotas 

<br><br>

### Operações em Contas

<br>

#### Criar Conta
- **URL:** `/conta`
- **Método:** `POST`
- **Descrição:** Cria uma nova conta.
- **Entrada:** `ContaSchema`
- **Saída (Código 201):** `ContaSchema`

<br>

#### Deletar / Bloquear Conta
- **URL:** `/conta/<id_conta>`
- **Método:** `DELETE`
- **Descrição:** Deleta ou bloqueia uma conta por ID.
- **Saída (Código 204):** `{ "message": "Conta bloqueada com sucesso" }`

<br>

#### Consultar Saldo de Conta
- **URL:** `/conta/<id_conta>`
- **Método:** `GET`
- **Descrição:** Obtém o saldo de uma conta por ID.
- **Saída (Código 200):** `{ "saldo": float }`

<br>

### Depósito em Conta
- **URL:** `/operacao`
- **Método:** `PUT`
- **Descrição:** Realiza um depósito em uma conta.
- **Entrada:** `TransacaoSchema`
- **Saída (Código 200):** `TransacaoSchema`

<br>

### Saque e Extrato em Conta
- **URL:** `/operacao/<id_conta>`
- **Método:** `DELETE` (para saque), `GET` (para extrato)
- **Saída (Código 200):** Para saque, `{ "message": "Saque realizado com sucesso" }`. Para extrato, `{ "extrato": [{ "id_transacao": int, "valor": float, "data_transacao": str }] }`

<br>

### Autenticação e Controle de Usuário

<br>

#### Login
- **URL:** `/login`
- **Método:** `POST`
- **Descrição:** Autenticação de usuário para obter token de acesso.
- **Entrada:** `PessoaSchema`
- **Saída (Código 200):** `{ "token_acesso": str, "token_refresh": str }`
<br>

### Logout
- **URL:** `/logout`
- **Método:** `POST`
- **Descrição:** Encerra a sessão de usuário.
- **Saída (Código 200):** `{ "mensagem": "Sessão encerrada com sucesso." }`
<br>

### Registro de Usuário
- **URL:** `/usuario`
- **Método:** `POST`
- **Descrição:** Registra um novo usuário.
- **Entrada:** `PessoaSchema`
- **Saída (Código 201):** `{ "mensagem": "Usuário criado com sucesso." }`

<br>

### Deletar Usuário
- **URL:** `/usuario/<int:id_usuario>`
- **Método:** `DELETE`
- **Descrição:** Deleta um usuário por ID.
- **Saída (Código 200):** `{ "mensagem": "Usuário deletado." }`

<br>

### Atualização de Token
- **URL:** `/refresh`
- **Método:** `POST`
- **Descrição:** Atualiza o token de acesso.
- **Saída (Código 200):** `{ "token_acesso": str }`

<br><br><br>

<figure>
<p align="center">
  <img src="https://i.imgur.com/7phya16.png" height="450" width="650" alt="API para Sistema de Avaliação de Créditos"/><br>
  Diagrama <em>Unified Modeling Language (UML)</em> Simplificado de uma </em>API Credit Application System</em>
</p>
</figure>

<br>
<hr>
<br>

## Tecnologias Utilizadas 💾
<br><br>

![GIT](https://img.shields.io/badge/git-F05032?logo=git&logoColor=white&style=for-the-badge) &nbsp;

![GITHUB](https://img.shields.io/badge/github-181717?logo=git&logoColor=white&style=for-the-badge) &nbsp;

![KOTLIN](https://img.shields.io/badge/kotlin-7F52FF?logo=kotlin&logoColor=white&style=for-the-badge) &nbsp;

![JAVA](https://img.shields.io/badge/Java-ED8B00?logo=java&logoColor=white&style=for-the-badge) &nbsp;

![GRADLE](https://img.shields.io/badge/gradle-02303A?logo=gradle&logoColor=white&style=for-the-badge) &nbsp;

![SPRING](https://img.shields.io/badge/spring-6DB33F?logo=spring&logoColor=white&style=for-the-badge) &nbsp;

![SPRING BOOT](https://img.shields.io/badge/springboot-6DB33F?logo=springboot&logoColor=white&style=for-the-badge) &nbsp;

![SWAGGER](https://img.shields.io/badge/swagger-85EA2D?logo=swagger&logoColor=white&style=for-the-badge) &nbsp;

![H2 DATABASE](https://img.shields.io/badge/H2DATABASE-1316BF?logo=databricks&logoColor=white&style=for-the-badge) &nbsp;

![HIBERNATE](https://img.shields.io/badge/hibernate-59666C?logo=hibernate&logoColor=white&style=for-the-badge) &nbsp;

![FLYWAY](https://img.shields.io/badge/flyway-CC0200?logo=flyway&logoColor=white&style=for-the-badge) &nbsp;


<br>
<hr>
<br>

<figure>
<p align="center">
  <img src="https://i.imgur.com/1Ea5PH3.png" height="350" width="600" alt="Arquitetura em 3 camadas Projeto Spring Boot"/><br>
  Arquitetura em 3 camadas Projeto Spring Boot
</p>
</figure>

<br>
<hr>
<br>

## Developer 🧑‍💻 
<br><br>
| [<img src="https://avatars.githubusercontent.com/u/37443722?v=4" width=115><br><sub>Gabriel Ferreira</sub>](https://github.com/GabesSeven)
| :---: 
