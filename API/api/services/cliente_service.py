from api import db
from ..models import cliente_model


def cadastrar_cliente(cliente):
    cliente_bd = cliente_model.Cliente(nome=cliente.nome, endereco=cliente.endereco, cidade=cliente.cidade,
                                       uf=cliente.uf, cep=cliente.cep, tel_resid=cliente.tel_resid,
                                       tel_cel=cliente.tel_cel, email=cliente.email, rg=cliente.rg, cpf=cliente.cpf,
                                       nascimento=cliente.nascimento, is_premium=cliente.is_premium)
    db.session.add(cliente_bd)
    db.session.commit()


def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes


def listar_cliente_id(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente


def atualizar_cliente(cliente_anterior, cliente_novo):
    cliente_anterior.nome = cliente_novo.nome
    cliente_anterior.endereco = cliente_novo.endereco
    cliente_anterior.cidade = cliente_novo.cidade
    cliente_anterior.uf = cliente_novo.uf
    cliente_anterior.cep = cliente_novo.cep
    cliente_anterior.tel_resid = cliente_novo.tel_resid
    cliente_anterior.tel_cel = cliente_novo.tel_cel
    cliente_anterior.email = cliente_novo.email
    cliente_anterior.rg = cliente_novo.rg
    cliente_anterior.cpf = cliente_novo.cpf
    cliente_anterior.nascimento = cliente_novo.nascimento
    cliente_anterior.is_premium = cliente_novo.is_premium
    db.session.commit()


def remover_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()
