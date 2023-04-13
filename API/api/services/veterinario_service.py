from api import db
from ..models import veterinario_model


def cadastrar_veterinario(vet):
    vet_bd = veterinario_model.Veterinario(nome=vet.nome, crmv=vet.crmv, endereco=vet.endereco, cidade=vet.cidade,
                                           uf=vet.uf, cep=vet.cep, tel_emergencia=vet.tel_emergencia, email=vet.email,
                                           hora_atendimento=vet.hora_atendimento, efetivo=vet.efetivo,
                                           valor_pagar=vet.valor_pagar)
    db.session.add(vet_bd)
    db.session.commit()


def listar_veterinarios():
    vets = veterinario_model.Veterinario.query.all()
    return vets


def listar_veterinario_id(id):
    vet = veterinario_model.Veterinario.query.filter_by(id=id).first()
    return vet


def atualizar_veterinario(vet_anterior, vet_novo):
    vet_anterior.nome = vet_novo.nome
    vet_anterior.crmv = vet_novo.crmv
    vet_anterior.endereco = vet_novo.endereco
    vet_anterior.cidade = vet_novo.cidade
    vet_anterior.uf = vet_novo.uf
    vet_anterior.cep = vet_novo.cep
    vet_anterior.tel_emergencia = vet_novo.tel_emergencia
    vet_anterior.email = vet_novo.email
    vet_anterior.hora_atendimento = vet_novo.hora_atendimento
    vet_anterior.efetivo = vet_novo.efetivo
    vet_anterior.valor_pagar = vet_novo.valor_pagar
    db.session.commit()


def remove_veterinario(vet):
    db.session.delete(vet)
    db.session.commit()