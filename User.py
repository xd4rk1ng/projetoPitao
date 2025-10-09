from decimal import Decimal
import json

import Functions
import Errors

class User:
    def __init__ (self, IBAN, credit_card, pin, name, balance):
        self.IBAN = IBAN
        self.credit_card = credit_card
        self.pin = pin
        self.name = name
        self.balance = Decimal(balance)

    def __str__(self):
        return f"{self.name}(€{self.balance})"
    
    from decimal import Decimal

    def LevantarSaldo(self, Users, file="dataBase.json"):
        
        #TODO func (input_string)
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


        # Save to JSON
        data_dict = [vars(u) for u in Users]
        with open(file, "w") as f:
            json.dump(data_dict, f, indent=4, default=str)

        print("Saldo atualizado com sucesso.")
        input()
    
    def TransferirPara(self, Users):
        while True:
            Functions.clear_console()
            print("Para quem deseja transferir dinheiro? (:q para sair)")
            iban = Functions.get_cast_input(str, "Por favor insira IBAN de destino: ")
            match iban:
                case None:
                    print("Operação cancelada.")
                    input()
                    return
                case Errors.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    continue
                
            recipient = Functions.search_user(Users, iban)
            if isinstance(recipient, Errors.Error):
                print("!!! Erro: Foi impossivel encontrar utilizador na base de dados.")
                print("(Pressione Enter para tentar de novo)")
                input()
                continue
            
            Functions.clear_console()
            print(f"Transferencia para IBAN: {iban}")
            print(f"Saldo -> {self.balance}")
            ammount = Functions.get_cast_input(Decimal,"Insira montante a enviar: ")
            match ammount:
                case None:
                    print("Operacao cancelada.")
                    input()
                    return
                case Errors.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    continue
            
            if not(0 < ammount <= Decimal(self.balance)):
                print("!!! Erro: Montante invalido! Verifique se o valor e positivo e dentro do seu saldo disponivel.")
                print("(Pressione Enter para tentar de novo)")
                input()
                continue
                
            recipient.balance += ammount
            self.balance -= ammount
            
            #TODO save data in json
            print("Operacao bem sucedida!")
            input()
            return
                
            
                
                
                
            
                

