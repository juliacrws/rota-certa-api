from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Motorista(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True)
    senha = Column(String)

    # Relacionamento: Um motorista tem veículos
    veiculos = relationship("Veiculo", back_populates="dono")

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, index=True)
    peso_maximo_toneladas = Column(Float)
    altura_metros = Column(Float)
    tipo_carga = Column(String)
    
    # A Chave Estrangeira liga o caminhão ao ID do motorista
    motorista_id = Column(Integer, ForeignKey("motoristas.id"))
    
    # Relacionamento: O veículo pertence a um motorista
    dono = relationship("Motorista", back_populates="veiculos")