class Usuario():
    def __init__(self,id , email, senha, nome):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome

class Anuncios():
    def __init__(self,id , vendedor, nome, preco ):
        self.id = id
        self.vendedor = vendedor
        self.nome = nome
        self.preco = preco

class Repo():
    def __init__(self):
        self.usuarios = []
        self.anuncios = []
        self.next_user_id = 1
        self.next_anuncio_id = 1

    def mostrarUsuarios(self):
        for i in self.usuarios:
            print(f'{i.id} - Email: {i.email} | Senha: {i.senha}')

    def mostrarAnuncios(self, user):
        for i in self.anuncios:
            if i.vendedor == user.id :
                print(f'ID do Anuncio: {i.id} - {i.nome} - Preço: {i.preco} | Id Vendedor: {i.vendedor}')

    def addUsuarioRepo(self, usuario):
        self.next_user_id += 1
        self.usuarios.append(usuario)

    def addAnuncioRepo(self, anuncio):
        self.next_anuncio_id += 1
        self.anuncios.append(anuncio)

    def emailExiste(self, email):
        for n in self.usuarios:
            if n.email == email:
                return False
        return True

    def validadorSenha(self, email, senha):
        for n in self.usuarios:
            if n.email == email:
                if n.senha == senha:
                    return n
        return False

repo = Repo() #aqui eu criei um objeto com base na classe Repo (repo de repositorio)
def menuLogin():
    print('1 - Cadastro')
    print('2 - Login')
    print('0 - Sair')

    opcao = int(input('Escolha: '))

    if opcao == 1:
        funcaoCadastro()

    elif opcao == 2:
        user = funcaoLogin()
        if user:
            while True:
                if menuPrincipal(user) == False:
                    break
        pass

    elif opcao == 0:
        return False

def menuPrincipal(user):
    print('1 - Criar Anuncio')
    print('2 - Meus Anuncios')
    print('3 - Editar Anuncios')
    print('4 - Remover Anuncios')
    print('0 - Sair da Conta')

    opcao = int(input('Escolha: '))

    if opcao == 1:
        criarAnuncio(user)

    elif opcao == 2:
        repo.mostrarAnuncios(user)

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 0:
        return False


def funcaoCadastro():
    email = input('Qual o email para cadastro?')
    if repo.emailExiste(email):
        senha = input('Digite uma senha para o cadastro: ')
        nome = input('Digite o seu nome: ')
        usuario = Usuario(repo.next_user_id,email, senha, nome)
        repo.addUsuarioRepo(usuario)
        repo.mostrarUsuarios()
    else:
        print('Email já existente!!!')
        return

def funcaoLogin ():
    email = input('Qual o seu email de login?')
    if not repo.emailExiste(email):
        senha = input('Digite a sua senha:')
        user = repo.validadorSenha(email, senha)
        print('Seja bem vindo: ', user.nome)
        return user
    else:
        print('Email Inválido!!!')
        return

def criarAnuncio(user):
    nome = input('Qual o nome do anuncio?')
    preco = float(input('Qual o preço do anuncio?'))
    anuncio = Anuncios(repo.next_anuncio_id, user.id, nome, preco)
    repo.addAnuncioRepo(anuncio)

while True:
    if menuLogin() == False:
        break
