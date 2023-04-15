class Produto:
    def __init__(self, codigo, descricao, unidade_medida, medida, quantidade_estoque, valor_custo, valor_venda, cor,
                 tipo, fabricante, quantidade_min_estoque):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__unidade_medida = unidade_medida
        self.__medida = medida
        self.__quantidade_estoque = quantidade_estoque
        self.__valor_custo = valor_custo
        self.__valor_venda = valor_venda
        self.__cor = cor
        self.__tipo = tipo
        self.__fabricante = fabricante
        self.__quantidade_min_estoque = quantidade_min_estoque
        # self.__fornecedor_id = fornecedor_id
        # Sugerir data de validade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def unidade_medida(self):
        return self.__unidade_medida

    @unidade_medida.setter
    def unidade_medida(self, unidade_medida):
        self.__unidade_medida = unidade_medida

    @property
    def medida(self):
        return self.__medida

    @medida.setter
    def medida(self, medida):
        self.__medida = medida

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

    @property
    def valor_custo(self):
        return self.__valor_custo

    @valor_custo.setter
    def valor_custo(self, valor_custo):
        self.__valor_custo = valor_custo

    @property
    def valor_venda(self):
        return self.__valor_venda

    @valor_venda.setter
    def valor_venda(self, valor_venda):
        self.__valor_venda = valor_venda

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    @property
    def quantidade_min_estoque(self):
        return self.__quantidade_min_estoque

    @quantidade_min_estoque.setter
    def quantidade_min_estoque(self, quantidade_min_estoque):
        self.__quantidade_min_estoque = quantidade_min_estoque
"""
    @property
    def fornecedor_id(self):
        return self.__fornecedor_id

    @fornecedor_id.setter
    def fornecedor_id(self, fornecedor_id):
        self.__fornecedor_id = fornecedor_id
"""