# 🚚 Rota Certa API - Professional Edition

O **Rota Certa** é o backend de um sistema inteligente de roteirização para caminhoneiros. Muito além de um simples GPS, esta API cruza dados geográficos reais com o perfil do veículo (peso, altura, tipo de carga) para gerar rotas seguras, evitar multas e garantir a conformidade legal do transporte.

## 🛠️ Stack Tecnológico
* **Backend:** Python + FastAPI
* **Banco de Dados:** SQLite (via SQLAlchemy ORM)
* **Segurança:** JWT (JSON Web Tokens) e Bcrypt (Criptografia de Senhas)
* **Geolocalização:** Integração com OpenStreetMap (Nominatim) e OSRM API.

## ⚙️ Arquitetura do Sistema
O projeto utiliza um padrão de **Monolito Modular**, preparando o terreno para uma futura migração para microsserviços, caso necessário:
* `core/`: Configurações de banco de dados e motor de segurança (JWT).
* `models/`: Entidades de banco de dados (SQLAlchemy).
* `schemas/`: Contratos de entrada e saída da API (Pydantic).
* `routers/`: Controladores dos endpoints (Motoristas, Veículos, Rotas, Auth).
* `services/`: Regras de negócio e integração com APIs externas (Satélites).

## 🚀 Como rodar o projeto localmente

1. **Ative o ambiente virtual:**
   ```bash
   venv\Scripts\activate
Instale as dependências:

Bash
pip install -r requirements.txt
(Pacotes essenciais: fastapi, uvicorn, sqlalchemy, requests, passlib, bcrypt, python-jose, python-multipart)

Inicie o servidor:

Bash
uvicorn main:app --reload
Acesse a Documentação Swagger: http://127.0.0.1:8000/docs

🔒 Fluxo de Uso (Caminho Feliz)
A API é blindada. Para calcular uma rota, siga o fluxo de entidades:

Cadastrar Motorista (POST /motoristas/): Crie um usuário. A senha será criptografada automaticamente.

Cadastrar Veículo (POST /veiculos/): Adicione um caminhão vinculando-o ao ID do motorista criado. Tipos de carga suportados: geral, granel, perigosa, refrigerada, viva, indivisivel.

Autenticação (POST /login): Envie o email e a senha do motorista para receber o access_token (JWT).

Calcular Rota (POST /calcular-rota): Com o token no cabeçalho de autorização (Cadeado fechado no Swagger), envie a cidade de origem, destino e o ID do veículo. A API buscará as coordenadas via satélite e retornará a quilometragem, tempo e desvios necessários.

Desenvolvido como projeto de evolução contínua em Engenharia de Software e Data Science.


### 3. Como visualizar
Depois de colar, salve o arquivo e aperte **`Ctrl + Shift + V`** no seu VS Code. Ele vai renderizar o texto e você verá como a formatação ficou limpa e direta ao ponto.