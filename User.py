from decimal import Decimal
from datetime import datetime #para o historico

import Functions

class User:
    def __init__ (self, IBAN, credit_card, pin, name, balance, history):
        self.IBAN = IBAN
        self.credit_card = credit_card
        self.pin = pin
        self.name = name
        self.balance = Decimal(balance)
        self.history = history

    def __str__(self):
        return f"{self.name}(€{self.balance})"
    
    from decimal import Decimal

    def MostrarSaldo(self):
        print(f"Saldo disponivel: € {self.balance}")
        input()   
        
    def LevantarSaldo(self, Users, file="dataBase.json"):
                
        while True:
            Functions.clear_console()
            print(f"Qual o montante que deseja levantar?(Saldo Disponivel: {self.balance})")
            ammount = Functions.get_cast_input(Decimal, "(Insira valor superior a 10): ")
            match ammount:
                case None:
                    print("Operação cancelada.")
                    input()
                    return
                case Functions.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    continue


            if not(10 <= ammount <= Decimal(self.balance)):
                print("!!! Erro: Montante invalido! Verifique se o valor e superior ou igual a 10 e dentro do seu saldo disponivel.")
                print("(Pressione Enter para tentar de novo)")
                input()
                continue

            print("Ejetando o montante requisitado...")
            self.balance -= ammount
            self.history.append(f"LV [{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: Levantamento no valor de {ammount}")

            Functions.save_users(Users, file)
            print("Saldo atualizado com sucesso.")
            input()
            return
    
    def Depositar(self, Users, file="dataBase.json"):
        while True:
            Functions.clear_console()
            print("Insira por favor o dinheiro no local indicado...")
            ammount = Functions.get_cast_input(Decimal, "> Montante : ")
            match ammount:
                case None:
                    print("Operação cancelada")
                    input()
                    return
                case Functions.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    continue
            
            print("Processando...")
            if ammount <= 0:
                print("!!! Erro: Montante invalido! Verifique se o valor que introduziu é positivo.")
                print("(Pressione uma tecla para tentar de novo)")
                input()
                continue
            
            self.balance += ammount
            self.history.append(f"DP [{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: Deposito no valor de {ammount}")
            
            Functions.save_users(Users, file)
            print("Saldo atualizado com sucesso.")
            input()
            return                        
    
    def TransferirPara(self, Users, file="dataBase.json"):
        while True:
            Functions.clear_console()
            print("Para quem deseja transferir dinheiro? (:q para sair)")
            iban = Functions.get_cast_input(str, "Por favor insira IBAN de destino: ")
            match iban:
                case None:
                    print("Operação cancelada.")
                    input()
                    return
                case Functions.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    continue
                
            recipient = Functions.search_user(Users, iban)
            if isinstance(recipient, Functions.Error):
                print("!!! Erro: Foi impossivel encontrar utilizador na base de dados.")
                print("(Pressione Enter para tentar de novo)")
                input()
                continue
            elif recipient == self:
                print("!!! Erro: O IBAN que introduziu e o seu!")
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
                case Functions.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    continue
            
            if not(0 < ammount <= Decimal(self.balance)):
                print("!!! Erro: Montante invalido! Verifique se o valor e positivo e dentro do seu saldo disponivel.")
                print("(Pressione Enter para tentar de novo)")
                input()
                continue
                
            print("Transferindo para destinatario...")
            recipient.balance += ammount
            self.balance -= ammount
            self.history.append(f"TF [{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}]: Transferencia no valor de {ammount} para {recipient.name}:{iban}")
            
            Functions.save_users(Users, file)
            print("Saldo atualizado com sucesso.")
            input()
            return
               
    def ConsultarMovimentos(self, Users):
        counter = 0
        for movement in reversed(self.history):        
            print(movement)
            if counter == 10:
                input()
                return
            counter += 1
        input()
        return