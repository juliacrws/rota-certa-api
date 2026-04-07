from pydantic import BaseModel
from enum import Enum

# Criamos a lista restrita de categorias
class TipoCarga(str, Enum):
    GERAL = "geral"
    GRANEL = "granel"
    PERIGOSA = "perigosa"
    REFRIGERADA = "refrigerada"
    VIVA = "viva"
    INDIVISIVEL = "indivisivel"

class VeiculoCreate(BaseModel):
    placa: str
    peso_maximo_toneladas: float
    altura_metros: float
    tipo_carga: TipoCarga  # Agora só aceita os valores da lista acima
    motorista_id: int

class VeiculoResponse(BaseModel):
    id: int
    placa: str
    peso_maximo_toneladas: float
    altura_metros: float
    tipo_carga: TipoCarga
    motorista_id: int

    class Config:
        from_attributes = True