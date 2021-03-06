class Cliente:
    __nome_cliente = ""

    def __init__(self, nome_cliente, numero_telefono):
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono

    def __repr__(self):
        return f"Cliente = {self.__nome_cliente}\nnumero di telefono = {self.__numero_telefono}"

#    @property
#    def nome_cliente(self):
#        return self.__nome_cliente
    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    @property
    def numero_telefono(self):
        return self.__numero_telefono
    @numero_telefono.setter
    def numero_telefono(self, numero_telefono):
        self.__numero_telefono = numero_telefono


