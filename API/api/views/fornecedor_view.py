from api import api
from flask import request, make_response, jsonify
from flask_restful import Resource
from ..entidades import fornecedor
from ..models.fornecedor_model import Fornecedor
from ..schemas import fornecedor_schema
from ..services import fornecedor_service
from ..decorator import admin_required
from ..paginate import paginate


class FornecedorList(Resource):

    @admin_required()
    def get(self):
        fs = fornecedor_schema.FornecedorSchema(many=True)
        return paginate(Fornecedor, fs)

    @admin_required()
    def post(self):
        fs = fornecedor_schema.FornecedorSchema()
        validate = fs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        cnpj = request.json['cnpj']
        endereco = request.json['endereco']
        cidade = request.json['cidade']
        uf = request.json['uf']
        cep = request.json['cep']
        telefone = request.json['telefone']
        email = request.json['email']

        fornecedor_novo = fornecedor.Fornecedor(nome=nome, cnpj=cnpj, endereco=endereco, cidade=cidade, uf=uf, cep=cep,
                                                telefone=telefone, email=email)
        fornecedor_service.cadastrar_fornecedor(fornecedor_novo)
        return make_response(fs.jsonify(fornecedor_novo), 200)


class FornecedorDetail(Resource):

    @admin_required()
    def get(self, id):
        fornecedor_bd = fornecedor_service.listar_fornecedor_id(id=id)
        if fornecedor_bd is None:
            return make_response(jsonify('Fornecedor não encontrado!'), 404)

        fs = fornecedor_schema.FornecedorSchema()
        return make_response(fs.jsonify(fornecedor_bd), 200)

    @admin_required()
    def put(self, id):
        fornecedor_bd = fornecedor_service.listar_fornecedor_id(id=id)
        if fornecedor_bd is None:
            return make_response(jsonify('Fornecedor não encontrado!'), 404)

        fs = fornecedor_schema.FornecedorSchema()
        validate = fs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        cnpj = request.json['cnpj']
        endereco = request.json['endereco']
        cidade = request.json['cidade']
        uf = request.json['uf']
        cep = request.json['cep']
        telefone = request.json['telefone']
        email = request.json['email']

        fornecedor_novo = fornecedor.Fornecedor(nome=nome, cnpj=cnpj, endereco=endereco, cidade=cidade, uf=uf, cep=cep,
                                                telefone=telefone, email=email)
        fornecedor_service.atualizar_fornecedor(fornecedor_antigo=fornecedor_bd, fornecedor_novo=fornecedor_novo)
        return make_response(fs.jsonify(fornecedor_novo), 200)

    @admin_required()
    def delete(self, id):
        fornecedor_bd = fornecedor_service.listar_fornecedor_id(id=id)
        if fornecedor_bd is None:
            return make_response(jsonify('Fornecedor não encontrado!'), 404)

        fornecedor_service.remover_fornecedor(fornecedor_bd)
        return make_response(jsonify('Fornecedor excluído com sucesso!'), 200)


api.add_resource(FornecedorList, '/fornecedor')
api.add_resource(FornecedorDetail, '/fornecedor/<int:id>')
