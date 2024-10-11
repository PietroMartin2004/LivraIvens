import conectarBanco

# Funções para Usuário
def atualizar_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo email: ")
    nova_senha = input("Digite a nova senha: ")

    colecao.update_one(
        {"_id": usuario["_id"]},
        {"$set": {"nome": novo_nome, "email": novo_email, "senha": nova_senha}}
    )
    print("Informações atualizadas com sucesso!")
