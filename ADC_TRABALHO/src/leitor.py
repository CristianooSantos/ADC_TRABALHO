"""
Leitor
======

Este módulo contém a classe `Leitor`, que representa os leitores de uma biblioteca e oferece métodos para gerenciar
seus dados, como salvar, atualizar, deletar e listar.

"""
import pickle
class Leitor:
    """Classe para gerenciar os leitores de uma biblioteca.

    Attributes:
        leitores (dict): Dicionário estático contendo todos os leitores cadastrados.
    """
    leitores = {}  

    def __init__(self, numero_leitor, nome, morada, telefone, nif, email):
        """Inicializa um leitor com os dados fornecidos.

        Args:
            numero_leitor (str): Número de identificação único do leitor.
            nome (str): Nome do leitor.
            morada (str): Endereço do leitor.
            telefone (str): Número de telefone do leitor.
            nif (str): Número de identificação fiscal do leitor.
            email (str): Endereço de e-mail do leitor.
        """
        self.numero_leitor = numero_leitor
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.nif = nif
        self.email = email

    def salvar(self):
        """Salva o leitor no dicionário estático `Leitor.leitores`.

        Raises:
            KeyError: Se o número do leitor já existir.

        Example:
            >>> leitor = Leitor("001", "João Silva", "Rua A", "123456789", "123456789", "joao@email.com")
            >>> leitor.salvar()
            Leitor 001 adicionado com sucesso.
        """
        if self.numero_leitor in Leitor.leitores:
            raise KeyError(f"O número do leitor {self.numero_leitor} já existe.")
        Leitor.leitores[self.numero_leitor] = self
        print(f"Leitor {self.numero_leitor} adicionado com sucesso.")

    @staticmethod
    def obter(numero_leitor):
        """Busca um leitor pelo número.

        Args:
            numero_leitor (str): Número do leitor a ser buscado.

        Returns:
            Leitor: O leitor encontrado, ou None se não encontrado.

        Example:
            >>> Leitor.obter("001")
            <Leitor object>
        """
        return Leitor.leitores.get(numero_leitor)

    @staticmethod
    def atualizar(numero_leitor, **kwargs):
        """Atualiza as informações de um leitor existente.

        Args:
            numero_leitor (str): Número do leitor a ser atualizado.
            **kwargs: Atributos do leitor que precisam ser atualizados.

        Raises:
            KeyError: Se o leitor não for encontrado.

        Example:
            >>> Leitor.atualizar("001", nome="João Pereira")
            Leitor 001 atualizado com sucesso.
        """
        leitor = Leitor.obter(numero_leitor)
        if not leitor:
            raise KeyError(f"Leitor {numero_leitor} não encontrado.")
        for chave, valor in kwargs.items():
            setattr(leitor, chave, valor)
        print(f"Leitor {numero_leitor} atualizado com sucesso.")

    @staticmethod
    def deletar(numero_leitor):
        """Remove um leitor do sistema.

        Args:
            numero_leitor (str): Número do leitor a ser removido.

        Raises:
            KeyError: Se o leitor não for encontrado.

        Example:
            >>> Leitor.deletar("001")
            Leitor 001 deletado com sucesso.
        """
        if numero_leitor not in Leitor.leitores:
            raise KeyError(f"Leitor {numero_leitor} não encontrado.")
        del Leitor.leitores[numero_leitor]
        print(f"Leitor {numero_leitor} deletado com sucesso.")

    @staticmethod
    def listar_todos():
        """Lista todos os leitores cadastrados.

        Example:
            >>> Leitor.listar_todos()
            Número do Leitor: 001
            Nome: João Silva
            Morada: Rua A
            Telefone: 123456789
            NIF: 123456789
            Email: joao@email.com
        """
        if not Leitor.leitores:
            print("Nenhum leitor cadastrado.")
            return
        print("\nLista de Leitores:")
        for leitor in Leitor.leitores.values():
            print(f"\nNúmero do Leitor: {leitor.numero_leitor}")
            print(f"Nome: {leitor.nome}")
            print(f"Morada: {leitor.morada}")
            print(f"Telefone: {leitor.telefone}")
            print(f"NIF: {leitor.nif}")
            print(f"Email: {leitor.email}")
            print("-" * 30)

    @staticmethod
    def salvar_em_arquivo(arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(Leitor.leitores, f)
            print(f"Leitores salvos em {arquivo}.")

    @staticmethod
    def carregar_de_arquivo(arquivo):
        try:
            with open(arquivo, 'rb') as f:
                Leitor.leitores = pickle.load(f)
                print(f"Leitores carregados de {arquivo}.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")