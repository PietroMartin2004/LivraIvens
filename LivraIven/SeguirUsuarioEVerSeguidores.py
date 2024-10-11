import conectarBanco

def seguir_usuario(usuario):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]

    nome_seguido = input("Digite o nome do usuário que deseja seguir: ")
    
    usuario_seguido = colecao_usuarios.find_one({"nome": nome_seguido})
    
    if usuario_seguido:

        if usuario_seguido["nome"] in usuario.get("seguindo", []):
            print(f"Você já está seguindo {nome_seguido}.")
        else:
            
            colecao_usuarios.update_one(
                {"_id": usuario["_id"]},
                {"$addToSet": {"seguindo": usuario_seguido["nome"]}} 
            )
            # Atualiza a lista de "seguidores" do usuário seguido
            colecao_usuarios.update_one(
                {"_id": usuario_seguido["_id"]},
                {"$addToSet": {"seguidores": usuario["nome"]}}
            )
            print(f"Você agora está seguindo {nome_seguido}.")
    else:
        print("Usuário não encontrado.")


def ver_seguidores():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    nome_usuario = input("Digite o nome do usuário: ")
    usuario = colecao.find_one({"nome": nome_usuario})

    if usuario:
        seguidores = colecao.find({"_id": {"$in": usuario["seguidores"]}})
        print(f"Seguidores de {nome_usuario}:")
        for seguidor in seguidores:
            print(seguidor["nome"])
    else:
        print("Usuário não encontrado.")

