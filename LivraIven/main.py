import pymongo
import conectarBanco
import funcaoADM
import funcaoUsuarios
import funcaoLivros
import funcaoInteracaos
import deletar

"""--------------------------------------------------------------"""

ADMIN_EMAIL = "admiven@gmail.com"
ADMIN_PASSWORD = "iven123"

"""--------------------------------------------------------------"""

def menu_login():
    while True:
        print("\n-=-=-=- LivraIvens -=-=-=-")
        print("1. Criar conta")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcaoUsuarios.cadastrar_usuario()
        elif opcao == '2':
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            if email == ADMIN_EMAIL and senha == ADMIN_PASSWORD:
                menu_admin()
            else:
                usuario = funcaoUsuarios.logar_usuario(email, senha)
                if usuario:
                    menu_usuario(usuario)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

"""--------------------------------------------------------------"""

def menu_admin():
    while True:
        print("\n-=-=-=- Menu Admin -=-=-=-")
        print("1. Cadastrar livro")
        print("2. Consultar todos os livros")
        print("3. Consultar livro por título")
        print("4. Atualizar usuário")
        print("5. Visualizar dados de um usuário")
        print("6. Ver todos os usuários")
        print("7. Deletar Usuario/interação/Livro")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcaoLivros.cadastrar_livro()
        elif opcao == '2':
            funcaoLivros.consultar_todos_livros()
        elif opcao == '3':
            funcaoLivros.consultar_livro()
        elif opcao == '4':
            funcaoADM.atualizar_usuario_admin()
        elif opcao == '5':
            funcaoUsuarios.visualizar_dados_usuario()
        elif opcao == '6':
            funcaoUsuarios.ver_todos_usuarios()
        elif opcao == '7':
            deletar.deletar_opcao()
        elif opcao == '8':
            print("Saindo do menu admin...")
            break
        else:
            print("Opção inválida!")

"""--------------------------------------------------------------"""

def menu_usuario(usuario):
    while True:
        print("\n-=-=-=- Menu Usuário -=-=-=-")
        print("1.  Atualizar nome, email ou senha")
        print("2.  Atualizar livros lidos ou favoritos")
        print("3.  Seguir um usuário")
        print("4.  Ver seguidores")
        print("5.  Ver livros lidos e favoritos")
        print("6.  Registrar interação")
        print("7.  Mudar interação")
        print("8.  Ver melhores livros avaliados")
        print("9.  Ver todos os livros disponíveis")
        print("10. Procurar por um livro específico")
        print("11. Excluir conta")
        print("12. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcaoUsuarios.atualizar_usuario(usuario)
        elif opcao == '2':
            funcaoUsuarios.atualizar_livros_usuario(usuario)
        elif opcao == '3':
            funcaoUsuarios.seguir_usuario(usuario)
        elif opcao == '4':
            funcaoUsuarios.ver_seguidores_usuario(usuario)
        elif opcao == '5':
            funcaoUsuarios.ver_livros_usuario(usuario)
        elif opcao == '6':
            funcaoInteracaos.registrar_interacao(usuario)
        elif opcao == '7':
            funcaoInteracaos.atualizar_interacoes_usuario()
        elif opcao == '8':
            funcaoLivros.ver_melhores_livros_avaliados()
        elif opcao == '9':
            funcaoLivros.ver_todos_livros()
        elif opcao == '10':
            funcaoLivros.procurar_livro()
        elif opcao == '11':
            if deletar.excluir_conta_usuario(usuario):
                break 
        elif opcao == '12':
            print("Saindo do menu de usuário...")
            break
        else:
            print("Opção inválida!")

"""--------------------------------------------------------------"""

# 50 usuários, 30 livros e 80

menu_login()