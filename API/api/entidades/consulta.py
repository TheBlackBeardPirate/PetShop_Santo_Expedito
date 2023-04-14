class Consulta:
    def __init__(self, horario, nome_cliente, cpf_cliente, cliente_premium, nome_animal, raca, emergencia, nome_vet, vet_efetivo,
                 crmv, valor):
        self.__horario = horario
        self.__nome_cliente = nome_cliente
        self.__cpf_cliente = cpf_cliente
        self.__cliente_premium = cliente_premium
        self.__nome_animal = nome_animal
        self.__raca = raca
        self.__emergencia = emergencia
        self.__nome_vet = nome_vet
        self.__vet_efetivo = vet_efetivo
        self.__crmv = crmv
        self.__valor = valor

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
            self.__nome_cliente = nome_cliente

    @property
    def cpf_cliente(self):
        return self.__cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, cpf_cliente):
        self.__cpf_cliente = cpf_cliente

    @property
    def cliente_premium(self):
        return self.__cliente_premium

    @cliente_premium.setter
    def cliente_premium(self, cliente_premium):
        self.__cliente_premium = cliente_premium

    @property
    def nome_animal(self):
        return self.__nome_animal

    @nome_animal.setter
    def nome_animal(self, nome_animal):
        self.__nome_animal = nome_animal

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def emergencia(self):
        return self.__emergencia

    @emergencia.setter
    def emergencia(self, emergencia):
        self.__emergencia = emergencia

    @property
    def nome_vet(self):
        return self.__nome_vet

    @nome_vet.setter
    def nome_vet(self, nome_vet):
        self.__nome_vet = nome_vet

    @property
    def vet_efetivo(self):
        return self.__vet_efetivo

    @vet_efetivo.setter
    def vet_efetivo(self, vet_efetivo):
        self.__vet_efetivo = vet_efetivo

    @property
    def crmv(self):
        return self.__crmv

    @crmv.setter
    def crmv(self, crmv):
        self.__crmv = crmv

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
