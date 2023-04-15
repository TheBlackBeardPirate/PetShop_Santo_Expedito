from api import ma
from ..models import animal_model
from marshmallow import fields


class AnimalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = animal_model.Animal()
        load_instance = True
        include_fk = True
        include_relationship = True
        fields = ('id', 'nome', 'raca', 'cor', 'idade', 'alergico', 'hora_comer', 'racao', 'registro', 'cliente_id')

    nome = fields.String(required=True)
    raca = fields.String(required=True)
    cor = fields.String(required=True)
    idade = fields.Integer(required=True)
    alergico = fields.Boolean(required=True)
    hora_comer = fields.String(required=True)
    racao = fields.String(required=True)
    registro = fields.String(required=True)
    cliente_id = fields.Integer(required=True)
