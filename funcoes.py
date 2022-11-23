import os
from time import sleep
from model import Maquina, Conta

def start():
    contas = []
    conta_logada = None

    os.system('clear')
    print("***************************\n Bem-vindo ao Banco Comuna \n***************************")
    print("\nPARA INICIAR, CADASTRE UM USUÁRIO E FAÇA UM DEPÓSITO INICIAL\n")
    cadastrar(contas)
    controle = True
    
    while controle:
        if conta_logada is None:
            conta_logada = login(contas)
            limpa_tela()
        
        if conta_logada:
            Maquina.menu()

            opcao_menu = entrada("Digite uma opção: ")

            if opcao_menu == "1":
                ver_saldo(conta_logada)
                Maquina.menu()
                
            elif opcao_menu == "2":
                depositar(conta_logada)
                Maquina.menu()

            elif opcao_menu == "3":
                sacar(conta_logada)
                Maquina.menu()

            elif opcao_menu == "4":
                cadastrar(contas)
                Maquina.menu()

            elif opcao_menu == "5":
                print("As seguintes contas estão cadastradas atualmente:\n")
                print(conta_logada)
                limpa_tela()
                Maquina.menu()

            elif opcao_menu =="6":
                conta_logada = login(contas)
                limpa_tela()
                Maquina.menu()
            
            elif opcao_menu == "7":
                conta_logada = None
                print("*************************\n Adeus ao Banco Comuna \n *****************")

            else:
                print ("Opcao inválida!")

def entrada(texto):
    return input(texto)
    
def limpa_tela():
    c = input("Digite qualquer coisa para continuar")
    if c:
        os.system('clear')

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

def sacar(conta):
    valor_saque = float(entrada("Digite o valor de saque: "))
    if valor_saque > dicionario["Saldo"]:
        print ("Saldo insuficiente!")
        limpa_tela()
    else:
        conta.sacar (valor_saque)
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
    for conta in contas:
        if usr == conta["Usuario"] and pwd == conta["Senha"]:
            print("Login realizado com sucesso!\nRetornando ao menu inicial...")
            limpa_tela()
            return conta
            
    print("Login incorreto!\nRetornando ao menu inicial...")
    return None