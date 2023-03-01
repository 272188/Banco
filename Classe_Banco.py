from Classe_Conta import *

class Banco:

    __slots__ = ['_lista_contas']

    def __init__(self):
        self._lista_contas = []

    def cadastrarConta(self,conta):
        if conta in self._lista_contas:
            print("Essa conta já está cadastrada!")
        else:
            self._lista_contas.append(conta)
            print("Conta cadastrada com sucesso!")

    def exibirContas(self):
        for i in self._lista_contas:
            print(f"Conta {i.numero} > {i.titular.nome} {i.titular.sobrenome}")

    def excluirConta(self, num):
        for i in self._lista_contas:
            if i.numero == num:
                self._lista_contas.remove(i)