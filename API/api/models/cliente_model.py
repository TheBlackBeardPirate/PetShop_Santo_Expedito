from api import db
from .animal_model import Animal


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    tel_resid = db.Column(db.String(10), nullable=False)
    tel_cel = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(8), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    # Usar db.Date no campo nascimento
    nascimento = db.Column(db.Date, nullable=False)
    is_premium = db.Column(db.Boolean, nullable=False)
    animais = db.relationship(Animal, backref='cliente')