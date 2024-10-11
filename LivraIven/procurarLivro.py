import conectarBanco

def procurar_livro():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_livros = banco["Livros"]
    
    titulo = input("Digite o título do livro que deseja procurar: ")
    livro = colecao_livros.find_one({"título": titulo})
    
    if livro:
        print(f"Título: {livro['título']}, Autor: {livro.get('autor', 'Desconhecido')}")
    else:
        print("Livro não encontrado.")
