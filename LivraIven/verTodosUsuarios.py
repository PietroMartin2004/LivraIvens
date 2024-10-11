import conectarBanco

def ver_todos_usuarios():
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao_usuarios = banco["Usuarios"]

    usuarios = list(colecao_usuarios.find({}))

    print("\n-=-=-=- Todos os Usuários -=-=-=-")
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario.get('nome', 'Desconhecido')}, Email: {usuario['email']}")
    else:
        print("Nenhum usuário cadastrado no momento.")
