from pydantic import BaseModel

class PedidoRota(BaseModel):
    origem: str
    destino: str
    veiculo_id: int  # Trocamos altura/peso/carga apenas pelo ID do caminhão