from api import api
from flask import make_response, jsonify, request
from flask_restful import Resource
from datetime import datetime
from ..entidades import consulta
from ..schemas import consulta_schema
from ..services import consulta_service
from ..decorator import admin_required


def valida_data(horario):
    nova_data = datetime.strptime(horario, '%Y-%m-%d %H:%M:%S')
    return nova_data


class ConsultaList(Resource):

    @admin_required()
    def get(self):
        consultas = consulta_service.listar_consultas()
        cs = consulta_schema.ConsultaSchema(many=True)
        # return paginate(Consulta, cs)
        return make_response(cs.jsonify(consultas), 200)

    @admin_required()
    def post(self):
        cs = consulta_schema.ConsultaSchema()
        validate = cs.validate(request.json)

        horario = request.json['horario']
        horario = valida_data(horario)

        if validate:
            return make_response(jsonify(validate), 400)

        # horario = request.json['horario']
        nome_cliente = request.json['nome_cliente']
        cpf_cliente = request.json['cpf_cliente']
        cliente_premium = request.json['cliente_premium']
        nome_animal = request.json['nome_animal']
        raca = request.json['raca']
        emergencia = request.json['emergencia']
        nome_vet = request.json['nome_vet']
        vet_efetivo = request.json['vet_efetivo']
        crmv = request.json['crmv']
        valor = request.json['valor']

        consulta_nova = consulta.Consulta(horario=horario, nome_cliente=nome_cliente, cpf_cliente=cpf_cliente,
                                          cliente_premium=cliente_premium, nome_animal=nome_animal, raca=raca,
                                          emergencia=emergencia, nome_vet=nome_vet, vet_efetivo=vet_efetivo,
                                          crmv=crmv, valor=valor)
        consulta_service.cadastrar_consulta(consulta_nova)
        return make_response(cs.jsonify(consulta_nova), 200)


class ConsultaDetail(Resource):

    @admin_required()
    def get(self, id):
        consulta_bd = consulta_service.listar_consulta_id(id=id)
        if consulta_bd is None:
            return make_response(jsonify('Consulta não encontrada!'), 404)

        cs = consulta_schema.ConsultaSchema()
        return make_response(cs.jsonify(consulta_bd), 200)

    @admin_required()
    def put(self, id):
        consulta_bd = consulta_service.listar_consulta_id(id=id)
        if consulta_bd is None:
            return make_response(jsonify('Consulta não encontrada!'), 404)

        horario = request.json['horario']
        horario = valida_data(horario)

        cs = consulta_schema.ConsultaSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        # horario = request.json['horario']
        nome_cliente = request.json['nome_cliente']
        cpf_cliente = request.json['cpf_cliente']
        cliente_premium = request.json['cliente_premium']
        nome_animal = request.json['nome_animal']
        raca = request.json['raca']
        emergencia = request.json['emergencia']
        nome_vet = request.json['nome_vet']
        vet_efetivo = request.json['vet_efetivo']
        crmv = request.json['crmv']
        valor = request.json['valor']

        consulta_nova = consulta.Consulta(horario=horario, nome_cliente=nome_cliente, cpf_cliente=cpf_cliente,
                                          cliente_premium=cliente_premium, nome_animal=nome_animal, raca=raca,
                                          emergencia=emergencia, nome_vet=nome_vet, vet_efetivo=vet_efetivo,
                                          crmv=crmv, valor=valor)
        consulta_service.editar_consulta(consulta_anterior=consulta_bd, consulta_nova=consulta_nova)
        return make_response(cs.jsonify(consulta_nova), 200)

    @admin_required()
    def delete(self, id):
        consulta_bd = consulta_service.listar_consulta_id(id=id)
        if consulta_bd is None:
            return make_response(jsonify('Consulta não encontrada!'), 404)

        consulta_service.remover_consulta(consulta_bd)
        return make_response(jsonify('Consulta removida com sucesso!'), 200)


api.add_resource(ConsultaList, '/consulta')
api.add_resource(ConsultaDetail, '/consulta/<int:id>')
