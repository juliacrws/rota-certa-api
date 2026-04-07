from pydantic import BaseModel, EmailStr

class MotoristaCreate(BaseModel):
    nome: str
    email: str
    cpf: str
    senha: str

class MotoristaResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True