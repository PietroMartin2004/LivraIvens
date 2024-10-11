import conectarBanco

def logar_usuario(email, senha):
    conexao = conectarBanco.conectar_banco()
    banco = conexao["Banco"]
    colecao = banco["Usuarios"]

    usuario = colecao.find_one({"email": email, "senha": senha})
    if usuario:
        print(f"Bem-vindo, {usuario['nome']}!")
        return usuario
    else:
        print("Email ou senha incorretos!")
        return None