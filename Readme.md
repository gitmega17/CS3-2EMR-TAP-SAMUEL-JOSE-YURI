# Smart Monitoring

Smart Monitoring é um aplicativo web desenvolvido com Flask, que permite a autenticação de usuários, registro de dados de sensores (temperatura e umidade) e visualização gráfica dos dados registrados. O aplicativo usa um banco de dados SQLite para armazenar informações dos usuários e dos dados dos sensores, além de implementar autenticação JWT para segurança.

## Funcionalidades

- **Registro de Usuários**: Permite que novos usuários se registrem com um nome de usuário, senha e um papel (role) que pode ser 'admin' ou 'user'.
- **Login**: Autenticação de usuários com verificação de credenciais e geração de um token JWT.
- **Inserção de Dados**: Usuários podem inserir dados de sensores (temperatura e umidade) via uma API.
- **Visualização de Dados**: Gráficos que exibem as leituras de temperatura e umidade em tempo real.
- **Limpeza de Dados**: Apenas usuários com o papel 'admin' podem limpar todos os dados da tabela de sensores.

## Tecnologias Utilizadas

- Python
- Flask
- SQLite
- JWT (JSON Web Tokens)
- Bcrypt para hashing de senhas
- Chart.js para visualização gráfica
- HTML/CSS para front-end

## Requisitos

- Python 3.x
- Biblioteca Flask
- Biblioteca SQLite
- Biblioteca Bcrypt
- Biblioteca JWT
- dotenv (para variáveis de ambiente)

## Fluxograma

![Fluxograma](images/fluxograma.png)

## Endpoints

| Método | Endpoint                    | Descrição                              |
|--------|-----------------------------|----------------------------------------|
| POST   | `/register`                 | Cadastra um novo usuário.             |
| POST   | `/login`                    | Realiza o login e retorna um token.   |
| POST   | `/dados-sensores`           | Insere novos dados de sensores.       |
| GET    | `/dados-sensores`           | Retorna todos os dados de sensores.   |
| DELETE | `/limpar-dados`            | Limpa todos os dados da tabela.       |
| GET    | `/dados-sensores-json`      | Retorna dados de sensores em formato JSON. |
| GET    | `/`                         | Página principal com dados de sensores. |
| GET    | `/graficos`                 | Página de exibição de gráficos.       |

## Parâmetros

### `/register`

- **Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }

### `/login`

- **Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }

### `/dados-sensores`

- **Body:**
  ```json
  {
    "sensor_id": "int",
    "temperatura": "float",
    "umidade": "float"
  }

## Exemplo de Cabeçalho de Autenticação
    Authorization: Bearer <token>


## Exemplos de Requisições e Respostas

### `/register`

#### Requisição
- **Body:**
  ```json
    POST /register
    Content-Type: application/json
    {
        "username": "user1",
        "password": "password123"
    }

#### Resposta
- **Body:**
  ```json
    {
        "message": "Usuário cadastrado com sucesso"
    }

### `/login`

#### Requisição
- **Body:**
  ```json
    POST /login
    Content-Type: application/json

    {
        "username": "user1",
        "password": "password123"
    }

#### Resposta
- **Body:**
  ```json
    {
        "message": "Login realizado com sucesso",
        "token": "<token>"
    }

### `/dados-sensores`

#### Requisição
- **Body:**
  ```json
    POST /dados-sensores
    Content-Type: application/json
    Authorization: Bearer <token>

    {
        "sensor_id": 1,
        "temperatura": 22.5,
        "umidade": 60
    }

#### Resposta
- **Body:**
  ```json
    {
        "message": "Dados inseridos com sucesso"  
    }

#### Requisição
- **Body:**
  ```json
    GET /dados-sensores
    Authorization: Bearer <token>

#### Resposta
- **Body:**
  ```json
    {
        "id": 1,
        "sensor_id": 1,
        "temperatura": 22.5,
        "umidade": 60,
        "timestamp": "2024-10-22T10:00:00"
    },



## Instalação

1. **Clone o repositório**:
    ```bash
    git clone <URL do repositório>
    cd <nome da pasta do repositório>
    ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. **Instale as dependências**:
    ```bash
    pip install Flask python-dotenv bcrypt PyJWT
    ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

5. **Inicialize o banco de dados**:
O banco de dados será inicializado automaticamente na primeira execução do aplicativo.


## Uso

1. **Inicie o servidor**:
 ```bash
 python app.py
 ```
O servidor será iniciado em `http://127.0.0.1:5000`.

2. **Acesse o aplicativo**:
Abra o navegador e vá para `http://127.0.0.1:5000`.

## Estrutura do Projeto
/smart_monitoring
├── app.py # Código principal do aplicativo Flask 
├── .env # Variáveis de ambiente 
├── /templates 
│ ├── index.html # Página de login 
│ └── graficos.html # Página de gráficos 
└── requirements.txt # Lista de dependências

## Deploy na Vercel

Este projeto pode ser facilmente implantado na Vercel. Siga os passos abaixo para configurar o deploy:

### Pré-requisitos
- Certifique-se de que você possui uma conta na [Vercel](https://vercel.com/signup).
- Tenha o [Node.js](https://nodejs.org/) instalado em sua máquina.

### Passos para Deploy

1. **Criar um Novo Projeto na Vercel**
   - Acesse o [Painel da Vercel](https://vercel.com/dashboard).
   - Clique em "New Project".

2. **Importar o Repositório**
   - Escolha a opção para importar do seu repositório Git (GitHub, GitLab, ou Bitbucket).
   - Se necessário, conecte sua conta da Vercel ao serviço de controle de versão.

3. **Configurar o Projeto**
   - Após importar, a Vercel tentará detectar automaticamente as configurações do projeto. Verifique se está tudo correto.
   - Nas variáveis de ambiente, adicione as configurações necessárias, como `SECRET_KEY`, `DATABASE_URL`, etc., conforme sua aplicação exige.

4. **Escolher o Framework**
   - Se o seu projeto usa um framework como Flask, escolha a opção correta, se necessário. A Vercel suporta vários frameworks.

5. **Implantar o Projeto**
   - Clique no botão "Deploy". A Vercel irá construir e implantar seu projeto.
   - Após a conclusão, você receberá uma URL onde seu aplicativo estará disponível.

### Acessando a Aplicação
- Após o deploy, você pode acessar seu aplicativo na URL fornecida pela Vercel. Você também pode configurar um domínio personalizado, se desejado.

### Observações
- Certifique-se de que todas as dependências estejam listadas no seu `requirements.txt`.
- Se houver necessidade de configuração adicional, você pode verificar a documentação da Vercel para mais informações sobre [Configurações de Deploy](https://vercel.com/docs/deployments).





