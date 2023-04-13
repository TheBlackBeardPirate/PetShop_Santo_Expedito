from api import ma
from ..models import cliente_model
from marshmallow import fields


class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cliente_model.Cliente()
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ('id', 'nome', 'endereco', 'cidade', 'uf', 'cep', 'tel_resid', 'tel_cel', 'email', 'rg', 'cpf',
                  'nascimento', 'is_premium')

    nome = fields.String(required=True)
    endereco = fields.String(required=True)
    cidade = fields.String(required=True)
    uf = fields.String(required=True)
    cep = fields.String(required=True)
    tel_resid = fields.String(required=True)
    tel_cel = fields.String(required=True)
    email = fields.String(required=True)
    rg = fields.String(required=True)
    cpf = fields.String(required=True)
    nascimento = fields.Date(required=True)
    is_premium = fields.Boolean(required=True)