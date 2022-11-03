
def menu():
    print ("MENU PRINCIPAL \n")
    print ("1 - Saldo")
    print ("2 - Deposito")
    print ("3 - Saque")
    print ("4 - Cadastrar novo usuario")
    print ("5 - Para sair")

def entrada(texto):
    return input(texto)

def depositar(dicionario):
    deposito = float(entrada("Digite o valor de deposito: "))
    dicionario["Saldo"] += deposito
    print ("Deposito efetuado com sucesso!")
    print ("Saldo atual: " + str(dicionario["Saldo"]))

def start():
    contas = []

    controle = True
    while controle:
            
        menu()

        opcao_menu = entrada("Digite uma opção: ")

        if opcao_menu == "1":
            if contas:
                print ("Saldo atual: " + str(conta["Saldo"]))

        elif opcao_menu == "2":
            depositar(contas[0])

        elif opcao_menu == "3":
            saque = float(entrada("Digite o valor de saque: "))
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