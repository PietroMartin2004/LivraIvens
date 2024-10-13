import conectarBanco

"""--------------------------------------------------------------"""

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

"""--------------------------------------------------------------"""

def atualizar_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo email: ")
    nova_senha = input("Digite a nova senha: ")

    colecao.update_one(
        {"_id": usuario["_id"]},
        {"$set": {"nome": novo_nome, "email": novo_email, "senha": nova_senha}}
    )
    print("Mudança atualizadas com sucesso!")

"""--------------------------------------------------------------"""

def logar_usuario(email, senha):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    usuario = colecao.find_one({"email": email, "senha": senha})
    if usuario:
        print(f"Bem-vindo, {usuario['nome']}!")
        return usuario
    else:
        print("Email ou senha incorretos!")
        return None

"""--------------------------------------------------------------"""

def seguir_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]

    nome_seguido = input("Digite o nome do usuário que deseja seguir: ")
    
    usuario_seguido = colecao_usuarios.find_one({"nome": nome_seguido})
    
    if usuario_seguido:

        if usuario_seguido["nome"] in usuario.get("seguindo", []):
            print(f"Você já está seguindo {nome_seguido}.")
        else:
            
            colecao_usuarios.update_one(
                {"_id": usuario["_id"]},
                {"$addToSet": {"seguindo": usuario_seguido["nome"]}} 
            )
            #Atualiza a lista de "seguidores" do usuário seguido
            colecao_usuarios.update_one(
                {"_id": usuario_seguido["_id"]},
                {"$addToSet": {"seguidores": usuario["nome"]}}
            )
            print(f"Você agora está seguindo {nome_seguido}.")
    else:
        print("Usuário não encontrado.")

"""--------------------------------------------------------------"""

def ver_seguidores_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]


    seguidores = colecao.find({"_id": {"$in": usuario["seguidores"]}})
    print(f"Seguidores de {usuario['nome']}:")
    for seguidor in seguidores:
        print(seguidor["nome"])

"""--------------------------------------------------------------"""

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

"""--------------------------------------------------------------"""

def ver_todos_usuarios():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]

    usuarios = list(colecao_usuarios.find({}))

    print("\n-=-=-=- Todos os Usuários -=-=-=-")
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario.get('nome', 'Desconhecido')}, Email: {usuario['email']}")
    else:
        print("Nenhum usuário cadastrado no momento.")

"""--------------------------------------------------------------"""

#Função para visualizar livros lidos e favoritos
def ver_livros_usuario(usuario):
    print(f"\nLivros Lidos: {usuario['livrosLidos']}")
    print(f"Livros Favoritos: {usuario['livrosFavoritos']}")

"""--------------------------------------------------------------"""

def atualizar_livros_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]
    colecao_livros = banco["Livros"]

    acao = input("Deseja adicionar livros lidos ou favoritos? (lidos/favoritos): ").lower()
    
    if acao in ["lidos", "favoritos"]:
        livro_titulo = input(f"Digite o título do livro que deseja adicionar aos {acao}: ")
        livro = colecao_livros.find_one({"título": livro_titulo})  #Busca o livro pelo titulo
        
        if livro:
            if acao == "lidos".lower():
                colecao_usuarios.update_one(
                    {"_id": usuario["_id"]},
                    {"$addToSet": {"livrosLidos": livro_titulo}}  #Adiciona o título do livro aos lidos
                )
                print("Livro adicionado aos lidos.")
            elif acao == "favoritos".lower():
                colecao_usuarios.update_one(
                    {"_id": usuario["_id"]},
                    {"$addToSet": {"livrosFavoritos": livro_titulo}}  #Adiciona o título do livro aos favoritos
                )
                print("Livro adicionado aos favoritos.")
        else:
            print("Livro não encontrado. Verifique o título e tente novamente.")
    else:
        print("Opção inválida!")

"""--------------------------------------------------------------"""