lista_usuarios = {}

class Login:

    __slots__ = ['_login', '_senha']

    def __init__(self, login, senha):
        self._login = login
        self._senha = senha
        lista_usuarios.setdefault(login, senha)

    def login(self, nome, senha):
        for i in lista_usuarios.keys():
            if nome == i:
                if senha == lista_usuarios[nome]:
                    return True
                else:
                    print("Senha Incorreta!")
                    return False
        print("Cliente não cadastrado!")