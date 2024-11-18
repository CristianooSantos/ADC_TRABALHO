from Classes.livro import Livro
from Classes.funcionario import Funcionario

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
                print(f"ID: {livro.id_livro}")
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Categoria: {livro.categoria}")
                print(f"ISBN: {livro.isbn}")
                print(f"Ano de Publicação: {livro.ano_publicacao}")
            else:
                print("Livro não encontrado.")

        elif opcao == "3":
            id_livro = input("ID do Livro: ")
            livro = Livro.obter(id_livro)
            if livro:
                print("\nDeixe o campo vazio para manter o valor atual.")
                titulo = input(f"Novo Título ({livro.titulo}): ")
                autor = input(f"Novo Autor ({livro.autor}): ")
                categoria = input(f"Nova Categoria ({livro.categoria}): ")
                isbn = input(f"Novo ISBN ({livro.isbn}): ")
                ano_publicacao = input(f"Novo Ano de Publicação ({livro.ano_publicacao}): ")
                Livro.atualizar(
                    id_livro,
                    titulo=titulo or livro.titulo,
                    autor=autor or livro.autor,
                    categoria=categoria or livro.categoria,
                    isbn=isbn or livro.isbn,
                    ano_publicacao=ano_publicacao or livro.ano_publicacao,
                )
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

if __name__ == "__main__":
    menu_principal()