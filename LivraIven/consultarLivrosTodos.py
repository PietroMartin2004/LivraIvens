import conectarBanco

def consultar_todos_livros():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Livros"]

    all_books = colecao.find()
    for book in all_books:
        print(book)
