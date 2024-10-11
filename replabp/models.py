class Usuario:
    def __init__(self, nome, senha, papel):
        self.nome = nome
        self.senha = senha
        self.papel = papel


users_lista = []
novo_user = Usuario("isabel", "123", "admin")
users_lista.append(novo_user)

