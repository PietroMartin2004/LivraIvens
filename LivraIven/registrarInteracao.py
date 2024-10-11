import conectarBanco

# Função para registrar interações do usuário
def registrar_interacao(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_interacoes = banco["Interacoes"]
    colecao_livros = banco["Livros"]

    livro_titulo = input("Digite o título do livro para o qual deseja registrar uma interação: ")
    livro = colecao_livros.find_one({"título": livro_titulo})

    if livro:
        tipo = input("Digite o tipo de interação (curtida, comentário): ").lower()
        comentario = input("Digite seu comentário (se houver): ")
        
        while True:
            try:
                avaliacao = float(input("Digite a avaliação (0 a 10): "))
                if 0 <= avaliacao <= 10:
                    break
                else:
                    print("Por favor, insira uma avaliação entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número entre 0 e 10.")

        # Armazenar a interação com o nome do usuário, título do livro e avaliação
        interacao = {
            "usuario": usuario["nome"],  # Nome do usuário
            "livro": livro["título"],    # Título do livro
            "tipo": tipo,                # Curtida ou comentário
            "comentario": comentario,    # Comentário (se houver)
            "avaliacao": avaliacao       # Avaliação (0 a 10)
        }

        # Inserir a interação na coleção 'Interacoes'
        colecao_interacoes.insert_one(interacao)
        print("Interação registrada com sucesso!")

        # Atualizar a coleção 'Livros' com a nova avaliação
        colecao_livros.update_one(
            {"_id": livro["_id"]},
            {"$addToSet": {"avaliações": {"usuario": usuario["nome"], "nota": avaliacao}}}
        )

        # Exibir o nome do usuário e título do livro
        print(f"Comentário registrado por: {usuario['nome']} para o livro: {livro['título']} com avaliação de {avaliacao}")
    else:
        print("Livro não encontrado. Verifique o título e tente novamente.")