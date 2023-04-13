from api import db


class Animal(db.Model):
    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    alergico = db.Column(db.Boolean, nullable=False)
    hora_comer = db.Column(db.String(50), nullable=False)
    racao = db.Column(db.String(50), nullable=False)
    registro = db.Column(db.String(50), nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    # cliente_id = db.Column(db.Integer, db.ForeignKey(cliente_model.Cliente.id))
    # cliente = db.relationship(cliente_model.Cliente, backref=db.backref('animal', lazy='dynamic'))