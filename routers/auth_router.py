from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.database import get_db
from models import db_models
from core.security import verify_password, create_access_token
from schemas.token_schema import Token

router = APIRouter(tags=["Autenticação"])

@router.post("/login", response_model=Token)
def login_para_obter_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # O formulário padrão do FastAPI usa o nome 'username', então vamos usá-lo para buscar o nosso 'email'
    motorista = db.query(db_models.Motorista).filter(db_models.Motorista.email == form_data.username).first()
    
    # Se não achou o email, ou se a senha estiver errada (comparamos a senha limpa com o Hash do banco)
    if not motorista or not verify_password(form_data.password, motorista.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Se passou pelas travas, criamos o Token guardando o ID do motorista dentro dele
    token = create_access_token(data={"sub": str(motorista.id)})
    
    return {"access_token": token, "token_type": "bearer"}