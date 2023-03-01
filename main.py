from Classe_Conta import *

from Classe_Banco import *
l1 = Login('Sheila', '123')

banco = Banco()


if l1.login('Sheila', '123') == True:
    cliente1 = Cliente('Sheila', 'Paloma Brito', '012.345.678-12')
    c1 = Conta('01', cliente1, 200.00)
    cliente2 = Cliente('Antonio', 'Silva', '987.654.321-00')
    c2 = Conta('02', cliente2, 640.00)
    banco.cadastrarConta(c1)
    banco.cadastrarConta(c2)
    banco.exibirContas()
    banco.excluirConta('02')
    print("")
    banco.exibirContas()

