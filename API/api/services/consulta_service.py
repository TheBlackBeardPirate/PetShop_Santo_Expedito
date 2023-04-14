from api import db
from ..models import consulta_model


def cadastrar_consulta(consulta):
    consulta_bd = consulta_model.Consulta(horario=consulta.horario, nome_cliente=consulta.nome_cliente,
                                          cpf_cliente=consulta.cpf_cliente, valor=consulta.valor,
                                          cliente_premium=consulta.cliente_premium,
                                          nome_animal=consulta.nome_animal, raca=consulta.raca,
                                          emergencia=consulta.emergencia, nome_vet=consulta.nome_vet,
                                          vet_efetivo=consulta.vet_efetivo, crmv=consulta.crmv)
    db.session.add(consulta_bd)
    db.session.commit()


def listar_consultas():
    consulta_bd = db.session.query(consulta_model.Consulta).order_by(consulta_model.Consulta.horario)
    # consulta_bd = consulta_model.Consulta.query.all()
    return consulta_bd


def listar_consulta_id(id):
    consulta_bd = consulta_model.Consulta.query.filter_by(id=id).first()
    return consulta_bd


def editar_consulta(consulta_anterior, consulta_nova):
    consulta_anterior.horario = consulta_nova.horario
    consulta_anterior.nome_cliente = consulta_nova.nome_cliente
    consulta_anterior.cpf_cliente = consulta_nova.cpf_cliente
    consulta_anterior.valor = consulta_nova.valor
    consulta_anterior.cliente_premium = consulta_nova.cliente_premium
    consulta_anterior.nome_animal = consulta_nova.nome_animal
    consulta_anterior.raca = consulta_nova.raca
    consulta_anterior.emergencia = consulta_nova.emergencia
    consulta_anterior.nome_vet = consulta_nova.nome_vet
    consulta_anterior.vet_efetivo = consulta_nova.vet_efetivo
    consulta_anterior.crmv = consulta_nova.crmv
    db.session.commit()


def remover_consulta(consulta):
    db.session.delete(consulta)
    db.session.commit()
