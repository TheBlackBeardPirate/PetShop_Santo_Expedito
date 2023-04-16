from api import db
from passlib.hash import pbkdf2_sha256


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    tel_resid = db.Column(db.String(10), nullable=False)
    tel_cel = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(8), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    api_key = db.Column(db.String(100), nullable=True)

    def encrip_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def decrip_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)
