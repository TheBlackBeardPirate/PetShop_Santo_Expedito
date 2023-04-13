from api import db


class Veterinario(db.Model):
    __tablename__ = 'veterinario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    crmv = db.Column(db.String(8), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    tel_emergencia = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    hora_atendimento = db.Column(db.String(70), nullable=False)
    efetivo = db.Column(db.Boolean, nullable=False)
    valor_pagar = db.Column(db.Float, nullable=True)