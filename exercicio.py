import os
import time

contas = []
"""
check if the solution below is better than the one on line 17
conta = {}

for conta in contas: 
    usuario = "Usuario"
    saldo = "Saldo"
"""
os.system('clear')
usuario = input("Digite o nome do usuario: ")
deposito = float(input("Digite o valor do deposito inicial: "))
saldo = deposito
conta = {"Usuario": usuario, "Saldo": saldo}
contas.append(conta)
print (conta)
time.sleep(2)
os.system('clear')

print ("MENU PRINCIPAL \n")
print ("1 - Saldo")
print ("2 - Deposito")
print ("3 - Saque")
print ("4 - Cadastrar novo usuario")

opcao_menu = input("Digite a opcao desejada: ")

if opcao_menu == "1":
    print ("Saldo atual: " + str(conta["Saldo"]))

if opcao_menu == "2":
    deposito = float(input("Digite o valor do deposito: "))
    conta["Saldo"]=saldo+deposito
    print ("Deposito efetuado com sucesso!")
    print ("Saldo atual: " + str(conta["Saldo"]))

if opcao_menu == "3":
    saque = float(input("Digite o valor a sacar: "))
    if saque > saldo:
        print ("Saldo insuficiente!")
    else:
        conta["Saldo"]=saldo-saque
        print ("Saque efetuado com sucesso!")
        print ("Saldo atual: " + str(conta["Saldo"]))

if opcao_menu == "4":
    usuario = input("Digite o nome do usuario: ")
    deposito = float(input("Digite o valor do deposito inicial: "))
    saldo = deposito
    conta = {"Usuario": usuario, "Saldo": saldo}
    contas.append(conta)
    print ("Conta cadastrada com sucesso!")
    print (contas)

else:
    print ("Opcao invalida!")