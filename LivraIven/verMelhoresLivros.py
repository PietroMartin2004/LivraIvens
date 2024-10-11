import conectarBanco

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

