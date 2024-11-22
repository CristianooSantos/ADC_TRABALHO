import pickle
from datetime import datetime

class Funcionario:
    funcionarios = {}  
    atividades = [] 

    def __init__(self, id_funcionario, nome, morada, telefone, nif, email):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.nif = nif
        self.email = email
        self.funcoes = [] 

    def salvar(self):
        Funcionario.funcionarios[self.id_funcionario] = self
        Funcionario.registar_atividade(f"Funcionário {self.id_funcionario} ({self.nome}) adicionado.")
        print(f"Funcionário {self.id_funcionario} adicionado com sucesso.")

    @staticmethod
    def obter(id_funcionario):
        return Funcionario.funcionarios.get(id_funcionario)

    @staticmethod
    def atualizar(id_funcionario, **kwargs):
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
        if id_funcionario in Funcionario.funcionarios:
            del Funcionario.funcionarios[id_funcionario]
            Funcionario.registar_atividade(f"Funcionário {id_funcionario} removido.")
            print(f"Funcionário {id_funcionario} deletado com sucesso.")
        else:
            print("Funcionário não encontrado.")

    @staticmethod
    def listar_todos():
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

    @staticmethod
    def salvar_em_arquivo(arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(Funcionario.funcionarios, f)
            print(f"Funcionários salvos em {arquivo}.")

    @staticmethod
    def carregar_de_arquivo(arquivo):
        try:
            with open(arquivo, 'rb') as f:
                Funcionario.funcionarios = pickle.load(f)
                print(f"Funcionários carregados de {arquivo}.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def atribuir_funcoes(id_funcionario, *funcoes):
        funcionario = Funcionario.obter(id_funcionario)
        if funcionario:
            funcionario.funcoes.extend(funcoes)
            Funcionario.registar_atividade(f"Funções {', '.join(funcoes)} atribuídas ao funcionário {id_funcionario}.")
            print(f"Funções atribuídas com sucesso ao funcionário {id_funcionario}.")
        else:
            print("Funcionário não encontrado.")

    @staticmethod
    def gerar_relatorio_atividades():
        if Funcionario.atividades:
            print("\nRelatório de Atividades:")
            for atividade in Funcionario.atividades:
                print(atividade)
        else:
            print("Nenhuma atividade registada.")

    @staticmethod
    def registar_atividade(descricao):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Funcionario.atividades.append(f"[{timestamp}] {descricao}")
