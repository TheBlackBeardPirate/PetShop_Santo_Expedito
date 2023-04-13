from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..entidades import animal
from ..services import animal_service
from ..schemas import animal_schema
from ..models.animal_model import Animal
from ..paginate import paginate


class AnimalList(Resource):
    def get(self):
        # animais = animal_service.listar_animal()
        asc = animal_schema.AnimalSchema(many=True)
        # return make_response(asc.jsonify(animais), 200)
        return paginate(Animal, asc)

    def post(self):
        asc = animal_schema.AnimalSchema()
        validate = asc.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        raca = request.json['raca']
        cor = request.json['cor']
        idade = request.json['idade']
        alergico = request.json['alergico']
        hora_comer = request.json['hora_comer']
        racao = request.json['racao']
        registro = request.json['registro']
        cliente_id = request.json['cliente_id']

        animal_novo = animal.Animal(nome=nome, raca=raca, cor=cor, idade=idade, alergico=alergico, hora_comer=hora_comer,
                                    racao=racao, registro=registro, cliente_id=cliente_id)

        animal_service.cadastrar_animal(animal_novo)
        return make_response(asc.jsonify(animal_novo), 200)


class AnimalDetail(Resource):
    def get(self, id):
        animal_bd = animal_service.listar_animal_id(id=id)
        if animal_bd is None:
            return make_response(jsonify('Animal não encontrado!'), 404)

        asc = animal_schema.AnimalSchema()
        return make_response(asc.jsonify(animal_bd), 200)

    def put(self, id):
        animal_bd = animal_service.listar_animal_id(id=id)
        if animal_bd is None:
            return make_response(jsonify('Animal não encontrado!'), 404)

        asc = animal_schema.AnimalSchema()
        validate = asc.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        raca = request.json['raca']
        cor = request.json['cor']
        idade = request.json['idade']
        alergico = request.json['alergico']
        hora_comer = request.json['hora_comer']
        racao = request.json['racao']
        registro = request.json['registro']
        cliente_id = request.json['cliente_id']

        animal_novo = animal.Animal(nome=nome, raca=raca, cor=cor, idade=idade, alergico=alergico,
                                    hora_comer=hora_comer, racao=racao, registro=registro, cliente_id=cliente_id)
        animal_service.atualizar_animal(animal_anterior=animal_bd, animal_novo=animal_novo)
        return make_response(asc.jsonify(animal_novo), 200)

    def delete(self,  id):
        animal_bd = animal_service.listar_animal_id(id=id)
        if animal_bd is None:
            return make_response(jsonify('Animal não encontrado!'), 404)

        animal_service.remove_animal(animal_bd)
        return make_response(jsonify('Animal excluído com sucesso!'), 200)


api.add_resource(AnimalList, '/animal')
api.add_resource(AnimalDetail, '/animal/<int:id>')