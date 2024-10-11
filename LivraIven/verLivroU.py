import conectarBanco
# Função para visualizar livros lidos e favoritos
def ver_livros_usuario(usuario):
    print(f"\nLivros Lidos: {usuario['livrosLidos']}")
    print(f"Livros Favoritos: {usuario['livrosFavoritos']}")