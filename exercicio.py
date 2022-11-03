import os
import time

# Faça com que cada opção solicite o nome e senha da conta para realizar as operações em uma 
# conta especifica

contas = []

controle = True
while controle:
        
    print ("MENU PRINCIPAL \n")
    print ("1 - Saldo")
    print ("2 - Deposito")
    print ("3 - Saque")
    print ("4 - Cadastrar novo usuario")
    print ("5 - Para sair")


    opcao_menu = input("Digite a opcao desejada: ")

    if opcao_menu == "1":
        if contas:
            print ("Saldo atual: " + str(conta["Saldo"]))

    elif opcao_menu == "2":
        deposito = float(input("Digite o valor do deposito: "))
        conta["Saldo"]=saldo+deposito
        print ("Deposito efetuado com sucesso!")
        print ("Saldo atual: " + str(conta["Saldo"]))

    elif opcao_menu == "3":
        saque = float(input("Digite o valor a sacar: "))
        if saque > saldo:
            print ("Saldo insuficiente!")
        else:
            conta["Saldo"]=conta["Saldo"]-saque
            print ("Saque efetuado com sucesso!")
            print ("Saldo atual: " + str(conta["Saldo"]))

    elif opcao_menu == "4":
        usuario = input("Digite o nome do usuario: ")
        deposito = float(input("Digite o valor do deposito inicial: "))
        saldo = deposito
        conta = {"Usuario": usuario, "Saldo": saldo}
        contas.append(conta)
        print ("Conta cadastrada com sucesso!")
        print (contas)
    
    elif opcao_menu == '5':
        controle = False
        print("*************************\n Adeus ao Banco Comuna \n *****************")

    else:
        print ("Opcao invalida!")