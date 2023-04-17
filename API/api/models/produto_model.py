from api import db


class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    unidade_medida = db.Column(db.String(20), nullable=False)
    medida = db.Column(db.Float, nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False)
    valor_custo = db.Column(db.Float, nullable=False)
    valor_venda = db.Column(db.Float, nullable=False)
    cor = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    fabricante = db.Column(db.String(50), nullable=False)
    quantidade_min_estoque = db.Column(db.Integer, nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))
    # Sugerir data de validade
