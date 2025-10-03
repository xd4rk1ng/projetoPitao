######### PROJETO PITON #########
### Aqui teremos o script principal para a execucao do nosso programa ###
import json
import os # Para o system(cls)

menu = { # Um dict com as nossas opções do menu
    1: "Consultar saldo",
    2: "Realizar Levantamento",
    3: "Realizar Depósito",
    4: "Realizar Transferência",
    5: "Consultar Movimentos",
    6: "Sair"
}

def ExibirMenu():
    for key, value in menu.items():
        print(f"{key}: {value}")


opt = None
while opt != 6:
    os.system('cls')
    ExibirMenu()
    opt = int(input("Insira a opção desejada: "))