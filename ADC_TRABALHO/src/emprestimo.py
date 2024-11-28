from datetime import datetime, timedelta
import pickle

class Emprestimo:
    """
    Classe para representar e gerir os empréstimos de livros.

    Atributos:
    -----------
    emprestimos : dict
        Dicionário para armazenar os empréstimos com seus respetivos IDs como chaves.
    contador_emprestimos : int
        Contador sequencial para gerar IDs únicos para os empréstimos.

    Métodos:
    --------
    __init__(self, isbn_livro, numero_leitor, id_funcionario, data_emprestimo=None, data_devolucao=None):
        Construtor da classe para inicializar um novo empréstimo.
    salvar(self):
        Salva o empréstimo atual no dicionário de empréstimos.
    obter(id_emprestimo):
        Obtém os dados de um empréstimo pelo ID.
    deletar(id_emprestimo):
        Remove um empréstimo do sistema pelo ID.
    listar_todos():
        Lista todos os empréstimos armazenados.
    salvar_em_arquivo(arquivo):
        Salva os empréstimos num ficheiro binário.
    carregar_de_arquivo(arquivo):
        Carrega os empréstimos de um ficheiro binário.
    """

    emprestimos = {}  # Armazena os empréstimos criados no sistema
    contador_emprestimos = 1  # Contador sequencial para atribuir IDs únicos

    def __init__(self, isbn_livro, numero_leitor, id_funcionario, data_emprestimo=None, data_devolucao=None):
        """
        Inicializa um novo objeto Emprestimo.

        Parâmetros:
        -----------
        isbn_livro : str
            ISBN do livro emprestado.
        numero_leitor : str
            Número identificador do leitor que realizou o empréstimo.
        id_funcionario : str
            Identificador do funcionário responsável pelo empréstimo.
        data_emprestimo : datetime.date, opcional
            Data do empréstimo. Padrão é a data atual.
        data_devolucao : datetime.date, opcional
            Data prevista para devolução. Padrão é 14 dias após a data do empréstimo.
        """
        self.id_emprestimo = Emprestimo.contador_emprestimos
        self.isbn_livro = isbn_livro
        self.numero_leitor = numero_leitor
        self.id_funcionario = id_funcionario
        self.data_emprestimo = data_emprestimo or datetime.now().date()
        self.data_devolucao = data_devolucao or self.data_emprestimo + timedelta(days=14)

        Emprestimo.contador_emprestimos += 1

    def salvar(self):
        """
        Salva o empréstimo no dicionário de empréstimos.
        """
        Emprestimo.emprestimos[self.id_emprestimo] = self
        print(f"Empréstimo {self.id_emprestimo} adicionado com sucesso.")

    @staticmethod
    def obter(id_emprestimo):
        """
        Obtém os dados de um empréstimo pelo ID.

        Parâmetros:
        -----------
        id_emprestimo : int
            Identificador do empréstimo a ser obtido.

        Retorna:
        --------
        Emprestimo
            Objeto do empréstimo correspondente ou None se não existir.
        """
        return Emprestimo.emprestimos.get(id_emprestimo)

    @staticmethod
    def deletar(id_emprestimo):
        """
        Remove um empréstimo pelo ID.

        Parâmetros:
        -----------
        id_emprestimo : int
            Identificador do empréstimo a ser removido.
        """
        if id_emprestimo in Emprestimo.emprestimos:
            del Emprestimo.emprestimos[id_emprestimo]
            print(f"Empréstimo {id_emprestimo} deletado com sucesso.")
        else:
            print("Empréstimo não encontrado.")

    @staticmethod
    def listar_todos():
        """
        Lista todos os empréstimos no sistema.
        """
        if Emprestimo.emprestimos:
            print("\nLista de Empréstimos:")
            for emprestimo in Emprestimo.emprestimos.values():
                print(f"\nID Empréstimo: {emprestimo.id_emprestimo}")
                print(f"ISBN Livro: {emprestimo.isbn_livro}")
                print(f"Número do Leitor: {emprestimo.numero_leitor}")
                print(f"ID Funcionário: {emprestimo.id_funcionario}")
                print(f"Data do Empréstimo: {emprestimo.data_emprestimo}")
                print(f"Data de Devolução: {emprestimo.data_devolucao}")
                print("-" * 30)
        else:
            print("Nenhum empréstimo cadastrado.")

    @staticmethod
    def salvar_em_arquivo(arquivo):
        """
        Salva todos os empréstimos num ficheiro binário.

        Parâmetros:
        -----------
        arquivo : str
            Nome do ficheiro onde os dados serão armazenados.
        """
        with open(arquivo, 'wb') as f:
            pickle.dump(Emprestimo.emprestimos, f)
            print(f"Empréstimos salvos em {arquivo}.")

    @staticmethod
    def carregar_de_arquivo(arquivo):
        """
        Carrega empréstimos de um ficheiro binário.

        Parâmetros:
        -----------
        arquivo : str
            Nome do ficheiro a ser lido.
        """
        try:
            with open(arquivo, 'rb') as f:
                Emprestimo.emprestimos = pickle.load(f)
                print(f"Empréstimos carregados de {arquivo}.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
