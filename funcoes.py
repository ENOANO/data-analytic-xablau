import os
from time import sleep

def start():
    contas = []
    
    os.system('clear')
    print("***************************\n Bem-vindo ao Banco Comuna \n***************************")
    print("\nPARA INICIAR, CADASTRE UM USUÁRIO E FAÇA UM DEPÓSITO INICIAL\n")
    cadastrar(contas)
    controle = True
    
    while controle:
            
        menu()

        opcao_menu = entrada("Digite uma opção: ")

        if opcao_menu == "1":
            if contas:
                ver_saldo(contas[0])
            else:
                print ("Não há contas cadastradas")

        elif opcao_menu == "2":
            depositar(contas[0])

        elif opcao_menu == "3":
            sacar(contas[0])

        elif opcao_menu == "4":
            cadastrar(contas)

        elif opcao_menu == "5":
            print("As seguintes contas estão cadastradas atualmente:\n")
            print(contas)
            limpa_tela()

        elif opcao_menu =="6":
           login(contas)
           limpa_tela()

        elif opcao_menu == "0":
            controle = False
            print("*************************\n Adeus ao Banco Comuna \n *****************")

        else:
            print ("Opcao inválida!")

def menu():
    os.system('clear')
    print ("MENU PRINCIPAL")
    print ("1 - Saldo")
    print ("2 - Deposito")
    print ("3 - Saque")
    print ("4 - Cadastrar novo usuario")
    print ("5 - Exibir contas")
    print ("6 - Mudar usuario")
    print ("0 - Sair")

def entrada(texto):
    return input(texto)
    
def limpa_tela():
    sleep(4)
    os.system('clear')
    menu()

def ver_saldo(dicionario):
    print ("Usuário: " + str(dicionario["Usuario"]))
    print ("Saldo atual: " + str(dicionario["Saldo"]))
    limpa_tela()
    
def depositar(dicionario):
    deposito = float(entrada("Digite o valor de deposito: "))
    dicionario["Saldo"] += deposito
    print ("Deposito efetuado com sucesso!")
    print ("Usuário: " + str(dicionario["Usuario"]))
    print ("Saldo atual: " + str(dicionario["Saldo"]))
    limpa_tela()

def sacar(dicionario):
    valor_saque = float(entrada("Digite o valor de saque: "))
    if valor_saque > dicionario["Saldo"]:
        print ("Saldo insuficiente!")
        limpa_tela()
    else:
        dicionario["Saldo"]=dicionario["Saldo"]-valor_saque
        print ("Saque efetuado com sucesso!")
        print ("Usuário: " + str(dicionario["Usuario"]))
        print ("Saldo atual: " + str(dicionario["Saldo"]))
        limpa_tela()

def cadastrar(contas):
    usuario = input("Digite o nome do usuario: ")
    senha = input("Digite a senha: ")
    deposito = float(input("Digite o valor do deposito: "))
    saldo = deposito
    conta = {"Usuario": usuario, "Senha": senha, "Saldo": saldo}
    contas.append(conta)
    print ("\n Conta cadastrada com sucesso! \n")
    limpa_tela()

def login(contas):
    usr = input("Digite o nome do usuário: ")
    pwd = input("Digite a senha: ")
    login = 1
    while login != 1:
        for conta in contas:
            if usr == conta["Usuario"] and pwd == conta["Senha"]:
                login = 1
                print("Login realizado com sucesso!\nRetornando ao menu inicial...")
                limpa_tela()
            else:
                print("Login incorreto!\nRetornando ao menu inicial...")
                limpa_tela()