from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify, request
from .services import usuario_service


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['roles'] != 'admin':
                return make_response(jsonify(mensagem='Recurso destinado a administradores!'), 403)

            return fn(*args, **kwargs)

        return decorator
    return wrapper


def api_key_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            api_key = request.args.get('api_key')
            user_api_key = usuario_service.listar_usuario_api_key(api_key=api_key)
            if user_api_key and api_key:
                return fn(*args, **kwargs)

            return make_response(jsonify(mensagem='Forneça uma api_key válida para executar essa ação!'), 401)

        return decorator
    return wrapper
