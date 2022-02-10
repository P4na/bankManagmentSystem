from datetime import datetime


class Conto:
    operazioni_effettuate = []
    tassa_prelievo = 1.00

    def __init__(self, cliente, numero_conto, bilancio_conto=0, saldo=0):
        self.__cliente = cliente
        self.__bilancio_conto = bilancio_conto
        self.__numero_conto = numero_conto
        self.__saldo = saldo

    def __repr__(self):
        return "Conto " + self.__numero_conto + " intestato a cliente " + self.__cliente.nome_cliente  + " con saldo " + str(self.__saldo) + "€"

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def bilancio_conto(self):
        return self.__bilancio_conto
    @bilancio_conto.setter
    def bilancio_conto(self, bilancio_conto):
        self.__bilancio_conto = bilancio_conto
    
    @property
    def numero_conto(self):
        return self.__numero_conto
    @numero_conto.setter
    def numero_conto(self, numero_conto):
        self.__numero_conto = numero_conto

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        
    def preleva_soldi(self, value):
        if self.tipo == True:
            if self.__saldo < (value + self.tassa_prelievo):
                self.__saldo -= value
                if self.saldo < 0 and self.saldo == False:
                    self.data_inizio_debito = datetime.datetime.now()
        else:
            if self.__saldo < (value + self.tassa_prelievo):
                print("importo richiesto non presente sul conto")
            else:
                self.__saldo -= value
                print("Saldo prelevato, buona giornata!")
                
    def versa_soldi(self, value):
        if self.__saldo < 0:
            self.__saldo += value
            if self.__saldo >= 0:
                self.data_inizio_debito = None
                print("Debito saldato, non sei più poraccio")     
        self.__saldo += value
        
        

class ContoSpecial(Conto):
    tipo = "Contospecial"
    
    @super
    def __init__(self, cliente, numero_conto, bilancio_conto=0, saldo=0, data_inizio_debito = None, tassa_prelievo = 2.00):
        super().__init__(cliente, numero_conto, bilancio_conto, saldo)