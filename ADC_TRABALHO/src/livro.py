import pickle

class Livro:
    """Classe para gerenciar os livros de uma biblioteca.

    Atributos:
        livros (dict): Dicionário estático contendo todos os livros cadastrados.
        emprestimos (dict): Dicionário estático contendo os registros de empréstimos dos livros.
    """
    livros = {}  
    emprestimos = {}  

    def __init__(self, id_livro, titulo, autor, categoria, isbn, ano_publicacao):
        """Inicializa um livro com os dados fornecidos.

        Args:
            id_livro (str): Identificador único do livro.
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
        self.disponivel = True 

    def salvar(self):
        """Salva o livro no dicionário estático `Livro.livros`.

        Registra também o número de empréstimos para o livro.

        Exemplo:
            >>> livro = Livro("001", "A Arte da Programação", "Donald Knuth", "Computação", "978-0134670958", 1968)
            >>> livro.salvar()
            Livro 001 adicionado com sucesso.
        """
        Livro.livros[self.id_livro] = self
        Livro.emprestimos[self.id_livro] = 0  
        print(f"Livro {self.id_livro} adicionado com sucesso.")

    @staticmethod
    def obter(id_livro):
        """Busca um livro pelo ID.

        Args:
            id_livro (str): ID do livro a ser buscado.

        Returns:
            Livro: O livro encontrado, ou None se não encontrado.

        Exemplo:
            >>> Livro.obter("001")
            <Livro object>
        """
        return Livro.livros.get(id_livro)

    @staticmethod
    def atualizar(id_livro, **kwargs):
        """Atualiza as informações de um livro existente.

        Args:
            id_livro (str): ID do livro a ser atualizado.
            **kwargs**: Atributos do livro que precisam ser atualizados.

        Levanta:
            KeyError: Se o livro não for encontrado.

        Exemplo:
            >>> Livro.atualizar("001", titulo="Estruturas de Dados", autor="Mark Allen Weiss")
            Livro 001 atualizado com sucesso.
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
        """Remove um livro do sistema.

        Args:
            id_livro (str): ID do livro a ser removido.

        Levanta:
            KeyError: Se o livro não for encontrado.

        Exemplo:
            >>> Livro.deletar("001")
            Livro 001 deletado com sucesso.
        """
        if id_livro in Livro.livros:
            del Livro.livros[id_livro]
            del Livro.emprestimos[id_livro]  
            print(f"Livro {id_livro} deletado com sucesso.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def listar_todos():
        """Lista todos os livros cadastrados.

        Exemplo:
            >>> Livro.listar_todos()
            ID: 001
            Título: A Arte da Programação
            Autor: Donald Knuth
            Categoria: Computação
            ISBN: 978-0134670958
            Ano de Publicação: 1968
            Disponível: Sim
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
                print(f"Disponível: {'Sim' if livro.disponivel else 'Não'}")
                print("-" * 30)
        else:
            print("Nenhum livro cadastrado.")

    @staticmethod
    def filtrar_por_categoria(categoria):
        """Filtra os livros pela categoria.

        Args:
            categoria (str): Categoria para a filtragem.

        Exemplo:
            >>> Livro.filtrar_por_categoria("Computação")
            Livros na categoria 'Computação':
            ID: 001, Título: A Arte da Programação, Disponível: Sim
        """
        encontrados = [livro for livro in Livro.livros.values() if livro.categoria.lower() == categoria.lower()]
        if encontrados:
            print(f"\nLivros na categoria '{categoria}':")
            for livro in encontrados:
                print(f"ID: {livro.id_livro}, Título: {livro.titulo}, Disponível: {'Sim' if livro.disponivel else 'Não'}")
        else:
            print(f"Nenhum livro encontrado na categoria '{categoria}'.")

    @staticmethod
    def verificar_disponibilidade(id_livro):
        """Verifica a disponibilidade de um livro.

        Args:
            id_livro (str): ID do livro a ser verificado.

        Exemplo:
            >>> Livro.verificar_disponibilidade("001")
            O livro 'A Arte da Programação' está disponível.
        """
        livro = Livro.obter(id_livro)
        if livro:
            estado = "disponível" if livro.disponivel else "indisponível"
            print(f"O livro '{livro.titulo}' está {estado}.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def emprestar(id_livro):
        """Empresta um livro, alterando seu status de disponibilidade.

        Args:
            id_livro (str): ID do livro a ser emprestado.

        Levanta:
            KeyError: Se o livro não for encontrado.

        Exemplo:
            >>> Livro.emprestar("001")
            Livro 'A Arte da Programação' emprestado com sucesso.
        """
        livro = Livro.obter(id_livro)
        if livro:
            if livro.disponivel:
                livro.disponivel = False
                Livro.emprestimos[id_livro] += 1  
                print(f"Livro '{livro.titulo}' emprestado com sucesso.")
            else:
                print(f"O livro '{livro.titulo}' já está emprestado.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def devolver(id_livro):
        """Devolve um livro, alterando seu status de disponibilidade.

        Args:
            id_livro (str): ID do livro a ser devolvido.

        Exemplo:
            >>> Livro.devolver("001")
            Livro 'A Arte da Programação' devolvido com sucesso.
        """
        livro = Livro.obter(id_livro)
        if livro:
            if not livro.disponivel:
                livro.disponivel = True
                print(f"Livro '{livro.titulo}' devolvido com sucesso.")
            else:
                print(f"O livro '{livro.titulo}' já está disponível.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def gerar_relatorio_mais_emprestados():
        """Gera um relatório dos livros mais emprestados.

        Exemplo:
            >>> Livro.gerar_relatorio_mais_emprestados()
            Relatório de Livros Mais Emprestados:
            Título: A Arte da Programação, Empréstimos: 3
        """
        if Livro.emprestimos:
            print("\nRelatório de Livros Mais Emprestados:")
            ordenados = sorted(Livro.emprestimos.items(), key=lambda item: item[1], reverse=True)
            for id_livro, emprestimos in ordenados:
                livro = Livro.obter(id_livro)
                print(f"Título: {livro.titulo}, Empréstimos: {emprestimos}")
        else:
            print("Nenhum dado de empréstimos disponível.")

    @staticmethod
    def salvar_em_arquivo(arquivo):
        """Salva os livros e registros de empréstimos em um arquivo.

        Args:
            arquivo (str): Caminho do arquivo onde os dados serão salvos.

        Exemplo:
            >>> Livro.salvar_em_arquivo("livros.pkl")
            Dados salvos em livros.pkl.
        """
        with open(arquivo, 'wb') as f:
            pickle.dump(Livro.livros, f)
            pickle.dump(Livro.emprestimos, f)
            print(f"Dados salvos em {arquivo}.")

    @staticmethod
    def carregar_de_arquivo(arquivo):
        """Carrega os livros e registros de empréstimos a partir de um arquivo.

        Args:
            arquivo (str): Caminho do arquivo de onde os dados serão carregados.

        Exemplo:
            >>> Livro.carregar_de_arquivo("livros.pkl")
            Dados carregados de livros.pkl.

        Levanta:
            FileNotFoundError: Se o arquivo não for encontrado.
        """
        try:
            with open(arquivo, 'rb') as f:
                Livro.livros = pickle.load(f)
                Livro.emprestimos = pickle.load(f)
                print(f"Dados carregados de {arquivo}.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            
    @staticmethod
    def procurar(termo):
        """Procura livros pelo título, autor ou ISBN.

        Args:
            termo (str): O termo de busca.

        Exemplo:
            >>> Livro.procurar("A Arte da Programação")
            Resultados encontrados:
            ID: 001, Título: A Arte da Programação, Disponível: Sim
        """
        resultados = [
            livro for livro in Livro.livros.values()
            if termo.lower() in livro.titulo.lower() or
               termo.lower() in livro.autor.lower() or
               termo.lower() in livro.isbn
        ]

        if resultados:
            print("\nResultados encontrados:")
            for livro in resultados:
                print(f"ID: {livro.id_livro}, Título: {livro.titulo}, Disponível: {'Sim' if livro.disponivel else 'Não'}")
        else:
            print(f"Nenhum livro encontrado com o termo '{termo}'.")
