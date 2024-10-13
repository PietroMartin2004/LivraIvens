import conectarBanco

"""--------------------------------------------------------------"""

#Função para ADMIN
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

"""--------------------------------------------------------------"""

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



def consultar_todos_livros():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Livros"]

    todos_livros = colecao.find()
    for book in todos_livros:
        print(book)

"""--------------------------------------------------------------"""

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

"""--------------------------------------------------------------"""

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

"""--------------------------------------------------------------"""

def ver_melhores_livros_avaliados():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_interacoes = banco["Interacoes"]
    
    # Agregação para calcular a média das avaliações de cada livro
    pipeline = [
        {
            "$group": {
                "_id": "$livro",
                "media_avaliacoes": {"$avg": "$avaliacao"},
                "avaliacoes_count": {"$sum": 1}
            }
        },
        {
            "$sort": {"media_avaliacoes": -1}  # Ordenar pela média das avaliações (maior para menor)
        },
        {
            "$limit": 10  # Limitar aos 10 melhores avaliados
        }
    ]
    
    melhores_livros = list(colecao_interacoes.aggregate(pipeline))
    
    print("\n-=-=-=- Melhores Livros Avaliados -=-=-=-")
    if melhores_livros:
        for livro in melhores_livros:
            print(f"Livro: {livro['_id']}, Média de Avaliações: {livro['media_avaliacoes']:.2f}, Número de Avaliações: {livro['avaliacoes_count']}")
    else:
        print("Nenhum livro avaliado até o momento.")

"""--------------------------------------------------------------"""