from api import db
from ..models import produto_model, cliente_model, venda_model


def id_produto_codigo(codigo):
    produto_db = produto_model.Produto.query.filter_by(codigo=codigo).first()
    return produto_db.id


def id_cliente_cpf(cpf):
    cliente_bd = cliente_model.Cliente.query.filter_by(cpf=cpf).first()
    return cliente_bd.id


def nome_produto_codigo(codigo):
    produto_db = produto_model.Produto.query.filter_by(codigo=codigo).first()
    # produto_db = db.session.query(produto_model.Produto.descricao).filter(produto_model.Produto.codigo == codigo)
    return produto_db.descricao


def valor_venda_produto_codigo(codigo):
    produto_db = produto_model.Produto.query.filter_by(codigo=codigo).first()
    # produto_db = db.session.query(produto_model.Produto.valor_venda).filter(produto_model.Produto.codigo == codigo)
    return produto_db.valor_venda


def valor_custo_produto_id(id):
    produto_db = produto_model.Produto.query.filter_by(id=id).first()
    return produto_db.valor_custo


def venda_realizada(venda):
    nova_venda = venda_model.Venda(cliente_id=venda.cliente_id, valor_total=venda.valor_total,
                                   data_hora=venda.data_hora, met_pagamento=venda.met_pagamento,
                                   valor_lucro=venda.valor_lucro, valor_custo=venda.valor_custo)
    db.session.add(nova_venda)
    db.session.commit()


def atualiza_estoque(codigo, qtd):
    produto_db = produto_model.Produto.query.filter_by(codigo=codigo).first()
    # produto_db = db.session.query(produto_model.Produto).filter_by(produto_model.Produto.codigo == codigo)
    produto_db.quantidade_estoque -= qtd
    db.session.commit()
