import os

class Conta:
    def __init__(self, nome, senha, saldo):
        self.usuario = nome
        self.senha = senha
        self.saldo = saldo

    def sacar(self):
        pass

    def depositar(self, valor):
        self.saldo += valor
    
    def saudar():
        print("OLA")

    def __str__(self):
        return 'Nome: {nome}'.format(nome = self.usuario)

class Maquina:

    def menu():
        os.system('clear')
        print ("MENU PRINCIPAL")
        print ("1 - Saldo")
        print ("2 - Deposito")
        print ("3 - Saque")
        print ("4 - Cadastrar novo usuario")
        print ("5 - Exibir contas")
        print ("6 - Mudar usuario")
        print ("7 - Sair")