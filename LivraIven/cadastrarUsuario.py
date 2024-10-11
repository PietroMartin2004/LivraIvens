import conectarBanco

# Função de login/registro
def cadastrar_usuario():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "livrosLidos": [],
        "livrosFavoritos": [],
        "seguindo": [],
        "seguidores": []
    }

    result = colecao.insert_one(usuario)
    print(f"Usuário cadastrado com ID: {result.inserted_id}")




