class Cliente:
    nome_cliente = ""

    def __init__(self, nome_cliente, numero_telefono):
        self.nome_cliente = nome_cliente
        self.numero_telefono = numero_telefono

    def __repr__(self):
        return print(f"""Cliente = {self.nome_cliente}\nnumero di telefono = {self.numero_telefono}""")
