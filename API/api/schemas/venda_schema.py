from api import ma
from ..models import venda_model
from marshmallow import fields


class VendaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = venda_model.Venda()
        load_instance = True
        include_fk = True
        include_relationship = True
        fields = ('id', 'cliente_id', 'valor_total', 'valor_custo', 'valor_lucro', 'met_pagamento', 'data_hora')

    valor_total = fields.Float(required=True)
    valor_custo = fields.Float(required=True)
    valor_lucro = fields.Float(required=True)
    met_pagamento = fields.String(required=True)
    data_hora = fields.DateTime(required=True)
    cliente_id = fields.Integer(required=True)
