from api import ma
from ..models import usuario_model
from marshmallow import fields


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario()
        load_instance = True
        fields = ('id', 'nome', 'endereco', 'cidade', 'uf', 'cep', 'tel_resid', 'tel_cel', 'email', 'rg', 'cpf',
                  'nascimento', 'senha', 'is_admin', 'api_key')

    nome = fields.String(required=False)
    endereco = fields.String(required=False)
    cidade  = fields.String(required=False)
    uf = fields.String(required=False)
    cep = fields.String(required=False)
    tel_resid = fields.String(required=False)
    tel_cel = fields.String(required=False)
    email = fields.String(required=False)
    rg = fields.String(required=False)
    cpf = fields.String(required=False)
    nascimento = fields.Date(required=False)
    senha = fields.String(required=False)
    is_admin = fields.Boolean(required=False)
    api_key = fields.String(required=False)
