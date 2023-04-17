from api import db
from .produto_model import Produto


class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    produtos = db.relationship(Produto, backref='fornecedor')
