from api import api
from datetime import datetime
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..entidades import cliente
from ..services import cliente_service
from ..schemas import cliente_schema
from ..paginate import paginate
from ..models.cliente_model import Cliente


def valida_data(nascimento):
    teste = ' 01:55:19'
    nascimento = nascimento + teste
    nova_data = datetime.date(datetime.strptime(nascimento, '%Y-%m-%d %H:%M:%S'))
    return nova_data


class ClienteList(Resource):
    def get(self):
        # clientes = cliente_service.listar_clientes()
        cs = cliente_schema.ClienteSchema(many=True)
        # return make_response(cs.jsonify(clientes), 200)
        return paginate(Cliente, cs)

    def post(self):
        cs = cliente_schema.ClienteSchema()
        validate = cs.validate(request.json)

        # request.json retorna um objeto <str>
        # o método validate não consegue validar datas oriundas de objetos json

        nascimento = request.json['nascimento']
        nascimento = valida_data(nascimento)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        endereco = request.json['endereco']
        cidade = request.json['cidade']
        uf = request.json['uf']
        cep = request.json['cep']
        tel_resid = request.json['tel_resid']
        tel_cel = request.json['tel_cel']
        email = request.json['email']
        rg = request.json['rg']
        cpf = request.json['cpf']
        # nascimento = request.json['nascimento']
        is_premium = request.json['is_premium']

        cliente_novo = cliente.Cliente(nome=nome, endereco=endereco, cidade=cidade, uf=uf, cep=cep, tel_resid=tel_resid,
                                       tel_cel=tel_cel, email=email, rg=rg, cpf=cpf, nascimento=nascimento,
                                       is_premium=is_premium)
        cliente_service.cadastrar_cliente(cliente_novo)
        return make_response(cs.jsonify(cliente_novo), 200)


class ClienteDetail(Resource):
    def get(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id=id)
        if cliente_bd is None:
            return make_response(jsonify('Cliente não encontrado!'), 404)

        cs = cliente_schema.ClienteSchema()
        return make_response(cs.jsonify(cliente_bd), 200)

    def put(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify('Cliente não encontrado!'), 404)

        nascimento = request.json['nascimento']
        nascimento = valida_data(nascimento)

        cs = cliente_schema.ClienteSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        endereco = request.json['endereco']
        cidade = request.json['cidade']
        uf = request.json['uf']
        cep = request.json['cep']
        tel_resid = request.json['tel_resid']
        tel_cel = request.json['tel_cel']
        email = request.json['email']
        rg = request.json['rg']
        cpf = request.json['cpf']
        # nascimento = request.json['nascimento']
        is_premium = request.json['is_premium']

        cliente_novo = cliente.Cliente(nome=nome, endereco=endereco, cidade=cidade, uf=uf, cep=cep, tel_resid=tel_resid,
                                       tel_cel=tel_cel, email=email, rg=rg, cpf=cpf, nascimento=nascimento,
                                       is_premium=is_premium)
        cliente_service.atualizar_cliente(cliente_anterior=cliente_bd, cliente_novo=cliente_novo)
        return make_response(cs.jsonify(cliente_novo), 200)

    def delete(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id=id)
        if cliente_bd is None:
            return make_response(jsonify('Cliente não encontrado!'), 404)

        cliente_service.remover_cliente(cliente_bd)
        return make_response(jsonify('Cliente excluído com sucesso!'), 200)


api.add_resource(ClienteList, '/cliente')
api.add_resource(ClienteDetail, '/cliente/<int:id>')
