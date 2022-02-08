from conto import Conto
from cliente import Cliente
from soluzione_it1.utility import Utility

class Banca:
    lista_clienti = []
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
        
    def apri_conto_corrente(self, conto):
        self.conti_correnti.append(conto)
                                   
    def aggiungi_clienti(self, cliente):
        self.lista_clienti.append(cliente) 
        
    def rimuovi_clienti(self, id):
        assert Utility.is_integer(id), "inserire un id intero"
        assert int(id) > 0, "inserire un id valido"
        
        pos=-1
        for index in range (0,len(self.clienti)):
            if self.clienti[index].id == int(id):
                pos = index
                break
            
        if pos<0:
            print("ERROR: numero conto non trovato")
        else:
            pass
    
    def chiudi_conto(self, numero_conto):
        pass
 

