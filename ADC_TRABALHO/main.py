from Classes.livro import Livro

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
            break
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
            
if __name__ == "__main__":
    menu_principal()


