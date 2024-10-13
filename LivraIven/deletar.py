import conectarBanco

"""--------------------------------------------------------------"""

def deletar_opcao():
    print("\nEscolha o que deseja deletar:")
    print("1. Deletar Usuário")
    print("2. Deletar Interação")
    print("3. Deletar Livro")
    opcao_delete = input("Escolha uma opção: ")

    if opcao_delete == '1':
        deletar_usuario()
    elif opcao_delete == '2':
        deletar_interacao()
    elif opcao_delete == '3':
        deletar_livro()
    else:
        print("Opção inválida!")

"""--------------------------------------------------------------"""

def deletar_usuario():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]

    email = input("Digite o email do usuário que deseja deletar: ")
    usuario = colecao_usuarios.find_one({"email": email})

    if usuario:
        colecao_usuarios.delete_one({"email": email})
        print(f"Usuário com email {email} foi deletado com sucesso!")
    else:
        print("Usuário não encontrado.")

"""--------------------------------------------------------------"""

def deletar_interacao():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_interacoes = banco["Interacoes"]

    usuario_nome = input("Digite o nome do usuário da interação: ")
    livro_titulo = input("Digite o título do livro da interação: ")

    interacao = colecao_interacoes.find_one({"usuario": usuario_nome, "livro": livro_titulo})

    if interacao:
        colecao_interacoes.delete_one({"usuario": usuario_nome, "livro": livro_titulo})
        print(f"Interação de {usuario_nome} com o livro '{livro_titulo}' foi deletada.")
    else:
        print("Interação não encontrada.")

"""--------------------------------------------------------------"""

def deletar_livro():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_livros = banco["Livros"]

    titulo = input("Digite o título do livro que deseja deletar: ")
    livro = colecao_livros.find_one({"título": titulo})

    if livro:
        colecao_livros.delete_one({"título": titulo})
        print(f"O livro '{titulo}' foi deletado com sucesso!")
    else:
        print("Livro não encontrado.")

"""--------------------------------------------------------------"""

def excluir_conta_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]

    confirmacao = input("Tem certeza que deseja excluir sua conta? (sim/não): ").lower()

    if confirmacao == "sim":
        #Exclui a conta do usuário logado
        colecao_usuarios.delete_one({"_id": usuario["_id"]})
        print("Sua conta foi excluída com sucesso.")
        return True
    else:
        print("Exclusão de conta cancelada.")
        return False
    
"""--------------------------------------------------------------"""