class Livro:
    """
    Classe para gerenciar livros em uma biblioteca.

    Attributes:
        livros (dict): Um dicionário estático para armazenar instâncias de livros, onde a chave é o ID do livro.

    Methods:
        __init__(id_livro, titulo, autor, categoria, isbn, ano_publicacao):
            Inicializa uma nova instância da classe Livro.

        salvar():
            Salva o livro na coleção estática `livros`.

        obter(id_livro):
            Obtém uma instância de Livro com base no ID fornecido.

        atualizar(id_livro, **kwargs):
            Atualiza os atributos de um livro existente.

        deletar(id_livro):
            Remove um livro da coleção com base no ID fornecido.

        listar_todos():
            Lista todos os livros cadastrados.
    """

    livros = {}

    def __init__(self, id_livro, titulo, autor, categoria, isbn, ano_publicacao):
        """
        Inicializa uma nova instância de Livro.

        Args:
            id_livro (int): Identificador único do livro.
            titulo (str): Título do livro.
            autor (str): Autor do livro.
            categoria (str): Categoria ou gênero do livro.
            isbn (str): Código ISBN do livro.
            ano_publicacao (int): Ano de publicação do livro.
        """
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao

    def salvar(self):
        """
        Salva o livro no dicionário estático `livros`.

        Side Effects:
            Adiciona a instância atual ao dicionário estático `livros`.
        
        Prints:
            Confirmação de que o livro foi salvo.
        """
        Livro.livros[self.id_livro] = self
        print(f"Livro {self.id_livro} adicionado com sucesso.")

    @staticmethod
    def obter(id_livro):
        """
        Obtém um livro pelo ID.

        Args:
            id_livro (int): Identificador único do livro.

        Returns:
            Livro: Instância do livro correspondente ao ID, ou None se não encontrado.
        """
        return Livro.livros.get(id_livro)

    @staticmethod
    def atualizar(id_livro, **kwargs):
        """
        Atualiza os atributos de um livro existente.

        Args:
            id_livro (int): Identificador único do livro.
            **kwargs: Parâmetros a serem atualizados no formato chave-valor.

        Side Effects:
            Atualiza os atributos do livro no dicionário estático.

        Prints:
            Confirmação de que o livro foi atualizado ou uma mensagem de erro se não encontrado.
        """
        livro = Livro.obter(id_livro)
        if livro:
            for chave, valor in kwargs.items():
                setattr(livro, chave, valor)
            print(f"Livro {id_livro} atualizado com sucesso.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def deletar(id_livro):
        """
        Remove um livro do dicionário `livros`.

        Args:
            id_livro (int): Identificador único do livro.

        Side Effects:
            Remove a instância correspondente do dicionário estático.

        Prints:
            Confirmação de que o livro foi deletado ou uma mensagem de erro se não encontrado.
        """
        if id_livro in Livro.livros:
            del Livro.livros[id_livro]
            print(f"Livro {id_livro} deletado com sucesso.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def listar_todos():
        """
        Lista todos os livros cadastrados.

        Prints:
            Detalhes de todos os livros armazenados ou uma mensagem indicando que não há livros cadastrados.
        """
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
