class Leitor:
    leitores = {}  

    def __init__(self, numero_leitor, nome, morada, telefone, nif, email):
        self.numero_leitor = numero_leitor
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.nif = nif
        self.email = email

    def salvar(self):
        Leitor.leitores[self.numero_leitor] = self
        print(f"Leitor {self.numero_leitor} adicionado com sucesso.")

    @staticmethod
    def obter(numero_leitor):
        return Leitor.leitores.get(numero_leitor)

    @staticmethod
    def atualizar(numero_leitor, **kwargs):
        leitor = Leitor.obter(numero_leitor)
        if leitor:
            for chave, valor in kwargs.items():
                setattr(leitor, chave, valor)
            print(f"Leitor {numero_leitor} atualizado com sucesso.")
        else:
            print("Leitor não encontrado.")

    @staticmethod
    def deletar(numero_leitor):
        if numero_leitor in Leitor.leitores:
            del Leitor.leitores[numero_leitor]
            print(f"Leitor {numero_leitor} deletado com sucesso.")
        else:
            print("Leitor não encontrado.")
