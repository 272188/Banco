class Cliente:

    __slots__ = ['nome', 'sobrenome', 'cpf']

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf