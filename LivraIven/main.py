import pymongo
import conectarBanco
import atualizarLivros
import atualizarUsuario
import atualizarUsuarioAdm
import cadastrarLivro
import consultarLivro
import consultarLivrosTodos
import cadastrarUsuario
import verSeguidoresUsuario
import verLivroU
import visualizarUsuario
import logarUsuario
import verTodosUsuarios
import procurarLivro
import verTodosLivros
import registrarInteracao
import procurarLivro
import atualizarInteracaoUsuario
import verMelhoresLivros
import SeguirUsuarioEVerSeguidores

ADMIN_EMAIL = "admlivrariven@gmail.com"
ADMIN_PASSWORD = "iven123"

# Conectar ao banco de dados
def conectar_banco():
    return pymongo.MongoClient("mongodb+srv://PMART:Ivens3560@pmart.xnmtt.mongodb.net/")






def menu_login():
    while True:
        print("\n-=-=-=- LivraIvens -=-=-=-")
        print("1. Criar conta")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrarUsuario.cadastrar_usuario()
        elif opcao == '2':
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            if email == ADMIN_EMAIL and senha == ADMIN_PASSWORD:
                menu_admin()
            else:
                usuario = logarUsuario.logar_usuario(email, senha)
                if usuario:
                    menu_usuario(usuario)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


def menu_admin():
    while True:
        print("\n-=-=-=- Menu Admin -=-=-=-")
        print("1. Cadastrar livro")
        print("2. Consultar todos os livros")
        print("3. Consultar livro por título")
        print("4. Atualizar usuário")
        print("5. Visualizar dados de um usuário")
        print("6. Ver todos os usuários")  # Nova opção adicionada
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrarLivro.cadastrar_livro()
        elif opcao == '2':
            consultarLivrosTodos.consultar_todos_livros()
        elif opcao == '3':
            consultarLivro.consultar_livro()
        elif opcao == '4':
            atualizarUsuarioAdm.atualizar_usuario_admin()
        elif opcao == '5':
            visualizarUsuario.visualizar_dados_usuario()
        elif opcao == '6':  # Chama a nova função para visualizar todos os usuários
            verTodosUsuarios.ver_todos_usuarios()
        elif opcao == '7':
            print("Saindo do menu admin...")
            break
        else:
            print("Opção inválida!")


def menu_usuario(usuario):
    while True:
        print("\n-=-=-=- Menu Usuário -=-=-=-")
        print("1.  Atualizar nome, email ou senha")
        print("2.  Atualizar livros lidos ou favoritos")
        print("3.  Seguir um usuário")
        print("4.  Ver seguidores")
        print("5.  Ver livros lidos e favoritos")
        print("6.  interação")
        print("7.  Mudar interação")
        print("8.  Ver melhores livros avaliados")
        print("9.  Ver todos os livros disponiveis")
        print("10. Procurar por um livro específico")
        print("11. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            atualizarUsuario.atualizar_usuario(usuario)
        elif opcao == '2':
            atualizarLivros.atualizar_livros_usuario(usuario)
        elif opcao == '3':
            SeguirUsuarioEVerSeguidores.seguir_usuario(usuario)
        elif opcao == '4':
            verSeguidoresUsuario.ver_seguidores_usuario(usuario)
        elif opcao == '5':
            verLivroU.ver_livros_usuario(usuario)
        elif opcao == '6':
            registrarInteracao.registrar_interacao(usuario)
        elif opcao == '7':
            atualizarInteracaoUsuario.atualizar_interacoes_usuario()
        elif opcao == '8':
            verMelhoresLivros.ver_melhores_livros_avaliados()
        elif opcao == '9':
            verTodosLivros.ver_todos_livros()
        elif opcao == '10':
            procurarLivro.procurar_livro()
        elif opcao == '11':
            print("Saindo do menu de usuário...")
            break
        else:
            print("Opção inválida!")

menu_login()