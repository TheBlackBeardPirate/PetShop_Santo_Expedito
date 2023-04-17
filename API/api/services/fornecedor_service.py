from api import db
from ..models import fornecedor_model


def cadastrar_fornecedor(fornecedor):
    fornecedor_bd = fornecedor_model.Fornecedor(nome=fornecedor.nome, cnpj=fornecedor.cnpj, endereco=fornecedor.endereco,
                                                cidade=fornecedor.cidade, uf=fornecedor.uf, cep=fornecedor.cep,
                                                telefone=fornecedor.telefone, email=fornecedor.email)
    db.session.add(fornecedor_bd)
    db.session.commit()


def listar_fornecedor_id(id):
    fornecedor = fornecedor_model.Fornecedor.query.filter_by(id=id).first()
    return fornecedor


def atualizar_fornecedor(fornecedor_antigo, fornecedor_novo):
    fornecedor_antigo.nome = fornecedor_novo.nome
    fornecedor_antigo.cnpj = fornecedor_novo.cnpj
    fornecedor_antigo.endereco = fornecedor_novo.endereco
    fornecedor_antigo.cidade =  fornecedor_novo.cidade
    fornecedor_antigo.uf = fornecedor_novo.uf
    fornecedor_antigo.cep = fornecedor_novo.cep
    fornecedor_antigo.telefone = fornecedor_novo.telefone
    fornecedor_antigo.email = fornecedor_novo.email
    db.session.commit()


def remover_fornecedor(fornecedor):
    db.session.delete(fornecedor)
    db.session.commit()
