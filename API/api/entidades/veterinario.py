class Veterinario:
    def __init__(self, nome, crmv, endereco, cidade, uf, cep, tel_emergencia, email, hora_atendimento, efetivo,
                 valor_pagar):
        self.__nome = nome
        self.__crmv = crmv
        self.__endereco = endereco
        self.__cidade = cidade
        self.__uf = uf
        self.__cep = cep
        self.__tel_emergencia = tel_emergencia
        self.__email = email
        self.__hora_atendimento = hora_atendimento
        self.__efetivo = efetivo
        self.__valor_pagar = valor_pagar

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def crmv(self):
        return self.__crmv

    @crmv.setter
    def crmv(self, crmv):
        self.__crmv = crmv

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
    def tel_emergencia(self):
        return self.__tel_emergencia

    @tel_emergencia.setter
    def tel_emergencia(self, tel_emergencia):
        self.__tel_emergencia = tel_emergencia

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def  hora_atendimento(self):
        return self.__hora_atendimento

    @hora_atendimento.setter
    def hora_atendimento(self, hora_atendimento):
        self.__hora_atendimento = hora_atendimento

    @property
    def efetivo(self):
        return self.__efetivo

    @efetivo.setter
    def efetivo(self, efetivo):
        self.__efetivo = efetivo

    @property
    def valor_pagar(self):
        return self.__valor_pagar

    @valor_pagar.setter
    def valor_pagar(self, valor_pagar):
        self.__valor_pagar = valor_pagar