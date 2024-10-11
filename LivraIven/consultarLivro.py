import conectarBanco

def consultar_livro():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Livros"]

    titulo = input("Digite o título do livro que deseja consultar: ")
    livro = colecao.find_one({"título": titulo})
    if livro:
        print(livro)
    else:
        print("Livro não encontrado!")