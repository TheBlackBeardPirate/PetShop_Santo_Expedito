from api import api
from flask_restful import Resource
from flask import make_response, request, jsonify
from ..schemas import produto_schema
from ..models.produto_model import Produto
from ..entidades import produto
from ..services import produto_service
from ..paginate import paginate
from ..decorator import admin_required


class ProdutoList(Resource):
    def get(self):
        ps = produto_schema.ProdutoSchema(many=True)
        return paginate(Produto, ps)
        # produtos = produto_service.listar_produtos()
        # return make_response(ps.jsonify(produtos), 200)

    @admin_required()
    def post(self):
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        codigo = request.json['codigo']
        descricao = request.json['descricao']
        unidade_medida = request.json['unidade_medida']
        medida = request.json['medida']
        quantidade_estoque = request.json['quantidade_estoque']
        valor_custo = request.json['valor_custo']
        valor_venda = request.json['valor_venda']
        cor = request.json['cor']
        tipo = request.json['tipo']
        fabricante = request.json['fabricante']
        quantidade_min_estoque = request.json['quantidade_min_estoque']
        fornecedor_id = request.json['fornecedor_id']

        produto_novo = produto.Produto(codigo=codigo, descricao=descricao, unidade_medida=unidade_medida, medida=medida,
                                       quantidade_estoque=quantidade_estoque, valor_custo=valor_custo, tipo=tipo,
                                       valor_venda=valor_venda, cor=cor, fabricante=fabricante,
                                       quantidade_min_estoque=quantidade_min_estoque, fornecedor_id=fornecedor_id)
        produto_service.cadastrar_produto(produto_novo)
        return make_response(ps.jsonify(produto_novo), 200)


class ProdutoDetail(Resource):
    def get(self, id):
        produto_bd = produto_service.listar_produto_id(id=id)
        if produto_bd is None:
            return make_response(jsonify('Produto não encontrado!'), 404)

        ps = produto_schema.ProdutoSchema()
        return make_response(ps.jsonify(produto_bd), 200)

    @admin_required()
    def put(self, id):
        produto_bd = produto_service.listar_produto_id(id=id)
        if produto_bd is None:
            return make_response(jsonify('Produto não encontrado!'), 404)

        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        codigo = request.json['codigo']
        descricao = request.json['descricao']
        unidade_medida = request.json['unidade_medida']
        medida = request.json['medida']
        quantidade_estoque = request.json['quantidade_estoque']
        valor_custo = request.json['valor_custo']
        valor_venda = request.json['valor_venda']
        cor = request.json['cor']
        tipo = request.json['tipo']
        fabricante = request.json['fabricante']
        quantidade_min_estoque = request.json['quantidade_min_estoque']
        fornecedor_id = request.json['fornecedor_id']

        produto_novo = produto.Produto(codigo=codigo, descricao=descricao, unidade_medida=unidade_medida, medida=medida,
                                       quantidade_estoque=quantidade_estoque, valor_custo=valor_custo, tipo=tipo,
                                       valor_venda=valor_venda, cor=cor, fabricante=fabricante,
                                       quantidade_min_estoque=quantidade_min_estoque, fornecedor_id=fornecedor_id)
        produto_service.atualizar_produto(produto_antigo=produto_bd, produto_novo=produto_novo)
        return make_response(ps.jsonify(produto_novo), 200)

    @admin_required()
    def delete(self, id):
        produto_bd = produto_service.listar_produto_id(id=id)
        if produto_bd is None:
            return make_response(jsonify('Produto não encontrado!'), 404)

        produto_service.remover_produto(produto_bd)
        return make_response(jsonify('Produto removido com sucesso!'), 200)


api.add_resource(ProdutoList, '/produto')
api.add_resource(ProdutoDetail, '/produto/<int:id>')
