import datetime as dt

class Data:
    def __init__(self):
        aux = dt.datetime.now()
        self.hora = f'{aux.day}/{aux.month}/{aux.year} {aux.hour}:{aux.minute}:{aux.second}'

    def exibir_hora(self):
        return self.hora
data = Data()

class Historico:

    __slots__ = ['data_abertura', 'transacoes']

    def __init__(self):
        self.data_abertura = data.exibir_hora()
        self.transacoes = []

    def imprime(self):
        print(f"Data de Abertura: {self.data_abertura}")
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)
