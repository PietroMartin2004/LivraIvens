import conectarBanco
# Funções do Admin
def cadastrar_livro():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Livros"]

    titulo = input("Digite o título: ") 
    autor = input("Digite o autor: ")
    genero = input("Digite o gênero: ")
    editora = input("Digite a editora: ")
    
    livro = {
        "título": titulo,
        "autor": autor,
        "gênero": genero,
        "editora": editora,
        "avaliações": []
    }

    result = colecao.insert_one(livro)
    print(f"Livro cadastrado com ID: {result.inserted_id}")