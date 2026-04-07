from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models import db_models
from schemas import motorista_schema
from core.security import get_password_hash  # NOVO: Importamos nossa ferramenta de segurança

router = APIRouter(prefix="/motoristas", tags=["Motoristas"])

@router.post("/", response_model=motorista_schema.MotoristaResponse)
def criar_motorista(motorista: motorista_schema.MotoristaCreate, db: Session = Depends(get_db)):
    # 1. Verifica se o email já existe
    db_user = db.query(db_models.Motorista).filter(db_models.Motorista.email == motorista.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    # 2. CRIPTOGRAFIA: Embaralha a senha antes de tocar no banco de dados
    senha_criptografada = get_password_hash(motorista.senha)
    
    # 3. Cria a instância do modelo salvando a senha segura
    novo_motorista = db_models.Motorista(
        nome=motorista.nome,
        email=motorista.email,
        cpf=motorista.cpf,
        senha=senha_criptografada  # A senha limpa (ex: "123") morre aqui. Só o Hash vai pro banco.
    )
    
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista