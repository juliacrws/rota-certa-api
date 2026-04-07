from models.db_models import Veiculo
from services.mapa_service import obter_coordenadas, calcular_distancia_tempo_real

def calcular_melhor_rota(origem: str, destino: str, veiculo: Veiculo) -> dict:
    rota_escolhida = f"Rota processada de {origem} para {destino}."
    alertas = []
    
    # 1. BUSCA DE DADOS GEOGRÁFICOS REAIS
    lat_orig, lon_orig = obter_coordenadas(origem)
    lat_dest, lon_dest = obter_coordenadas(destino)
    
    distancia = 0.0
    tempo = 0.0
    
    if lat_orig and lat_dest:
        distancia, tempo = calcular_distancia_tempo_real(lat_orig, lon_orig, lat_dest, lon_dest)
        if distancia:
            rota_escolhida += f" Distância real: {distancia} km. Tempo estimado: {tempo} horas."
        else:
            alertas.append("Aviso: Não foi possível calcular a distância exata via satélite.")
    else:
        alertas.append("Aviso: Cidades não localizadas no mapa. Usando cálculo base.")

    # 2. BLOQUEIOS (Limites Físicos)
    if veiculo.peso_maximo_toneladas > 60.0 or veiculo.altura_metros > 5.0:
        return {
            "sucesso": False,
            "rota_sugerida": "NENHUMA ROTA VIÁVEL.",
            "distancia_km": 0.0,
            "tempo_horas": 0.0,
            "alertas": ["BLOQUEIO: Veículo excede limites absolutos da malha viária."]
        }

    # 3. CONFORMIDADE E TIPO DE CARGA
    if veiculo.altura_metros > 4.4:
        rota_escolhida += " [DESVIO DE VIADUTOS]"
        alertas.append("Atenção: Altura requer desvios.")
        
    if veiculo.tipo_carga == "perigosa":
        rota_escolhida += " [EVITANDO MANANCIAIS]"
    elif veiculo.tipo_carga == "viva":
        rota_escolhida += " [PARADAS SOMBREADAS]"
    elif veiculo.tipo_carga == "refrigerada":
        rota_escolhida += " [ASFALTO PREMIUM]"

    return {
        "sucesso": True,
        "rota_sugerida": rota_escolhida,
        "distancia_km": distancia or 0.0,
        "tempo_horas": tempo or 0.0,
        "alertas": alertas
    }