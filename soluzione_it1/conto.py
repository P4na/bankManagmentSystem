
class Conto:
    operazioni_effettuate = []

    def __init__(self, Cliente, numero_conto, bilancio_conto=0, saldo=0):
        self.cliente = Cliente
        self.bilancio_conto = bilancio_conto
        self.numero_conto = numero_conto
        self.saldo = saldo

    def __repr__(self):
        return "Conto " + self.numero_conto + " intestato a cliente " + self.cliente.nome_cliente  + " con saldo " + str(self.saldo) + "€"