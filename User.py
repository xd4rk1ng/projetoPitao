from decimal import Decimal

import Functions

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
        while True:
            Functions.clear_console()
            print("Qual o montante que deseja levantar?")
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

            Functions.save_users(Users, file)
            print("Saldo atualizado com sucesso.")
            input()
            return
    def MostrarSaldo(self):
        print(f"Saldo disponivel: € {self.balance}")
        input()   
    
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
            
            
            Functions.save_users(Users, file)
            print("Saldo atualizado com sucesso.")
            input()
            return
                
            
                
                
                
            
                

