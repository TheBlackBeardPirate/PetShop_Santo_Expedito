from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..entidades import veterinario
from ..schemas import veterinario_schema
from ..services import veterinario_service
from ..paginate import paginate
from ..models.veterinario_model import Veterinario
from ..decorator import admin_required


class VeterinarioList(Resource):

    @admin_required()
    def get(self):
        vs = veterinario_schema.VeterinarioSchema(many=True)
        return paginate(Veterinario, vs)

    @admin_required()
    def post(self):
        vs = veterinario_schema.VeterinarioSchema()
        validate = vs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        crmv = request.json['crmv']
        endereco = request.json['endereco']
        cidade = request.json['cidade']
        uf = request.json['uf']
        cep = request.json['cep']
        tel_emergencia = request.json['tel_emergencia']
        email = request.json['email']
        hora_atendimento = request.json['hora_atendimento']
        efetivo = request.json['efetivo']
        valor_pagar = request.json['valor_pagar']

        vet_novo = veterinario.Veterinario(nome=nome, crmv=crmv, endereco=endereco, cidade=cidade, uf=uf, cep=cep,
                                           tel_emergencia=tel_emergencia, email=email,
                                           hora_atendimento=hora_atendimento,
                                           efetivo=efetivo, valor_pagar=valor_pagar)
        veterinario_service.cadastrar_veterinario(vet_novo)
        return make_response(vs.jsonify(vet_novo), 200)


class VeterinarioDetail(Resource):
    @admin_required()
    def get(self, id):
        vet_bd = veterinario_service.listar_veterinario_id(id=id)

        if vet_bd is None:
            return make_response(jsonify('Veterinário não encontrado!'), 404)

        vs = veterinario_schema.VeterinarioSchema()
        return make_response(vs.jsonify(vet_bd), 200)

    @admin_required()
    def put(self, id):
        vet_bd = veterinario_service.listar_veterinario_id(id=id)

        if vet_bd is None:
            return make_response(jsonify('Veterinário não encontrado!'), 404)

        vs = veterinario_schema.VeterinarioSchema()
        validate = vs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        crmv = request.json['crmv']
        endereco = request.json['endereco']
        cidade = request.json['cidade']
        uf = request.json['uf']
        cep = request.json['cep']
        tel_emergencia = request.json['tel_emergencia']
        email = request.json['email']
        hora_atendimento = request.json['hora_atendimento']
        efetivo = request.json['efetivo']
        valor_pagar = request.json['valor_pagar']

        if not efetivo and (valor_pagar is None or valor_pagar <= 0.0):
            return make_response(jsonify('O atendimento por Médico veterinário não efetivo deve gerar taxa de '
                                         'utilização da clínica e dos produtos e equipamentos consumidos e utilizados!'),
                                 400)

        vet_novo = veterinario.Veterinario(nome=nome, crmv=crmv, endereco=endereco, cidade=cidade, uf=uf, cep=cep,
                                           tel_emergencia=tel_emergencia, email=email,
                                           hora_atendimento=hora_atendimento,
                                           efetivo=efetivo, valor_pagar=valor_pagar)
        veterinario_service.atualizar_veterinario(vet_anterior=vet_bd, vet_novo=vet_novo)
        return make_response(vs.jsonify(vet_novo), 200)

    @admin_required()
    def delete(self, id):
        vet_bd = veterinario_service.listar_veterinario_id(id=id)

        if vet_bd is None:
            return make_response(jsonify('Veterinário não encontrado!'), 404)

        veterinario_service.remove_veterinario(vet_bd)
        return make_response(jsonify('Veterinário excluído com sucesso!'), 200)


api.add_resource(VeterinarioList, '/veterinario')
api.add_resource(VeterinarioDetail, '/veterinario/<int:id>')
