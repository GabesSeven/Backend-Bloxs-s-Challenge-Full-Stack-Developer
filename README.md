# <em>Backend - Bloxs s Challenge - Full Stack Developer</em>
<br><br>

<p style="text-align: justify;">
    Interface de programação de aplicativos (API): operações bancárias básicas a partir de uma simples aplicação web.
  <ol>
    <li>BackEnd: <a href='https://github.com/GabesSeven/Backend-Bloxs-s-Challenge-Full-Stack-Developer'>https://github.com/GabesSeven/Backend-Bloxs-s-Challenge-Full-Stack-Developer</a>;</li>
    <li>FrontEnd: <a href='https://github.com/GabesSeven/Frontend-Bloxs-s-Challenge-Full-Stack-Developer'>https://github.com/GabesSeven/Frontend-Bloxs-s-Challenge-Full-Stack-Developer</a>.</li>
    <li>Banco de Dados MySQL para o Render: <a href='https://github.com/GabesSeven/Database-Bloxs-s-Challenge-Full-Stack-Developer'>https://github.com/GabesSeven/Database-Bloxs-s-Challenge-Full-Stack-Developer</a>.</li>
  </ol>
</p>

<br>
<hr>
<br>

## ⚠️⚠️⚠️ Observações - O que faltou? ⚠️⚠️⚠️
<br><br>

### Segurança
<br>
<ol>
 <li>Para facilitar a exeução estou subindo os arquivos das variáveis de ambiente (⚠️⚠️⚠️ISSO É ERRADÍSSIMO⚠️⚠️⚠️) e as bibliotecas;</li>
</ol>

### Acesso Remoto
<br>
<ol>
 <li>Subir a aplicação em ambiente cloud, atualmente trabalho com Render para sublir as plataformas (frontend, backend e banco de dados);</li>
 <li>A arquitetura ideal seria em um ambiente <strong>AWS</strong> como na imagem abaixo.</li>
</ol>

<figure>
<p align="center">
  <img src="https://github.com/GabesSeven/Backend-Bloxs-s-Challenge-Full-Stack-Developer/assets/37443722/0688ce5c-66ad-4470-938d-0a782d030a01" height="450" width="650" alt="arquitetura AWS"/><br>
  Arquitetura AWS ideal para o projeto.
</p>
</figure>

### Banco de Dados
<ol>
<li>Como só desenvolvi local, deixei o banco padrão Python, SQLite3, como visto na imagem abaixo;</li>
</li>Plataforma Render possui <strong>PosgreSQL (gratuito para teste)</strong> e <strong>MySQL (pago)</strong>;</li>
<li>Configurei o upload do banco MySQL no Render, mas não passei o cartão de crédito;</li>
</li>Porém domínio em Banco de Dados relacionais, atualmente crio e gerencio o da Statup ao qual trabalho, também sei trabalhar com Normalização, já trabalhei com Oracle, PostgreSQL e MySQL.</li>

<figure>
<p align="center">
  <img src="https://github.com/GabesSeven/Backend-Bloxs-s-Challenge-Full-Stack-Developer/assets/37443722/7dae7e44-3103-4d9b-9740-0d928164467d" height="450" width="650" alt="Console - banco SQLLite3"/><br>
  Console - SQLite3
</p>
</figure>

### Endpoints
<br>
<ol>
  <li>Extrato</li>
  <li>Saque - ocorre verificação de limite por valores de transações diárias</li>
</ol>

## Execução Local 🏃‍♀️
<br><br>

<p>No <strong>Terminal</strong> <em>/ <strong>Console</em></strong>:</p>
<ol>
	<li>Faça um clone do projeto na sua máquina:<br><code>git clone git@github.com:GabesSeven/credit-application-system.git</code></li><br>
	<li>Entre na pasta raiz do projeto:<br><code>cd credit-application-system/</code></li><br>
	<!-- <li>Em um terminal, crie um ambiente virtual:<br> <code>python3.11 -v .venv</code></li><br> -->
	<li>Em um terminal, inicie o ambiente virtual:<br> <code>source .venv/bin/activate</code></li><br>
	<!-- <li>Em um terminal, instale as bibliotecas:<br> <code>pip3 install -r requirements.txt</code></li><br> -->
  <li>Acessoa ao Swagger. Em um navegador:<br><a href='http://127.0.0.1:5000/swagger-ui'>http://127.0.0.1:5000/swagger-ui</a></li><br>
</ol>

<br>
<hr>
<br>

## Rotas 🛣️
<br><br>

#### Operação em Usuário: Criar Conta
- **URL:** `/criar-usuario`
- **Método:** `POST`
- **Descrição:** Cria um novo usuário.
- **Entrada:** 
```
json {
  "email": "user@example.com",
  "senha": "string",
  "nome": "string",
  "sobrenome": "string",
  "cpf": "string",
  "data_nascimento": "2023-12-20"
} 
```
- **Saída (201):** 
```
json {
  "cpf": "string",
  "data_criacao": "2023-12-20T13:33:43.877102",
  "data_nascimento": "2023-12-20",
  "email": "user@example.com",
  "id_pessoa": "780c74f0-a253-4903-bcc2-e78f99b31f6b",
  "nome": "string",
  "sobrenome": "string",
  "usuario_ativo": false
}
```
<br>

#### Autenticação: Login
- **URL:** `/login`
- **Método:** `POST`
- **Descrição:** Autenticação de usuário para obter token de acesso.
- **Entrada:** 
```
json {
  "email": "user@example.com",
  "senha": "string"
}
```
- **Saída (200):** 
```
json {
  "token_acesso": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzAzMDgwMjUwLCJqdGkiOiJiZmVlODE0Mi05OTMzLTQwZDItYTMzNy04ZTUzMjBjMWFhMDQiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiYTBhNGJkYTAtNTg2My00YTY1LTg3YzQtNjUzMjE3YzkxMmI1IiwibmJmIjoxNzAzMDgwMjUwLCJjc3JmIjoiNTIwNTRjNWItNmIyZi00YzI2LTk3Y2UtYWVjNDZjOTkzMjMxIiwiZXhwIjoxNzAzMDgxMTUwfQ.eN06KsVxK90kku2Ik7mKRp7Nd9W3nNNgBuWAjJCZJw0",
  "token_refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMzA4MDI1MCwianRpIjoiYTQ4NWExNDMtNGM4NS00ZGQwLWIyYTItYmI1ZjgxOTQ3ZDJjIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJhMGE0YmRhMC01ODYzLTRhNjUtODdjNC02NTMyMTdjOTEyYjUiLCJuYmYiOjE3MDMwODAyNTAsImNzcmYiOiI4NTRjNGJjNi00MjYxLTQ5MDEtYTc2Yy1mMTViMTNkNDUzODgiLCJleHAiOjE3MDU2NzIyNTB9.QYlZsPi-PAs8I0O4ntBHJ9kyU9gs-xxx_5LWchKKkis"
}
```
<br>

### Autenticação: Logout
- **URL:** `/logout`
- **Método:** `POST`
- **Descrição:** Encerra a sessão de usuário bloqueando o token de acesso do mesmo.
- **Saída (200):** 
json {
  "mensagem": "Sessão encerrada com sucesso."
}
<br>

### Autenticação: Atualização de Token
- **URL:** `/refresh`
- **Método:** `POST`
- **Descrição:** Atualiza o token de acesso.
- **Saída (200):** 
```
json {
  "token_acesso": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzAzMDgwMjUwLCJqdGkiOiJiZmVlODE0Mi05OTMzLTQwZDItYTMzNy04ZTUzMjBjMWFhMDQiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiYTBhNGJkYTAtNTg2My00YTY1LTg3YzQtNjUzMjE3YzkxMmI1IiwibmJmIjoxNzAzMDgwMjUwLCJjc3JmIjoiNTIwNTRjNWItNmIyZi00YzI2LTk3Y2UtYWVjNDZjOTkzMjMxIiwiZXhwIjoxNzAzMDgxMTUwfQ.eN06KsVxK90kku2Ik7mKRp7Nd9W3nNNgBuWAjJCZJw0"
}
```

<br>

#### Operação em Conta: Criar Conta
- **URL:** `/conta/<id_conta>`
- **Método:** `GET`
- **Descrição:** Criar uma nova conta.
- **Entrada:** 
```
json {
  "id_pessoa": "780c74f0-a253-4903-bcc2-e78f99b31f6b",
  "saldo": 0,
  "limite_saque_diario": 0,
  "tipo_conta": 0
}
```
- **Saída (201):** 
```
{
  "saldo": 0,
  "limite_saque_diario": 0,
  "tipo_conta": 0,
  "id_conta": "780c74f0-a253-4903-bcc2-e78f99b31f6b",
  "flag_ativo": true,
  "data_criacao": "2023-12-20"
}
```

<br>

#### Operação em Conta: Consultar Saldo de Conta
- **URL:** `/conta/<id_conta>`
- **Método:** `GET`
- **Descrição:** Obtém o saldo de uma conta por ID.
- **Saída (200):** 
```
json {
  "saldo": float
}
```

<br>

### Operação em Conta: Depósito em Conta
- **URL:** `/operacao`
- **Método:** `PUT`
- **Descrição:** Realiza um depósito em uma conta.
- **Entrada:** 
```
json {
  "id_conta": "780c74f0-a253-4903-bcc2-e78f99b31f6b",
  "valor": 0
}
```
- **Saída (200):** 
```
json {
  "id_conta": "780c74f0-a253-4903-bcc2-e78f99b31f6b",
  "valor": 0
}
```
<br>

### ⚠️NÃO FINALIZADO: Operação em Conta: Saque em Conta ⚠️ 

<br>

- **URL:** `/operacao/`
- **Método:** `POST`
- **Descrição:** Realiza saque em uma conta.


### ⚠️NÃO FINALIZADO: Operação em Conta: Extrato em Conta ⚠️ 

<br>

- **URL:** `/operacao/<id_conta>`
- **Método:** `GET` (para extrato)
- **Descrição:** Realiza um depósito.

<br><br><br>

## Banco de Dados 🎲

```plaintext
    +-----------------+          +---------------------+
    |    PessoaModel  |1        N|   ContaModel        |
    +-----------------+<-------->|---------------------+
    | id_pessoa [PK]  |          | id_conta [PK]       |
    | email           |          | id_pessoa [FK]      |
    | senha           |          | saldo               |
    | nome            |          | limite_saque_diario |
    | sobrenome       |          | flag_ativo          |
    | cpf             |          | tipo_conta          |
    | data_nascimento |          | data_criacao        |
    | data_criacao    |          +---------------------+
    | usuario_ativo   |                1 |
    +-----------------+                  |
                                         |
                                         |
                                       N |
                                 +-------------------+
                                 |  TransacaoModel   |
                                 +-------------------+
                                 | id_transacao [PK] |
                                 | id_conta [FK]     |
                                 | valor             |
                                 | data_transacao    |
                                 +-------------------+
```    

<br>
<hr>
<br>

<!-- ## Tecnologias Utilizadas 💾
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

![FLYWAY](https://img.shields.io/badge/flyway-CC0200?logo=flyway&logoColor=white&style=for-the-badge) &nbsp; -->

<br>
<hr>
<br>

## Developer 🧑‍💻 
<br><br>
| [<img src="https://avatars.githubusercontent.com/u/37443722?v=4" width=115><br><sub>Gabriel Ferreira</sub>](https://github.com/GabesSeven)
| :---: 
