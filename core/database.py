from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão. Aqui definimos o SQLite para desenvolvimento rápido.
# No futuro, mudaremos apenas esta linha para a URL do PostgreSQL.
SQLALCHEMY_DATABASE_URL = "sqlite:///./rota_certa.db"

# Criando o motor de conexão
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # Exigência apenas do SQLite
)

# Sessão do banco (como se fosse a "janela" de comunicação aberta)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base que usaremos para criar nossas tabelas depois
Base = declarative_base()

# Função que o FastAPI vai usar para abrir e fechar a conexão a cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()