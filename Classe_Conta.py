from Classe_Historico import *
from Classe_Cliente import *
from Login import *

class Conta:

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    _total_contas = 0

    def __init__(self, numero, cliente, saldo, limite = 1000):

        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @property
    def historico(self):
        return self._historico

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @saldo.setter
    def saldo(self, saldo):
        if self._saldo < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = saldo

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @historico.setter
    def historico(self, historico):
        self._historico = historico

    def depositar(self, valor, aux = 0):
        if valor < 0:
            print("Valor Inválido!")
        else:
            if aux == 0:
                self.saldo += valor
                self.historico.transacoes.append(f"{data.exibir_hora()} > Deposito de {valor}")
            else:
                self.saldo += valor

    def sacar(self, valor, aux = 0):
        if self.saldo < valor:
            return False
        else:
            if aux == 0:
                self.saldo -= valor
                self.historico.transacoes.append(f"{data.exibir_hora()} > Saque de {valor}")
            else:
                self.saldo -= valor
        return True

    def transferir(self, destino, valor):
        saque = self.sacar(valor, 1)
        if saque == True:
            destino.depositar(valor, 1)
            self.historico.transacoes.append(f"{data.exibir_hora()} > Realizou uma transferencia de {valor:.2f} para "
                                             f"{destino.titular.nome}")
            destino.historico.transacoes.append(f"{data.exibir_hora()} > Recebeu uma transferência de {valor:.2f} de "
                                                f"{self.titular.nome}")
            return True
        else:
            return False

    def extrato(self):
        print(f"Conta: {self.numero} \nsaldo: {self.saldo}")
        self.historico.transacoes.append(f"{data.exibir_hora()} > Retirada de Extrato - Saldo de {self.saldo:.2f}")
