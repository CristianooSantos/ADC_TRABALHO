from livro import Livro
from funcionario import Funcionario
from emprestimo import Emprestimo
from leitor import Leitor
from datetime import datetime

def menu_principal():
    while True:
        print("\nSistema de Gestão da Biblioteca")
        print("1. Gerir Leitores")
        print("2. Gerir Livros")
        print("3. Gerir Funcionários")
        print("4. Gerir Empréstimos")
        print("5. Gerar Relatório Mensal")
        print("6. Carregar Dados de Arquivo")
        print("7. Salvar Dados em Arquivo")
        print("8. Sair")

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
            gerar_relatorio_mensal()
        elif opcao == "6":
            carregar_dados()
        elif opcao == "7":
            salvar_dados()
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def carregar_dados():
    try:
        Livro.carregar_de_arquivo("livros.pkl")
        Leitor.carregar_de_arquivo("leitores.pkl")
        Funcionario.carregar_de_arquivo("funcionarios.pkl")
        Emprestimo.carregar_de_arquivo("emprestimos.pkl")
        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def salvar_dados():
    try:
        Livro.salvar_em_arquivo("livros.pkl")
        Leitor.salvar_em_arquivo("leitores.pkl")
        Funcionario.salvar_em_arquivo("funcionarios.pkl")
        Emprestimo.salvar_em_arquivo("emprestimos.pkl")
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

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
        print("6. Atribuir Funções a Funcionário")
        print("7. Gerar Relatório de Atividades")
        print("8. Voltar ao Menu Principal")

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
                print(f"ID: {funcionario.id_funcionario}")
                print(f"Nome: {funcionario.nome}")
                print(f"Morada: {funcionario.morada}")
                print(f"Telefone: {funcionario.telefone}")
                print(f"NIF: {funcionario.nif}")
                print(f"Email: {funcionario.email}")
                print(f"Funções: {', '.join(funcionario.funcoes) if funcionario.funcoes else 'Nenhuma'}")
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
            id_funcionario = input("ID do Funcionário: ")
            funcionario = Funcionario.obter(id_funcionario)
            if funcionario:
                funcoes = input("Insira as funções separadas por vírgulas: ").split(",")
                funcoes = [funcao.strip() for funcao in funcoes]
                Funcionario.atribuir_funcoes(id_funcionario, *funcoes)
            else:
                print("Funcionário não encontrado.")

        elif opcao == "7":
            Funcionario.gerar_relatorio_atividades()

        elif opcao == "8":
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
            Emprestimo.listar_todos()

        elif opcao == "5":
            break

        else:
            print("Opção inválida! Tente novamente.")

def gerar_relatorio_mensal():
    """
    Gera e exibe um relatório mensal com informações sobre livros, leitores e empréstimos registrados.

    O relatório inclui as seguintes informações:
    - Total de livros cadastrados no sistema.
    - Total de leitores cadastrados no sistema.
    - Total de empréstimos realizados no mês atual.
    - Total de livros devolvidos no mês atual.
    - Número de leitores únicos ativos no mês.
    - Livro mais popular (título e ID) com base no número de empréstimos.

    Args:
        Nenhum

    Returns:
        None: A função apenas exibe os dados processados no console.

    Raises:
        Nenhum

    Exemplo de saída:
        Relatório Mensal:
        Total de Livros Cadastrados: 10
        Total de Leitores Cadastrados: 15
        Total de Empréstimos no Mês: 7
        Livros Devolvidos no Mês: 5
        Leitores Ativos no Mês: 6
        Livro Mais Popular no Mês: "O Alquimista" (ID: 3)
    """
    hoje = datetime.now().date()  
    inicio_mes = hoje.replace(day=1)  

    emprestimos_mes = [
        e for e in Emprestimo.emprestimos.values()
        if e.data_emprestimo >= inicio_mes  
    ]
    total_emprestimos = len(emprestimos_mes)
    livros_devolvidos = sum(1 for e in emprestimos_mes if e.data_devolucao <= hoje)
    leitores_ativos = len(set(e.numero_leitor for e in emprestimos_mes))

    livro_popular_id = None
    livro_popular_titulo = None

    if emprestimos_mes:
        livros_contagem = {}
        for e in emprestimos_mes:
            livros_contagem[e.isbn_livro] = livros_contagem.get(e.isbn_livro, 0) + 1
        livro_popular_id = max(livros_contagem, key=livros_contagem.get)
        livro_popular = Livro.obter(livro_popular_id)
        if livro_popular:
            livro_popular_titulo = livro_popular.titulo

    total_livros = len(Livro.livros)
    total_leitores = len(Leitor.leitores)

    print("\nRelatório Mensal:")
    print(f"Total de Livros Cadastrados: {total_livros}")
    print(f"Total de Leitores Cadastrados: {total_leitores}")
    print(f"Total de Empréstimos no Mês: {total_emprestimos}")
    print(f"Livros Devolvidos no Mês: {livros_devolvidos}")
    print(f"Leitores Ativos no Mês: {leitores_ativos}")
    if livro_popular_titulo and livro_popular_id:
        print(f"Livro Mais Popular no Mês: {livro_popular_titulo} (ID: {livro_popular_id})")
    else:
        print("Livro Mais Popular no Mês: Nenhum")



if __name__ == "__main__":
    menu_principal()
