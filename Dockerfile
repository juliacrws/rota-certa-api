# 1. Pega um "computador" Linux minúsculo que já tem o Python instalado
FROM python:3.11-slim

# 2. Cria uma pasta chamada /app dentro desse computador e entra nela
WORKDIR /app

# 3. Copia APENAS o arquivo de requisitos primeiro (isso deixa o Docker mais rápido)
COPY requirements.txt .

# 4. Instala as bibliotecas do projeto dentro do computador virtual
RUN pip install --no-cache-dir -r requirements.txt

# 5. Agora sim, copia todo o resto do seu código para dentro do /app
COPY . .

# 6. Avisa que o servidor vai conversar com o mundo externo pela porta 8000
EXPOSE 8000

# 7. O comando que o Docker vai rodar assim que for ligado
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]