class Utilizador:
    def __init__(self, nome, cartao, pin, saldo):
        self.nome = nome
        self.cartao = cartao
        self.pin = pin
        self.saldo = saldo

    def __str__(self):
        return f"{self.nome}(€{self.saldo})"