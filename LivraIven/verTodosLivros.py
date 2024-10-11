import conectarBanco

def ver_todos_livros():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_livros = banco["Livros"]
    
    livros = list(colecao_livros.find({}))
    
    print("\n-=-=-=- Todos os Livros Disponiveis -=-=-=-")
    if livros:
        for livro in livros:
            print(f"Título: {livro['título']}, Autor: {livro.get('autor', 'Desconhecido')}")
    else:
        print("Nenhum livro cadastrado no momento.")
