from api import ma
from marshmallow import fields
from ..models import fornecedor_model


class FornecedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = fornecedor_model.Fornecedor()
        load_instance = True
        include_fk = True
        include_relationship = True
        fields = ('id', 'nome', 'cnpj', 'endereco', 'cidade', 'uf', 'cep', 'telefone', 'email')

    nome = fields.String(required=True)
    cnpj = fields.String(required=True)
    endereco = fields.String(required=True)
    cidade = fields.String(required=True)
    uf = fields.String(required=True)
    cep = fields.String(required=True)
    telefone = fields.String(required=True)
    email = fields.String(required=True)
