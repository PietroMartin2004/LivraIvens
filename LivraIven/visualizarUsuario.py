import conectarBanco

def visualizar_dados_usuario():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    usuario = colecao.find_one({"email": email, "senha": senha})
    if usuario:
        print(f"Livros Lidos: {usuario['livrosLidos']}")
        print(f"Livros Favoritos: {usuario['livrosFavoritos']}")
        print(f"Seguindo: {usuario['seguindo']}")
        print(f"Seguidores: {usuario['seguidores']}")
    else:
        print("Usuário não encontrado!")