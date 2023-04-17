from api import db
from ..models import produto_model


def cadastrar_produto(produto):
    produto_bd = produto_model.Produto(codigo=produto.codigo, descricao=produto.descricao, medida=produto.medida,
                                       unidade_medida=produto.unidade_medida, valor_custo=produto.valor_custo,
                                       quantidade_estoque=produto.quantidade_estoque, valor_venda=produto.valor_venda,
                                       cor=produto.cor, tipo=produto.tipo, fabricante=produto.fabricante,
                                       quantidade_min_estoque=produto.quantidade_min_estoque,
                                       fornecedor_id=produto.fornecedor_id)
    db.session.add(produto_bd)
    db.session.commit()


def listar_produtos():
    produtos = produto_model.Produto.query.all()
    return produtos


def listar_produto_id(id):
    produto = produto_model.Produto.query.filter_by(id=id).first()
    return produto


def atualizar_produto(produto_antigo, produto_novo):
    produto_antigo.codigo = produto_novo.codigo
    produto_antigo.descricao = produto_novo.descricao
    produto_antigo.medida = produto_novo.medida
    produto_antigo.unidade_medida = produto_novo.unidade_medida
    produto_antigo.valor_custo = produto_novo.valor_custo
    produto_antigo.quantidade_estoque = produto_novo.quantidade_estoque
    produto_antigo.valor_venda = produto_novo.valor_venda
    produto_antigo.cor = produto_novo.cor
    produto_antigo.tipo = produto_novo.tipo
    produto_antigo.fabricante = produto_novo.fabricante
    produto_antigo.quantidade_min_estoque = produto_novo.quantidade_min_estoque
    produto_antigo.fornecedor_id = produto_novo.fornecedor_id
    db.session.commit()


def remover_produto(produto):
    db.session.delete(produto)
    db.session.commit()
