from api import db
from ..models import usuario_model


def cadastrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, endereco=usuario.endereco, cidade=usuario.cidade, uf=usuario.uf,
                                       cep=usuario.cep, tel_resid=usuario.tel_resid, tel_cel=usuario.tel_cel,
                                       email=usuario.email, rg=usuario.rg, cpf=usuario.cpf, nascimento=usuario.nascimento,
                                       senha=usuario.senha, is_admin=usuario.is_admin, api_key=usuario.api_key)
    usuario_bd.encrip_senha()
    db.session.add(usuario_bd)
    db.session.commit()


def listar_usuario_email(email):
    usuario_bd = usuario_model.Usuario.query.filter_by(email=email).first()
    return usuario_bd


def listar_usuario_id(id):
    usuario_bd = usuario_model.Usuario.query.filter_by(id=id).first()
    return usuario_bd


def atualizar_usuario(usuario_antigo, usuario_novo):
    usuario_antigo.nome = usuario_novo.nome
    usuario_antigo.endereco = usuario_novo.endereco
    usuario_antigo.cidade = usuario_novo.cidade
    usuario_antigo.uf = usuario_novo.uf
    usuario_antigo.cep = usuario_novo.cep
    usuario_antigo.tel_resid = usuario_novo.tel_resid
    usuario_antigo.tel_cel = usuario_novo.tel_cel
    usuario_antigo.email = usuario_novo.email
    usuario_antigo.rg = usuario_novo.rg
    usuario_antigo.cpf = usuario_novo.cpf
    usuario_antigo.nascimento = usuario_novo.nascimento
    usuario_antigo.senha = usuario_novo.senha
    usuario_antigo.is_admin = usuario_novo.is_admin
    usuario_antigo.api_key = usuario_novo.api_key
    db.session.commit()


def remover_usuario(usuario):
    db.session.delete(usuario)
    db.session.delete()


def listar_usuario_api_key(api_key):
    usuario_bd = usuario_model.Usuario.query.filter_by(api_key=api_key).first()
    return usuario_bd
