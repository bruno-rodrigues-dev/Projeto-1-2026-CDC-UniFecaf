class Usuario():
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
#aqui é a classe usuario e tals
class Repo():
    def __init__(self):
        self.usuarios = []
#esse vai ser o "banco de dados por enquanto", aonde vamos guardar os usuarios
    def mostrarUsuarios(self):
        n = 1
        for i in self.usuarios:
            print(n, f' - Email: {i.email} | Senha: {i.senha}')
            n += 1

    def addUsuarioRepo(self, usuario):
        self.usuarios.append(usuario)

    def validarEmail(self, email):
        for n in self.usuarios:
            if n.email == email:
                print('Email já existente!!!')
                return False
        return True
repo = Repo() #aqui eu criei um objeto com base na classe Repo (repo de repositorio)
def menu():
    print('1 - Cadastro')
    print('2 - Login')
    print('0 - Sair')

    opcao = int(input('Escolha: '))

    if opcao == 1:
        funcaoCadastro()

    elif opcao == 2:
        # funcaoLogin, ainda nao fiz
        pass

    elif opcao == 0:
        return False

def funcaoCadastro():
    email = input('Qual o email para cadastro?')
    if repo.validarEmail(email):
        senha = input('Digite uma senha para o cadastro: ')
        usuario = Usuario(email, senha)
        repo.addUsuarioRepo(usuario)
        repo.mostrarUsuarios()
    else:
        return

while True:
    if menu() == False:
        break