from api import ma
from marshmallow import fields
from ..models import consulta_model


class ConsultaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = consulta_model.Consulta()
        load_instance = True
        fields = ('id', 'horario', 'nome_cliente', 'cpf_cliente', 'cliente_premium', 'nome_animal', 'raca',
                  'emergencia', 'nome_vet', 'vet_efetivo', 'crmv', 'valor')

    horario = fields.DateTime(required=True)
    nome_cliente = fields.String(required=True)
    cpf_cliente = fields.String(required=True)
    cliente_premium = fields.Boolean(required=True)
    nome_animal = fields.String(required=True)
    raca = fields.String(required=True)
    emergencia = fields.Boolean(required=True)
    nome_vet = fields.String(required=True)
    vet_efetivo = fields.Boolean(required=True)
    crmv = fields.String(required=True)
    valor = fields.Float(required=True)
