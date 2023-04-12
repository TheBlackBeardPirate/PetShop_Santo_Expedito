class Animal:
    def __init__(self, nome, raca, cor, idade, alergico, hora_comer, racao, registro, cliente_id):
        self.__nome = nome
        self.__raca = raca
        self.__cor = cor
        self.__idade = idade
        self.__alergico = alergico
        self.__hora_comer = hora_comer
        self.__racao = racao
        self.__registro = registro
        self.__cliente_id = cliente_id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def alergico(self):
        return self.__alergico

    @alergico.setter
    def alergico(self, alergico):
        self.__alergico = alergico

    @property
    def hora_comer(self):
        return self.__hora_comer

    @hora_comer.setter
    def hora_comer(self, hora_comer):
        self.__hora_comer = hora_comer

    @property
    def racao(self):
        return self.__racao

    @racao.setter
    def racao(self, racao):
        self.__racao = racao

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro):
        self.__registro = registro

    @property
    def cliente_id(self):
        return self.__cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id
