from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models import db_models
from schemas import veiculo_schema

router = APIRouter(prefix="/veiculos", tags=["Veículos"])

@router.post("/", response_model=veiculo_schema.VeiculoResponse)
def cadastrar_veiculo(veiculo: veiculo_schema.VeiculoCreate, db: Session = Depends(get_db)):
    # 1. Checa se o motorista dono do caminhão realmente existe
    motorista = db.query(db_models.Motorista).filter(db_models.Motorista.id == veiculo.motorista_id).first()
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado no sistema.")
    
    # 2. Checa se a placa já existe
    db_veiculo = db.query(db_models.Veiculo).filter(db_models.Veiculo.placa == veiculo.placa).first()
    if db_veiculo:
        raise HTTPException(status_code=400, detail="Placa já cadastrada.")

    # 3. Salva no banco
    novo_veiculo = db_models.Veiculo(**veiculo.model_dump())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    
    return novo_veiculo