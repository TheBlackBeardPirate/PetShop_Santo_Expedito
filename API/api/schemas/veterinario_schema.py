from api import ma
from ..models import veterinario_model
from marshmallow import fields


class VeterinarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = veterinario_model.Veterinario()
        load_instance = True
        fields = ('id', 'nome', 'crmv',  'endereco', 'cidade', 'uf', 'cep', 'tel_emergencia', 'email',
                  'hora_atendimento', 'efetivo', 'valor_pagar')

    nome = fields.String(required=True)
    crmv = fields.String(required=True)
    endereco = fields.String(required=True)
    cidade = fields.String(required=True)
    uf  = fields.String(required=True)
    cep = fields.String(required=True)
    tel_emergencia = fields.String(required=True)
    email = fields.String(required=True)
    hora_atendimento = fields.String(required=True)
    efetivo = fields.Boolean(required=True)
    valor_pagar = fields.Float(required=True)