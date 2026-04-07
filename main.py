from fastapi import FastAPI
from routers import rota_router, motorista_router, veiculo_router, auth_router # NOVO: auth_router
from core.database import engine, Base
from models import db_models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rota Certa API - Professional Edition")

app.include_router(auth_router.router) # NOVO: Rota de login (geralmente colocamos primeiro)
app.include_router(rota_router.router)
app.include_router(motorista_router.router)
app.include_router(veiculo_router.router)

@app.get("/")
def home():
    return {"status": "Rota Certa API Blindada!"}