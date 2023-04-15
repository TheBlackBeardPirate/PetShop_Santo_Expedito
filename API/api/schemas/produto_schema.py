from api import ma
from ..models import produto_model
from marshmallow import fields


class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = produto_model.Produto()
        load_instance = True
        include_fk = True
        include_relationship = True
        fields = ('id', 'codigo', 'descricao', 'unidade_medida', 'medida', 'quantidade_estoque', 'valor_custo',
                  'valor_venda', 'cor', 'tipo', 'fabricante', 'quantidade_min_estoque')

    codigo = fields.String(required=True)
    descricao = fields.String(required=True)
    unidade_medida = fields.String(required=True)
    medida = fields.Float(required=True)
    quantidade_estoque = fields.Integer(required=True)
    valor_custo = fields.Float(required=True)
    valor_venda = fields.Float(required=True)
    cor = fields.String(required=True)
    tipo = fields.String(required=True)
    fabricante = fields.String(required=True)
    quantidade_min_estoque = fields.Integer(required=True)
    # fornecedor_id = fields.Integer(required=True)
    # Sugerir data de validade
