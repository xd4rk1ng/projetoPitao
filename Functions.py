import os
import json
import User

class Error:
    def __init__(self, message, exception):
        self.message = message
        self.exception = exception

    def __str__(self):
        return f"{self.message}"

def get_Users(file):
    error_Message = "Error loading file"
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
    
def save_users(Users, file):
    error_Message = "Error Saving File"
    # Save to JSON
    try:
        data_dict = [vars(u) for u in Users]
        with open(file, "w") as f:
            json.dump(data_dict, f, indent=4, default=str)
    except Exception as e:
        print(f"{error_Message: {e}}")
        return
    
    
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
                    return user 
        if not user_found:
            print("Cartão não encontrado.")


def clear_console(): # Function to clear the terminal
    # Windows uses 'cls', Linux/macOS use 'clear'
    if os.name == "posix":
        command = "clear"
    else:
        command = "cls" 
    os.system(command)

def show_menu(user):
    clear_console()

    menu = {
    '1 ': "Consultar saldo",
    '2 ': "Realizar Levantamento",
    '3 ': "Realizar Depósito",
    '4 ': "Realizar Transferência",
    '5 ': "Consultar Movimentos",
    ':q': "Sair"
    }
    
    print(f"Bem vindo {user.name}!")
    for key, value in menu.items():
        print(f"{key}: {value}")
        
def search_user(Users, user_iban):
    error_message = "Ocorreu um erro na operacao."
    for usr in Users:
        if usr.IBAN != user_iban:
            continue
        return usr
    return Functions.Error(error_message, None)

def get_cast_input(cast_type, message):
    error_message = ""
    input_str = input(message)
    if input_str == ":q":
        return None
    
    try:
        return cast_type(input_str)
    except ValueError as e:
        return Functions.Error("Valor inválido fornecido.", e)
    except TypeError as e:
        return Functions.Error("Tipo incorreto de valor.", e)
    except Exception as e:
        return Functions.Error("Erro inesperado na operação.", e)