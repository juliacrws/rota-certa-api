import requests

def obter_coordenadas(cidade: str):
    url = f"https://nominatim.openstreetmap.org/search?q={cidade}&format=json&limit=1"
    # Melhorando o User-Agent para o OpenStreetMap não achar que somos um ataque de spam
    headers = {"User-Agent": "RotaCertaAPI_Estudo_FIAP/1.0"} 
    
    try:
        # TIMEOUT: Se demorar mais de 10 segundos, desiste e não trava a API
        resposta = requests.get(url, headers=headers, timeout=10)
        if resposta.status_code == 200 and len(resposta.json()) > 0:
            dados = resposta.json()[0]
            return float(dados["lat"]), float(dados["lon"])
    except Exception as e:
        print(f"Erro ao buscar coordenadas de {cidade}: {e}")
        
    return None, None

def calcular_distancia_tempo_real(lat_origem, lon_origem, lat_destino, lon_destino):
    url = f"http://router.project-osrm.org/route/v1/driving/{lon_origem},{lat_origem};{lon_destino},{lat_destino}?overview=false"
    
    try:
        # TIMEOUT de 10 segundos aqui também
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            dados = resposta.json()
            if dados.get("code") == "Ok":
                rota = dados["routes"][0]
                distancia_km = rota["distance"] / 1000 
                tempo_horas = (rota["duration"] / 60) / 60 
                return round(distancia_km, 2), round(tempo_horas, 2)
    except Exception as e:
        print(f"Erro ao calcular rota no OSRM: {e}")
        
    return None, None