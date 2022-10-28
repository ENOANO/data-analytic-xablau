import os
import time

os.system('clear')
deposito = float(input("Digite o valor do deposito: "))
usuario = input("Digite o nome do usuario: ")
saldo = deposito
conta = {"Usuario": usuario, "Saldo": saldo}
print (conta)
time.sleep(3)
os.system('clear')

print ("MENU PRINCIPAL \n")
print ("1 - Saldo")
print ("2 - Deposito")
print ("3 - Saque")
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

else:
    print ("Opcao invalida!")