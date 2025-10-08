from decimal import Decimal
import json

class User:
    def __init__ (self, IBAN, credit_card, pin, name, balance):
        self.IBAN = IBAN
        self.credit_card = credit_card
        self.pin = pin
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}(€{self.balance})"
    
    from decimal import Decimal

    def LevantarSaldo(self, Users, file="dataBase.json"):
        try:
            cash = Decimal(input("Insira a quantidade que deseja levantar (QUANTIDADES MAIORES QUE 10): "))
        except:
            print("Por favor, insira um número válido.")
            return

        # Ensure balance is Decimal
        self.balance = Decimal(str(self.balance))

        if cash < 10:
            print("O montante tem de ser maior que 10.")
            return
        if cash > self.balance:
            print("O montante não pode ser superior ao que tens em conta.")
            return

        self.balance -= cash
        print("Ejetando o montante requisitado...")

        # Update the in-memory list
        for usr in Users:
            if usr.credit_card == self.credit_card:
                usr.balance = self.balance
                break

        # Save to JSON
        data = [vars(u) for u in Users]
        with open(file, "w") as f:
            json.dump(data, f, indent=4, default=str)

        print("Saldo atualizado com sucesso.")
        input()

