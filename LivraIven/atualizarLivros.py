import conectarBanco

def atualizar_livros_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]
    colecao_livros = banco["Livros"]

    acao = input("Deseja adicionar livros lidos ou favoritos? (lidos/favoritos): ").lower()
    
    if acao in ["lidos", "favoritos"]:
        livro_titulo = input(f"Digite o título do livro que deseja adicionar aos {acao}: ")
        livro = colecao_livros.find_one({"título": livro_titulo})  # Busca o livro pelo título
        
        if livro:
            if acao == "lidos":
                colecao_usuarios.update_one(
                    {"título": usuario["_id"]},
                    {"$addToSet": {"livrosLidos": livro_titulo}}  # Adiciona o título do livro aos lidos
                )
                print("Livro adicionado aos lidos.")
            elif acao == "favoritos":
                colecao_usuarios.update_one(
                    {"_id": usuario["_id"]},
                    {"$addToSet": {"livrosFavoritos": livro_titulo}}  # Adiciona o título do livro aos favoritos
                )
                print("Livro adicionado aos favoritos.")
        else:
            print("Livro não encontrado. Verifique o título e tente novamente.")
    else:
        print("Opção inválida!")
