class Venda:
    def __init__(self, cliente_id, valor_total, valor_custo, valor_lucro, met_pagamento, data_hora):
        self.__cliente_id = cliente_id
        self.__valor_total = valor_total
        self.__valor_custo = valor_custo
        self.__valor_lucro = valor_lucro
        self.__met_pagamento = met_pagamento
        self.__data_hora = data_hora

    @property
    def cliente_id(self):
        return self.__cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

    @property
    def valor_custo(self):
        return self.__valor_custo

    @valor_custo.setter
    def valor_custo(self, valor_custo):
        self.__valor_custo = valor_custo

    @property
    def valor_lucro(self):
        return self.__valor_lucro

    @valor_lucro.setter
    def valor_lucro(self, valor_lucro):
        self.__valor_lucro = valor_lucro

    @property
    def met_pagamento(self):
        return self.__met_pagamento

    @met_pagamento.setter
    def met_pagamento(self, met_pagamento):
        self.__met_pagamento = met_pagamento

    @property
    def data_hora(self):
        return self.__data_hora

    @data_hora.setter
    def data_hora(self, data_hora):
        self.__data_hora = data_hora
