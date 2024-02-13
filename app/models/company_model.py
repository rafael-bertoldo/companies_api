from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Company(db.Model):
    id: int
    CNPJ: str
    nome_razao: str
    nome_fantasia: str
    CNAE: str


    id = db.Column(db.Integer, primary_key=True)
    CNPJ = db.Column(db.String(14), unique=True, nullable=False)
    nome_razao = db.Column(db.String(100), nullable=False)
    nome_fantasia = db.Column(db.String(100), nullable=False)
    CNAE = db.Column(db.String(10), nullable=False)
    

    def serialize(self):
        return {
            'id': self.id,
            'CNPJ': self.CNPJ,
            'nome_razao': self.nome_razao,
            'nome_fantasia': self.nome_fantasia,
            'CNAE': self.CNAE
        }