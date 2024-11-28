import pickle
from datetime import datetime

class Funcionario:
    """
    Classe para representar e gerir os dados de funcionários.
    
    Atributos:
    -----------
    funcionarios : dict
        Dicionário para armazenar os funcionários com seus respetivos IDs como chaves.
    atividades : list
        Lista para registar todas as atividades realizadas no sistema.

    Métodos:
    --------
    __init__(self, id_funcionario, nome, morada, telefone, nif, email):
        Construtor da classe para inicializar um novo funcionário.
    salvar(self):
        Salva o funcionário atual no dicionário de funcionários e regista a atividade.
    obter(id_funcionario):
        Obtém os dados de um funcionário pelo ID.
    atualizar(id_funcionario, **kwargs):
        Atualiza os dados de um funcionário específico.
    deletar(id_funcionario):
        Remove um funcionário do sistema pelo ID.
    listar_todos():
        Lista todos os funcionários armazenados.
    salvar_em_arquivo(arquivo):
        Salva os funcionários num ficheiro binário.
    carregar_de_arquivo(arquivo):
        Carrega os funcionários de um ficheiro binário.
    atribuir_funcoes(id_funcionario, *funcoes):
        Atribui funções a um funcionário específico.
    gerar_relatorio_atividades():
        Gera e exibe um relatório de todas as atividades registadas.
    registar_atividade(descricao):
        Regista uma nova atividade no sistema com um timestamp.
    """

    funcionarios = {}  # Armazena os funcionários criados no sistema
    atividades = []  # Regista as atividades realizadas no sistema

    def __init__(self, id_funcionario, nome, morada, telefone, nif, email):
        """
        Inicializa um novo objeto Funcionario.

        Parâmetros:
        -----------
        id_funcionario : str
            Identificador único do funcionário.
        nome : str
            Nome completo do funcionário.
        morada : str
            Endereço residencial do funcionário.
        telefone : str
            Número de telefone do funcionário.
        nif : str
            Número de Identificação Fiscal do funcionário.
        email : str
            Endereço de email do funcionário.
        """
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.nif = nif
        self.email = email
        self.funcoes = []  # Lista de funções atribuídas ao funcionário

    def salvar(self):
        """
        Salva o funcionário no dicionário de funcionários e regista a atividade.
        """
        Funcionario.funcionarios[self.id_funcionario] = self
        Funcionario.registar_atividade(f"Funcionário {self.id_funcionario} ({self.nome}) adicionado.")
        print(f"Funcionário {self.id_funcionario} adicionado com sucesso.")

    @staticmethod
    def obter(id_funcionario):
        """
        Obtém os dados de um funcionário pelo ID.

        Parâmetros:
        -----------
        id_funcionario : str
            Identificador do funcionário a ser obtido.

        Retorna:
        --------
        Funcionario
            Objeto do funcionário correspondente ou None se não existir.
        """
        return Funcionario.funcionarios.get(id_funcionario)

    @staticmethod
    def atualizar(id_funcionario, **kwargs):
        """
        Atualiza os dados de um funcionário.

        Parâmetros:
        -----------
        id_funcionario : str
            Identificador do funcionário a ser atualizado.
        **kwargs : dict
            Dados a serem atualizados no funcionário.
        """
        funcionario = Funcionario.obter(id_funcionario)
        if funcionario:
            for chave, valor in kwargs.items():
                setattr(funcionario, chave, valor)
            Funcionario.registar_atividade(f"Funcionário {id_funcionario} atualizado com novos dados: {kwargs}.")
            print(f"Funcionário {id_funcionario} atualizado com sucesso.")
        else:
            print("Funcionário não encontrado.")

    @staticmethod
    def deletar(id_funcionario):
        """
        Remove um funcionário pelo ID.

        Parâmetros:
        -----------
        id_funcionario : str
            Identificador do funcionário a ser removido.
        """
        if id_funcionario in Funcionario.funcionarios:
            del Funcionario.funcionarios[id_funcionario]
            Funcionario.registar_atividade(f"Funcionário {id_funcionario} removido.")
            print(f"Funcionário {id_funcionario} deletado com sucesso.")
        else:
            print("Funcionário não encontrado.")

    @staticmethod
    def listar_todos():
        """
        Lista todos os funcionários no sistema.
        """
        if Funcionario.funcionarios:
            print("\nLista de Funcionários:")
            for funcionario in Funcionario.funcionarios.values():
                print(f"\nID: {funcionario.id_funcionario}")
                print(f"Nome: {funcionario.nome}")
                print(f"Morada: {funcionario.morada}")
                print(f"Telefone: {funcionario.telefone}")
                print(f"NIF: {funcionario.nif}")
                print(f"Email: {funcionario.email}")
                print(f"Funções: {', '.join(funcionario.funcoes) if funcionario.funcoes else 'Nenhuma'}")
                print("-" * 30)
        else:
            print("Nenhum funcionário registado.")

    @staticmethod
    def salvar_em_arquivo(arquivo):
        """
        Salva todos os funcionários num ficheiro binário.

        Parâmetros:
        -----------
        arquivo : str
            Nome do ficheiro onde os dados serão armazenados.
        """
        with open(arquivo, 'wb') as f:
            pickle.dump(Funcionario.funcionarios, f)
            print(f"Funcionários salvos em {arquivo}.")

    @staticmethod
    def carregar_de_arquivo(arquivo):
        """
        Carrega funcionários de um ficheiro binário.

        Parâmetros:
        -----------
        arquivo : str
            Nome do ficheiro a ser lido.
        """
        try:
            with open(arquivo, 'rb') as f:
                Funcionario.funcionarios = pickle.load(f)
                print(f"Funcionários carregados de {arquivo}.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def atribuir_funcoes(id_funcionario, *funcoes):
        """
        Atribui funções a um funcionário.

        Parâmetros:
        -----------
        id_funcionario : str
            Identificador do funcionário.
        *funcoes : tuple
            Lista de funções a serem atribuídas.
        """
        funcionario = Funcionario.obter(id_funcionario)
        if funcionario:
            funcionario.funcoes.extend(funcoes)
            Funcionario.registar_atividade(f"Funções {', '.join(funcoes)} atribuídas ao funcionário {id_funcionario}.")
            print(f"Funções atribuídas com sucesso ao funcionário {id_funcionario}.")
        else:
            print("Funcionário não encontrado.")

    @staticmethod
    def gerar_relatorio_atividades():
        """
        Gera e exibe um relatório de atividades realizadas.
        """
        if Funcionario.atividades:
            print("\nRelatório de Atividades:")
            for atividade in Funcionario.atividades:
                print(atividade)
        else:
            print("Nenhuma atividade registada.")

    @staticmethod
    def registar_atividade(descricao):
        """
        Regista uma nova atividade com timestamp.

        Parâmetros:
        -----------
        descricao : str
            Descrição da atividade realizada.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Funcionario.atividades.append(f"[{timestamp}] {descricao}")
