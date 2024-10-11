import conectarBanco

def atualizar_interacoes_usuario():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_interacoes = banco["Interacoes"]
    colecao_usuarios = banco["Usuarios"]

    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    usuario = colecao_usuarios.find_one({"email": email, "senha": senha})
    if usuario:
        tipo = input("Digite o novo tipo de interação (curtida, comentário): ")
        comentario = input("Digite o novo comentário (se houver): ")

        while True:
            try:
                avaliacao = float(input("Digite a nova avaliação (0 a 10): "))
                if 0 <= avaliacao <= 10:
                    break
                else:
                    print("Por favor, insira uma avaliação entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número entre 0 e 10.")

        # Atualiza o tipo, comentário e avaliação da interação
        colecao_interacoes.update_many(
            {"usuario": usuario["nome"]},
            {"$set": {"tipo": tipo, "comentario": comentario, "avaliacao": avaliacao}}
        )
        print("Interações do usuário atualizadas com sucesso!")
    else:
        print("Usuário não encontrado!")
