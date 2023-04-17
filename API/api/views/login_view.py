from api import api, jwt
from flask import make_response, jsonify, request
from flask_restful import Resource
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from ..services import usuario_service
from ..schemas import login_schema


class LoginList(Resource):

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        usuario_token = usuario_service.listar_usuario_id(identity)
        if usuario_token.is_admin:
            roles = 'admin'
        else:
            roles = 'user'
        return {'roles': roles}

    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        email = request.json['email']
        senha = request.json['senha']

        usuario_bd = usuario_service.listar_usuario_email(email=email)
        if usuario_bd is None:
            return make_response(jsonify('Usuário não encontrado!'), 404)

        if not usuario_bd.decrip_senha(senha=senha):
            return make_response(jsonify('Senha incorreta!'), 401)

        access_token = create_access_token(identity=usuario_bd.id, expires_delta=timedelta(seconds=300))

        refresh_token = create_refresh_token(identity=usuario_bd.id)

        return make_response(jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'message': 'Login realizado com sucesso!'
        }), 200)


api.add_resource(LoginList, '/login')
