from api import db


class Consulta(db.Model):
    __tablename__ = 'consulta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    horario = db.Column(db.DateTime, nullable=False)
    nome_cliente = db.Column(db.String(100), nullable=False)
    cpf_cliente = db.Column(db.String(11), nullable=False)
    cliente_premium = db.Column(db.Boolean, nullable=False)
    nome_animal = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(50), nullable=False)
    emergencia = db.Column(db.Boolean, nullable=False)
    nome_vet = db.Column(db.String(100), nullable=False)
    vet_efetivo = db.Column(db.Boolean, nullable=False)
    crmv = db.Column(db.String(8), nullable=False)
    valor = db.Column(db.Float, nullable=False)
