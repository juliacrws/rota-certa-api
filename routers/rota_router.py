from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.rota_model import PedidoRota
from models import db_models
from services.rota_service import calcular_melhor_rota
from core.security import get_current_user_id # NOVO: Importamos o cadeado

router = APIRouter(tags=["Rotas"])

@router.post("/calcular-rota")
def calcular_rota(
    pedido: PedidoRota, 
    db: Session = Depends(get_db),
    usuario_id: int = Depends(get_current_user_id) # CADEADO ATIVADO AQUI!
):
    veiculo = db.query(db_models.Veiculo).filter(db_models.Veiculo.id == pedido.veiculo_id).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")

    # SUPER SEGURANÇA: Impede que a Ana calcule rota usando o caminhão do Roberto
    if veiculo.motorista_id != usuario_id:
        raise HTTPException(status_code=403, detail="Acesso negado. Este veículo não pertence a você.")

    resultado = calcular_melhor_rota(pedido.origem, pedido.destino, veiculo)

    if not resultado["sucesso"]:
        raise HTTPException(status_code=400, detail={"mensagem": "Rota bloqueada.", "motivos": resultado["alertas"]})

    return {
        "sucesso": resultado["sucesso"],
        "origem": pedido.origem,
        "destino": pedido.destino,
        "veiculo": veiculo.placa,
        "tipo_carga": veiculo.tipo_carga,
        "distancia_km": resultado["distancia_km"], 
        "tempo_estimado_horas": resultado["tempo_horas"], 
        "rota_sugerida": resultado["rota_sugerida"],
        "alertas": resultado["alertas"]
    }