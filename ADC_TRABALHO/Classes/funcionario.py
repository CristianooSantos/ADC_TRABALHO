class Funcionario:
    funcionarios = {} 

    def __init__(self, id_funcionario, nome, morada, telefone, nif, email):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.nif = nif
        self.email = email

    def salvar(self):
        Funcionario.funcionarios[self.id_funcionario] = self
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
            print(f"Funcionário {id_funcionario} atualizado com sucesso.")
        else:
            print("Funcionário não encontrado.")

    @staticmethod
    def deletar(id_funcionario):
        if id_funcionario in Funcionario.funcionarios:
            del Funcionario.funcionarios[id_funcionario]
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
                print("-" * 30) 
