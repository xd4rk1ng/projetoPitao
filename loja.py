#!/usr/bin/env python3
######### PROJETO PITON #########
### Aqui teremos o script principal para a execucao do nosso programa ###
import os # Para o system(cls)
class User:
    def __init__ (self, IBAN, id_credit_card,  name, saldo):
        self.IBAN = IBAN
        self.id_credit_card = id_credit_card
        self.name = name
        self.balance = balance

def get_Users(file):
    import json
    error_Message = "Error opening file"
    try:
        with open(file, "r") as f:
            data = json.load(f)
            Users = []
            for usr_data in data:
                Users.append(User(**usr_data))
            return Users
        
    except Exception as e:
        print(f"{error_Message}: {e}")
        return []

menu = { 
    1: "Consultar saldo",
    2: "Realizar Levantamento",
    3: "Realizar Depósito",
    4: "Realizar Transferência",
    5: "Consultar Movimentos",
    6: "Sair"
}

def clear_console():
    # Windows uses 'cls', Linux/macOS use 'clear'
    if os.name == "posix":
        command = "clear"
    else:
        command = "cls" 
    os.system(command)

def ExibirMenu():
    for key, value in menu.items():
        print(f"{key}: {value}")

## ENTRY POINT ##
file_name = "dataBase.json"
Users = get_Users(file_name)

## uncomment to test Users loaded in memory
# for usr in Users:
#     print (usr.name)

opt = None
error_message = ""

while opt != 6:
    clear_console() 
    ExibirMenu()
    
    # All this does is point out to the user theyve inserted invalid option
    try:
        opt = int(input(f"Insira a opção desejada: {error_message}"))
        error_message = "" # cleans error message
    except Exception:
        error_message = "!!Opcao invalida!!" # sets message


