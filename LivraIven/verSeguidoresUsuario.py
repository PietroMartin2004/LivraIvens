import conectarBanco

# Função para ver apenas os seguidores do usuário
def ver_seguidores_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    # Encontra os usuários que seguem o usuário atual
    seguidores = colecao.find({"_id": {"$in": usuario["seguidores"]}})
    print(f"Seguidores de {usuario['nome']}:")
    for seguidor in seguidores:
        print(seguidor["nome"])