#!/usr/bin/env python3
######### PROJETO PITON #########
### Aqui teremos o script principal para a execucao do nosso programa ###
import os # Para o system(cls)
import User # Nossa classe
import json
import Functions
import Errors



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

    while True:
        Functions.show_menu(user) # Exhibits the menu for an specific user, with their information

        try: # Try is needed to ensure the user inserts an INTEGER
            opt = Functions.get_cast_input(str,"Opção desejada: ")
            match opt:
                case None:
                    print("Operação cancelada.")
                    input()
                    break
                case Errors.Error(message=msg):
                    print(f"!!! Erro: {msg}")
                    print("(Pressione Enter para tentar de novo)")
                    input()
                    
                case "1": # Print user balance
                    user.MostrarSaldo()         
                case "2": # Take out cash
                    user.LevantarSaldo(Users)
                case "3": # Deposit cash
                    user.Depositar(Users)
                case "4": # Transfer to user
                    user.TransferirPara(Users)
                case "5": # Display transfer history
                    user.MostrarHistorico(Users)
                case _:
                    print("!Insira uma opção valida!")
                    input()
        except ValueError: # ValueEror means the user inserted a non interger value, rather than an incorrect number
            print("Erro: Insira um numero inteiro")
            input()