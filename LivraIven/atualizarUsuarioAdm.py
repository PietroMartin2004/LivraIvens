import conectarBanco

def atualizar_usuario_admin():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    email = input("Digite o email do usuário a ser atualizado: ")
    senha = input("Digite a senha do usuário: ")
    
    usuario = colecao.find_one({"email": email, "senha": senha})
    if usuario:
        novo_nome = input("Digite o novo nome: ")
        nova_senha = input("Digite a nova senha: ")

        colecao.update_one(
            {"email": email, "senha": senha},
            {"$set": {"nome": novo_nome, "senha": nova_senha}}
        )
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado!")