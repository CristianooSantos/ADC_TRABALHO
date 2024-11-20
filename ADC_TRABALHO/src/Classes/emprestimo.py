from datetime import datetime, timedelta

class Emprestimo:
    emprestimos = {}  
    contador_emprestimos = 1

    def __init__(self, isbn_livro, numero_leitor, id_funcionario, data_emprestimo=None, data_devolucao=None):
        self.id_emprestimo = Emprestimo.contador_emprestimos
        self.isbn_livro = isbn_livro
        self.numero_leitor = numero_leitor
        self.id_funcionario = id_funcionario
        self.data_emprestimo = data_emprestimo or datetime.now().date()
        self.data_devolucao = data_devolucao or self.data_emprestimo + timedelta(days=14)

        Emprestimo.contador_emprestimos += 1

    def salvar(self):
        Emprestimo.emprestimos[self.id_emprestimo] = self
        print(f"Empréstimo {self.id_emprestimo} adicionado com sucesso.")

    @staticmethod
    def obter(id_emprestimo):
        return Emprestimo.emprestimos.get(id_emprestimo)

    @staticmethod
    def deletar(id_emprestimo):
        if id_emprestimo in Emprestimo.emprestimos:
            del Emprestimo.emprestimos[id_emprestimo]
            print(f"Empréstimo {id_emprestimo} deletado com sucesso.")
        else:
            print("Empréstimo não encontrado.")

    @staticmethod
    def listar_todos():
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
