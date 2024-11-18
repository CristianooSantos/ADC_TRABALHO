from Classes.livro import Livro
from Classes.funcionario import Funcionario
from Classes.emprestimo import Emprestimo
def menu_principal():
    while True:
        print("\nSistema de Gestão da Biblioteca")
        print("1. Gerir Leitores")
        print("2. Gerir Livros")
        print("3. Gerir Funcionários")
        print("4. Gerir Empréstimos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            break
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            menu_funcionarios()
        elif opcao == "4":
            break
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_livros():
    while True:
        print("\nGerenciamento de Livros")
        print("1. Adicionar Livro")
        print("2. Consultar Livro")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            ano_publicacao = input("Ano de Publicação: ")
            livro = Livro(isbn, titulo, autor, categoria, ano_publicacao)
            livro.salvar()

        elif opcao == "2":
            isbn = input("ISBN: ")
            livro = Livro.obter(isbn)
            if livro:
                print(vars(livro))
            else:
                print("Livro não encontrado.")

        elif opcao == "3":
            isbn = input("ISBN: ")
            livro = Livro.obter(isbn)
            if livro:
                titulo = input("Novo Título: ")
                autor = input("Novo Autor: ")
                categoria = input("Nova Categoria: ")
                ano_publicacao = input("Novo Ano de Publicação: ")
                Livro.atualizar(isbn, titulo=titulo or livro.titulo, autor=autor, categoria=categoria, ano_publicacao=ano_publicacao)
            else:
                print("Livro não encontrado.")

        elif opcao == "4":
            isbn = input("ISBN: ")
            Livro.deletar(isbn)

        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")
            
def menu_funcionarios():
    while True:
        print("\nGerenciamento de Funcionários")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Deletar Funcionário")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_funcionario = input("ID do Funcionário: ")
            nome = input("Nome: ")
            morada = input("Morada: ")
            telefone = input("Telefone: ")
            nif = input("NIF: ")
            email = input("Email: ")
            funcionario = Funcionario(id_funcionario, nome, morada, telefone, nif, email)
            funcionario.salvar()

        elif opcao == "2":
            funcionarios = Funcionario.listar_todos()
            if funcionarios:
                for func in funcionarios:
                    print(vars(func))

        elif opcao == "3":
            id_funcionario = input("ID do Funcionário: ")
            funcionario = Funcionario.obter(id_funcionario)
            if funcionario:
                nome = input("Novo Nome: ")
                morada = input("Nova Morada: ")
                telefone = input("Novo Telefone: ")
                nif = input("Novo NIF: ")
                email = input("Novo Email: ")
                Funcionario.atualizar(id_funcionario, nome=nome or funcionario.nome, morada=morada, telefone=telefone, nif=nif, email=email)
            else:
                print("Funcionário não encontrado.")

        elif opcao == "4":
            id_funcionario = input("ID do Funcionário: ")
            Funcionario.deletar(id_funcionario)

        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_emprestimos():
    while True:
        print("\nGerenciamento de Empréstimos")
        print("1. Criar Empréstimo")
        print("2. Consultar Empréstimo")
        print("3. Deletar Empréstimo")
        print("4. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            isbn_livro = input("ISBN do Livro: ")
            numero_leitor = input("Número do Leitor: ")
            id_funcionario = input("ID do Funcionário: ")
            emprestimo = Emprestimo(isbn_livro, numero_leitor, id_funcionario)
            emprestimo.salvar()
            enviar_notificacao(numero_leitor, "Seu livro foi emprestado com sucesso!")

        elif opcao == "2":
            id_emprestimo = int(input("ID do Empréstimo: "))
            emprestimo = Emprestimo.obter(id_emprestimo)
            if emprestimo:
                print(vars(emprestimo))
            else:
                print("Empréstimo não encontrado.")

        elif opcao == "3":
            id_emprestimo = int(input("ID do Empréstimo: "))
            Emprestimo.deletar(id_emprestimo)

        elif opcao == "4":
            break
        else:
            print("Opção inválida! Tente novamente.")
            
if __name__ == "__main__":
    menu_principal()