from api import api
from flask_restful import Resource
from datetime import datetime
from flask import make_response, jsonify, request
from ..services import controle_service
from ..models import venda_model


class ControleList(Resource):
    def post(self):
        nf = []
        ids = []
        quant = []
        custo = 0.0
        total = 0.0
        cpf_cliente = request.json['cpf_cliente']
        met_pagamento = request.json['met_pagamento']
        codigos = request.json['codigo'].split()
        qtds = request.json['qtd'].split()
        tam = len(codigos)
        for i in range(tam):
            item = {
                'nome': controle_service.nome_produto_codigo(codigos[i]),
                'valor_unitario': controle_service.valor_venda_produto_codigo(codigos[i]),
                'valor_total': controle_service.valor_venda_produto_codigo(codigos[i]) * int(qtds[i])
            }
            ids.append(controle_service.id_produto_codigo(codigos[i]))
            quant.append(int(qtds[i]))
            nf.append(item)
            total += item['valor_total']
            controle_service.atualiza_estoque(codigos[i], int(qtds[i]))

        tam = len(ids)
        for id in range(tam):
            custo += (controle_service.valor_custo_produto_id(id=ids[id]) * quant[id])

        cliente_id = controle_service.id_cliente_cpf(cpf_cliente)
        lucro = total - custo

        venda = venda_model.Venda(cliente_id=cliente_id, valor_total=total, valor_custo=custo, valor_lucro=lucro,
                                  met_pagamento=met_pagamento, data_hora=datetime.now())
        controle_service.venda_realizada(venda=venda)

        return make_response(jsonify(nf, total), 200)


api.add_resource(ControleList, '/produto/controle')
