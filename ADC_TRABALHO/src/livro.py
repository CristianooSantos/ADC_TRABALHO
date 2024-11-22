import pickle

class Livro:
    livros = {}
    emprestimos = {}

    def __init__(self, id_livro, titulo, autor, categoria, isbn, ano_publicacao):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def salvar(self):
        Livro.livros[self.id_livro] = self
        Livro.emprestimos[self.id_livro] = 0
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
            del Livro.emprestimos[id_livro]
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
                print(f"Disponível: {'Sim' if livro.disponivel else 'Não'}")
                print("-" * 30)
        else:
            print("Nenhum livro cadastrado.")

    @staticmethod
    def filtrar_por_categoria(categoria):
        encontrados = [livro for livro in Livro.livros.values() if livro.categoria.lower() == categoria.lower()]
        if encontrados:
            print(f"\nLivros na categoria '{categoria}':")
            for livro in encontrados:
                print(f"ID: {livro.id_livro}, Título: {livro.titulo}, Disponível: {'Sim' if livro.disponivel else 'Não'}")
        else:
            print(f"Nenhum livro encontrado na categoria '{categoria}'.")

    @staticmethod
    def verificar_disponibilidade(id_livro):
        livro = Livro.obter(id_livro)
        if livro:
            estado = "disponível" if livro.disponivel else "indisponível"
            print(f"O livro '{livro.titulo}' está {estado}.")
        else:
            print("Livro não encontrado.")

    @staticmethod
    def emprestar(id_livro):
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
        with open(arquivo, 'wb') as f:
            pickle.dump({'livros': Livro.livros, 'emprestimos': Livro.emprestimos}, f)
            print(f"Dados salvos em {arquivo}.")

    @staticmethod
    def carregar_de_arquivo(arquivo):
        try:
            with open(arquivo, 'rb') as f:
                dados = pickle.load(f)
                Livro.livros = dados['livros']
                Livro.emprestimos = dados['emprestimos']
                print(f"Dados carregados de {arquivo}.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
