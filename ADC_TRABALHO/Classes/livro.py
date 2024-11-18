class Livro:
    livros = {}  

    def __init__(self, id_livro, titulo, autor, categoria, isbn, ano_publicacao):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao

    def salvar(self):
        Livro.livros[self.id_livro] = self
        print(f"Livro {self.id_livro} adicionado com sucesso.")

    @staticmethod
    def obter(id_livro):
        return Livro.livros.get(id_livro)

    @staticmethod
    def atualizar(id_livro, **kwargs):
        livro = Livro.obter(id_livro)
        if livro:
            for chave, valor in kwargs.items():
                setattr(livro, chave, valor)
            print(f"Livro {id_livro} atualizado com sucesso.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def deletar(id_livro):
        if id_livro in Livro.livros:
            del Livro.livros[id_livro]
            print(f"Livro {id_livro} deletado com sucesso.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def listar_todos():
        if Livro.livros:
            print("\nLista de Livros:")
            for livro in Livro.livros.values():
                print(f"\nID: {livro.id_livro}")
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Categoria: {livro.categoria}")
                print(f"ISBN: {livro.isbn}")
                print(f"Ano de Publicação: {livro.ano_publicacao}")
                print("-" * 30)
        else:
            print("Nenhum livro cadastrado.")
