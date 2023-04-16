import uuid
from flask_restful import Resource
from datetime import datetime
from flask import jsonify, make_response, request
from api import api
from ..schemas import usuario_schema
from ..entidades import usuario
from ..services import usuario_service
from ..decorator import admin_required


def valida_data(nascimento):
    teste = ' 01:55:19'
    nascimento = nascimento + teste
    nova_data = datetime.date(datetime.strptime(nascimento, '%Y-%m-%d %H:%M:%S'))
    return nova_data


class UsuarioList(Resource):

    @admin_required()
    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)

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
        senha = request.json['senha']
        is_admin = request.json['is_admin']
        api_key = str(uuid.uuid4())

        usuario_novo = usuario.Usuario(nome, endereco, cidade, uf, cep, tel_resid, tel_cel, email, rg, cpf, nascimento,
                                       senha, is_admin, api_key)
        usuario_service.cadastrar_usuario(usuario_novo)
        return make_response(us.jsonify(usuario_novo), 200)


class UsuarioDetail(Resource):

    @admin_required()
    def get(self, id):
        usuario_bd = usuario_service.listar_usuario_id(id=id)
        if usuario_bd is None:
            return make_response(jsonify('Usuario não encontrado!'), 404)

        us = usuario_schema.UsuarioSchema()
        return make_response(us.jsonify(usuario_bd), 200)

    @admin_required()
    def put(self, id):
        usuario_bd = usuario_service.listar_usuario_id(id)
        if usuario_bd is None:
            return make_response(jsonify('Usuario não encontrado!'), 404)

        nascimento = request.json['nascimento']
        nascimento = valida_data(nascimento)

        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
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
        senha = request.json['senha']
        is_admin = request.json['is_admin']
        api_key = str(uuid.uuid4())

        usuario_novo = usuario.Usuario(nome, endereco, cidade, uf, cep, tel_resid, tel_cel, email, rg, cpf, nascimento,
                                       senha, is_admin, api_key)
        usuario_service.atualizar_usuario(usuario_antigo=usuario_bd, usuario_novo=usuario_novo)
        return make_response(us.jsonify(usuario_novo), 200)

    @admin_required()
    def delete(self, id):
        usuario_bd = usuario_service.listar_usuario_id(id=id)
        if usuario_bd is None:
            return make_response(jsonify('Cliente não encontrado!'), 404)

        usuario_service.remover_usuario(usuario_bd)
        return make_response(jsonify('Usuário excluído com sucesso!'), 200)


api.add_resource(UsuarioList, '/usuario')
api.add_resource(UsuarioDetail, '/usuario/<int:id>')
