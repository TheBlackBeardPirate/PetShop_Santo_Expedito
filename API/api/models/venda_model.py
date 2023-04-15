from api import db


class Venda(db.Model):
    __tablename__ = 'venda'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    valor_custo = db.Column(db.Float, nullable=False)
    valor_lucro = db.Column(db.Float, nullable=False)
    met_pagamento = db.Column(db.String(50), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
