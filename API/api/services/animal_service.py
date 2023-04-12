from api import db
from ..models import animal_model


def cadastrar_animal(animal):
    animal_bd = animal_model.Animal(nome=animal.nome, raca=animal.raca, cor=animal.cor, idade=animal.idade,
                                    alergico=animal.alergico, hora_comer=animal.hora_comer, racao=animal.racao,
                                    registro=animal.registro, cliente_id=animal.cliente_id)
    db.session.add(animal_bd)
    db.session.commit()


def listar_animal():
    animais = animal_model.Animal.query.all()
    return animais


def listar_animal_id(id):
    animal = animal_model.Animal.query.filter_by(id=id).first()
    return animal


def atualizar_animal(animal_anterior, animal_novo):
    animal_anterior.nome = animal_novo.nome
    animal_anterior.raca = animal_novo.raca
    animal_anterior.cor = animal_novo.cor
    animal_anterior.idade = animal_novo.idade
    animal_anterior.alergico = animal_novo.alergico
    animal_anterior.hora_comer = animal_novo.hora_comer
    animal_anterior.racao = animal_novo.racao
    animal_anterior.registro = animal_novo.registro
    animal_anterior.cliente_id = animal_novo.cliente_id
    db.session.commit()


def remove_animal(animal):
    db.session.delete(animal)
    db.session.commit()
