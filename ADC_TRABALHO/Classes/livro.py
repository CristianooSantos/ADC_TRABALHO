class Livro:
    livros = {}  

    def __init__(self, isbn, titulo, autor, categoria, ano_publicacao):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano_publicacao = ano_publicacao

    def salvar(self):
        Livro.livros[self.isbn] = self
        print(f"Livro '{self.titulo}' adicionado com sucesso.")

    @staticmethod
    def obter(isbn):
        return Livro.livros.get(isbn)

    @staticmethod
    def atualizar(isbn, **kwargs):
        livro = Livro.obter(isbn)
        if livro:
            for chave, valor in kwargs.items():
                setattr(livro, chave, valor)
            print(f"Livro '{isbn}' atualizado com sucesso.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def deletar(isbn):
        if isbn in Livro.livros:
            del Livro.livros[isbn]
            print(f"Livro '{isbn}' deletado com sucesso.")
        else:
            print("Livro não encontrado.")
