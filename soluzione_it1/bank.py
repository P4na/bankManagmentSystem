class Banca:
    clienti = []
    conti_correnti = []

    def __init__(self, nome_banca):
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []

    def __repr__(self):
        return f"Nome banca = {self.__nome_banca}\nnumero totale di clienti = {len(self.__clienti)}\nnumero totale di conti correnti: {len(self.__conti_correnti)}"
    
    @property
    def nome_banca(self):
        return self.__nome_cliente
    @nome_banca.setter
    def nome_banca(self, nome_banca):
        self.__nome_cliente = nome_banca

    @property
    def clienti(self):
        return self.__clienti
    @clienti.setter
    def clienti(self, clienti):
        self.__clienti = clienti



