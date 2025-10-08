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

opt = None

while opt != 6:
    Functions.clear_console()
    Functions.login(Users)

    try: # Try é necessario para garantir que o usuario insere um INT, pois não vai conseguir fazer parse a certos inputs
        opt = int(input("Opção desejada: "))
        match(opt):
            case 1:
                for u in Users:
                    print(u)
                break
            case 2:
                pass
                break
            case 3:
                pass
                break
            case 4:
                pass
                break
            case 5:
                pass
                break
            case 6:
                pass
            case _:
                print("!Insira uma opção valida!")
                input()
    except ValueError:
        print("Erro: Insira um numero inteiro")
        input()



