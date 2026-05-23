# carved-homes-backend
carved-homes-backend


# 🏡 Carved Homes Backend

Backend profissional da plataforma **Carved Homes**, desenvolvido com **FastAPI + PostgreSQL**, focado em aluguel de quartos, hospedagens premium e reservas modernas em Johannesburg, South Africa.

---

# 🚀 Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- Alembic
- JWT Authentication
- CORS Middleware

---

# 📁 Estrutura do Projeto

```txt
carved-homes-backend/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       ├── health.py
│   │       ├── rooms.py
│   │       ├── bookings.py
│   │       ├── reviews.py
│   │       └── webhooks.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── room.py
│   │   ├── booking.py
│   │   └── review.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── room.py
│   │   ├── booking.py
│   │   └── review.py
│   │
│   ├── services/
│   │
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md

⚙️ Instalação
1. Clonar repositório

git clone https://github.com/wilsondala/carved-homes-backend.git

2. Entrar na pasta do projeto
cd carved-homes-backend

3. Criar ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate

Linux / Mac
python3 -m venv venv
source venv/bin/activate

4. Instalar dependências
pip install -r requirements.txt


🛢️ Configuração PostgreSQL
Criar banco de dados
CREATE DATABASE carved_homes;

🔐 Configuração do .env

Criar arquivo:

.env

Conteúdo:

DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/carved_homes

SECRET_KEY=super_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

BACKEND_CORS_ORIGINS=["http://localhost:5173"]

JWT_SECRET_KEY=super_secret_key

JWT_ALGORITHM=HS256

Executar API
python -m uvicorn app.main:app --reload


🌐 Swagger Docs

Após iniciar o servidor:

http://127.0.0.1:8000/docs


Health Check

Endpoint:

/api/v1/health

Resposta:

{
  "status": "online",
  "service": "Carved Homes API"
}


🏠 Funcionalidades
Rooms
Criar quartos
Listar quartos
Atualizar quartos
Remover quartos
Bookings
Reservas
Gestão de hospedagem
Datas de check-in/check-out
Reviews
Avaliações
Sistema de comentários
Rating de hospedagem
Users
Cadastro
Login
JWT Authentication
🔒 Segurança
JWT Authentication
Password Hashing
CORS Protection
Environment Variables
SQLAlchemy ORM
🧱 Banco de Dados

Tabelas criadas automaticamente:

users
rooms
bookings
reviews
🚀 Deploy Futuro

Backend preparado para:

Render
Railway
Docker
Oracle Cloud
VPS Ubuntu
Nginx + Gunicorn/Uvicorn
📌 Estrutura Inicial Concluída

✅ FastAPI operacional
✅ PostgreSQL conectado
✅ SQLAlchemy funcionando
✅ Swagger online
✅ Rotas funcionando
✅ Health check funcionando
✅ Estrutura profissional criada

👨‍💻 Autor

Wilson Dala Ndembuza

📄 Licença

Este projeto é privado e desenvolvido para fins comerciais e profissionais.