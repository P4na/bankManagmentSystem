from soluzione_it1.cliente import Cliente
from soluzione_it1.bank import Banca
from soluzione_it1.conto import Conto

cliente1 = Cliente('Davide', '3924663077')
cliente2 = Cliente('Simona', '3335688985')
cliente3 = Cliente('Marco', '3335688285')
banca_san_paolo = Banca('Banca San Paolo')
account = Conto('00001', cliente1)


cliente1.__repr__()
banca_san_paolo.__repr__()
account.__repr__()
