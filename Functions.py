import os
import json
import User

def get_Users(file):
    error_Message = "Error opening file"
    try:
        with open(file, "r") as f: # Salva nosso JSON como F
            data = json.load(f) # Guarda numa variavel
            Users = [] # Lista de users
            for usr_data in data:
                Users.append(User.User(**usr_data)) # Adiciona cada user na lista
            return Users
        
    except Exception as e:
        print(f"{error_Message}: {e}")
        return []
    
def login(Users):
    logged = False
    while not logged:
        card = input("Nº do cartão: ")

        user_found = False  # Ve se o cartão foi encontrado
        for user in Users:            
            if card == user.credit_card:
                user_found = True
                pin = ""  # Inicia o PIN
                while pin != user.pin:
                    pin = input("Insira o PIN: ")
                    if pin == user.pin:
                        logged = True
                        break  # Exit the PIN loop
                    else:
                        print("Pin incorreto.")
                if logged:
                    clear_console()
                    ExibirMenu(user)  
        if not user_found:
            print("Cartão não encontrado.")


def clear_console(): # Fnção de limpeza de tela
    # Windows uses 'cls', Linux/macOS use 'clear'
    if os.name == "posix":
        command = "clear"
    else:
        command = "cls" 
    os.system(command)

def ExibirMenu(user):
    menu = { 
    1: "Consultar saldo",
    2: "Realizar Levantamento",
    3: "Realizar Depósito",
    4: "Realizar Transferência",
    5: "Consultar Movimentos",
    6: "Sair"
    }
    
    print(f"Bem vindo {user.name}!")
    for key, value in menu.items():
        print(f"{key}: {value}")