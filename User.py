class User:
    def __init__ (self, IBAN, credit_card, pin, name, balance):
        self.IBAN = IBAN
        self.credit_card = credit_card
        self.pin = pin
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}(€{self.balance})"