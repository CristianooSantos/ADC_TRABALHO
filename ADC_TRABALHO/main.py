from Classes.livro import Livro
from Classes.funcionario import Funcionario
from Classes.emprestimo import Emprestimo
from Classes.leitor import Leitor

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
            menu_leitores()
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            menu_funcionarios()
        elif opcao == "4":
            menu_emprestimos()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_leitores():
    while True:
        print("\nGerenciamento de Leitores")
        print("1. Adicionar Leitor")
        print("2. Consultar Leitor por ID")
        print("3. Atualizar Leitor")
        print("4. Deletar Leitor")
        print("5. Listar Todos os Leitores")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_leitor = input("Número do Leitor: ")
            nome = input("Nome: ")
            morada = input("Morada: ")
            telefone = input("Telefone: ")
            nif = input("NIF: ")
            email = input("Email: ")
            leitor = Leitor(numero_leitor, nome, morada, telefone, nif, email)
            leitor.salvar()

        elif opcao == "2":
            numero_leitor = input("Número do Leitor: ")
            leitor = Leitor.obter(numero_leitor)
            if leitor:
                print("\nInformações do Leitor:")
                print(vars(leitor))
            else:
                print("Leitor não encontrado.")

        elif opcao == "3":
            numero_leitor = input("Número do Leitor: ")
            leitor = Leitor.obter(numero_leitor)
            if leitor:
                nome = input(f"Novo Nome ({leitor.nome}): ") or leitor.nome
                morada = input(f"Nova Morada ({leitor.morada}): ") or leitor.morada
                telefone = input(f"Novo Telefone ({leitor.telefone}): ") or leitor.telefone
                nif = input(f"Novo NIF ({leitor.nif}): ") or leitor.nif
                email = input(f"Novo Email ({leitor.email}): ") or leitor.email
                Leitor.atualizar(numero_leitor, nome=nome, morada=morada, telefone=telefone, nif=nif, email=email)
            else:
                print("Leitor não encontrado.")

        elif opcao == "4":
            numero_leitor = input("Número do Leitor: ")
            Leitor.deletar(numero_leitor)

        elif opcao == "5":
            Leitor.listar_todos()

        elif opcao == "6":
            break

        else:
            print("Opção inválida! Tente novamente.")

def menu_livros():
    while True:
        print("\nGerenciamento de Livros")
        print("1. Adicionar Livro")
        print("2. Consultar Livro por ID")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Listar Todos os Livros")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_livro = input("ID do Livro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")
            ano_publicacao = input("Ano de Publicação: ")
            livro = Livro(id_livro, titulo, autor, categoria, isbn, ano_publicacao)
            livro.salvar()

        elif opcao == "2":
            id_livro = input("ID do Livro: ")
            livro = Livro.obter(id_livro)
            if livro:
                print("\nInformações do Livro:")
                print(vars(livro))
            else:
                print("Livro não encontrado.")

        elif opcao == "3":
            id_livro = input("ID do Livro: ")
            livro = Livro.obter(id_livro)
            if livro:
                titulo = input(f"Novo Título ({livro.titulo}): ") or livro.titulo
                autor = input(f"Novo Autor ({livro.autor}): ") or livro.autor
                categoria = input(f"Nova Categoria ({livro.categoria}): ") or livro.categoria
                isbn = input(f"Novo ISBN ({livro.isbn}): ") or livro.isbn
                ano_publicacao = input(f"Novo Ano de Publicação ({livro.ano_publicacao}): ") or livro.ano_publicacao
                Livro.atualizar(id_livro, titulo=titulo, autor=autor, categoria=categoria, isbn=isbn, ano_publicacao=ano_publicacao)
            else:
                print("Livro não encontrado.")

        elif opcao == "4":
            id_livro = input("ID do Livro: ")
            Livro.deletar(id_livro)

        elif opcao == "5":
            Livro.listar_todos()

        elif opcao == "6":
            break

        else:
            print("Opção inválida! Tente novamente.")

def menu_funcionarios():
    while True:
        print("\nGerenciamento de Funcionários")
        print("1. Adicionar Funcionário")
        print("2. Consultar Funcionário por ID")
        print("3. Atualizar Funcionário")
        print("4. Deletar Funcionário")
        print("5. Listar Todos os Funcionários")
        print("6. Voltar ao Menu Principal")

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
            id_funcionario = input("ID do Funcionário: ")
            funcionario = Funcionario.obter(id_funcionario)
            if funcionario:
                print("\nInformações do Funcionário:")
                print(vars(funcionario))
            else:
                print("Funcionário não encontrado.")

        elif opcao == "3":
            id_funcionario = input("ID do Funcionário: ")
            funcionario = Funcionario.obter(id_funcionario)
            if funcionario:
                nome = input(f"Novo Nome ({funcionario.nome}): ") or funcionario.nome
                morada = input(f"Nova Morada ({funcionario.morada}): ") or funcionario.morada
                telefone = input(f"Novo Telefone ({funcionario.telefone}): ") or funcionario.telefone
                nif = input(f"Novo NIF ({funcionario.nif}): ") or funcionario.nif
                email = input(f"Novo Email ({funcionario.email}): ") or funcionario.email
                Funcionario.atualizar(id_funcionario, nome=nome, morada=morada, telefone=telefone, nif=nif, email=email)
            else:
                print("Funcionário não encontrado.")

        elif opcao == "4":
            id_funcionario = input("ID do Funcionário: ")
            Funcionario.deletar(id_funcionario)

        elif opcao == "5":
            Funcionario.listar_todos()

        elif opcao == "6":
            break

        else:
            print("Opção inválida! Tente novamente.")

def menu_emprestimos():
    while True:
        print("\nGerenciamento de Empréstimos")
        print("1. Criar Empréstimo")
        print("2. Consultar Empréstimo por ID")
        print("3. Deletar Empréstimo")
        print("4. Listar Todos os Empréstimos")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            isbn_livro = input("ISBN do Livro: ")
            numero_leitor = input("Número do Leitor: ")
            id_funcionario = input("ID do Funcionário: ")
            emprestimo = Emprestimo(isbn_livro, numero_leitor, id_funcionario)
            emprestimo.salvar()

        elif opcao == "2":
            id_emprestimo = input("ID do Empréstimo: ")
            emprestimo = Emprestimo.obter(id_emprestimo)
            if emprestimo:
                print("\nInformações do Empréstimo:")
                print(vars(emprestimo))
            else:
                print("Empréstimo não encontrado.")

        elif opcao == "3":
            id_emprestimo = input("ID do Empréstimo: ")
            Emprestimo.deletar(id_emprestimo)

        elif opcao == "4":
            emprestimos = Emprestimo.listar_todos()
            if emprestimos:
                print("\nLista de Empréstimos:")
                for emp in emprestimos:
                    print(vars(emp))

        elif opcao == "5":
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()
