class Banca:
    clienti = []
    conti_correnti = []

    def __init__(self, nome_banca):
        self.nome_banca = nome_banca
        self.clienti = []
        self.conti_correnti = []

    def __repr__(self):
        return print(f"""Nome banca = {self.nome_banca}\nnumero totale di clienti = {len(self.clienti)}\n
        numero totale di conti correnti: {len(self.conti_correnti)}""")
