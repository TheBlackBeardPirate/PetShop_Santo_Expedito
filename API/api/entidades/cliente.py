class Cliente:
    def __init__(self, nome, endereco, cidade, uf, cep, tel_resid, tel_cel, email, rg, cpf, nascimento, is_premium):
        self.__nome = nome
        self.__endereco = endereco
        self.__cidade = cidade
        self.__uf = uf
        self.__cep = cep
        self.__tel_resid = tel_resid
        self.__tel_cel = tel_cel
        self.__email = email
        self.__rg = rg
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__is_premium = is_premium

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def tel_resid(self):
        return self.__tel_resid

    @tel_resid.setter
    def tel_resid(self, tel_resid):
        self.__tel_resid = tel_resid

    @property
    def tel_cel(self):
        return self.__tel_cel

    @tel_cel.setter
    def tel_cel(self, tel_cel):
        self.__tel_cel = tel_cel

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def is_premium(self):
        return self.__is_premium

    @is_premium.setter
    def is_premium(self, is_premium):
        self.__is_premium = is_premium