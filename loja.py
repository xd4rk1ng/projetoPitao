#!/usr/bin/env python3
######### PROJETO PITON #########
### Aqui teremos o script principal para a execucao do nosso programa ###
import os # Para o system(cls)
import User # Nossa classe
import json
import Functions



## ENTRY POINT ##
file_name = "dataBase.json"
Users = Functions.get_Users(file_name)

## uncomment to test Users loaded in memory
# for usr in Users:
#     print (usr.name)

while True: # The ATM cannot be turned off by users, so this cycle can stay running
    Functions.clear_console()
    opt = None
    user = Functions.login(Users)

    while opt != 6:
        Functions.show_menu(user) # Exhibits the menu for an specific user, with their information

        try: # Try is needed to ensure the user inserts an INTERGER
            opt = int(input("Opção desejada: ")) 
            match(opt):
                case 1: # Prints the users balance
                    print(f"Saldo disponivel: € {user.balance}")
                    input()            
                case 2: # Takes out cash
                    user.LevantarSaldo(Users)
                case 3:
                    pass
                    break
                case 4:
                    user.TransferirPara(Users)
                case 5:
                    pass
                    break
                case 6:
                    break
                case _:
                    print("!Insira uma opção valida!")
                    input()
        except ValueError: # ValueEror means the user inserted a non interger value, rather than an incorrect number
            print("Erro: Insira um numero inteiro")
            input()