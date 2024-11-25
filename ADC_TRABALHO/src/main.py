"""
Sistema de Gestão de Biblioteca
===============================

Este módulo principal implementa um sistema para gerenciar livros, leitores, funcionários e empréstimos em uma biblioteca.
Ele permite criar, atualizar, listar e deletar dados de várias entidades, além de gerenciar empréstimos e gerar relatórios.

Módulos e Classes Utilizadas:
-----------------------------
- Livro: Gerencia livros na biblioteca.
- Leitor: Gerencia leitores da biblioteca.
- Funcionario: Gerencia funcionários da biblioteca.
- Emprestimo: Gerencia empréstimos realizados.
- datetime: Para lidar com datas e horários.

Funções Principais:
-------------------
- criar_dados_teste(): Cria dados fictícios para teste.
- menu_principal(): Gerencia o fluxo principal do programa e exibe as opções do menu.
- carregar_dados(): Carrega os dados das entidades a partir de arquivos serializados.
- salvar_dados(): Salva os dados das entidades em arquivos serializados.
- menu_leitores(): Gerencia operações relacionadas aos leitores.
- menu_livros(): Gerencia operações relacionadas aos livros.
- menu_funcionarios(): Gerencia operações relacionadas aos funcionários.
- menu_emprestimos(): Gerencia operações relacionadas aos empréstimos.
- gerar_relatorio_mensal(): Gera um relatório mensal sobre as atividades da biblioteca.

Execução:
---------
Este módulo deve ser executado diretamente. O menu principal será iniciado e o usuário poderá interagir com as opções.

Exemplo de Uso:
---------------
$ python main.py
"""


from livro import Livro
from funcionario import Funcionario
from emprestimo import Emprestimo
from leitor import Leitor
from datetime import datetime

def criar_dados_teste():
    """
    Popula as entidades com dados fictícios para testes.

    Exemplo:
        >>> criar_dados_teste()
        Dados de teste criados com sucesso!
    """
   
    Livro("1", "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", "978-0-1234-5678-9", 1954).salvar()
    Livro("2", "1984", "George Orwell", "Distopia", "978-0-9876-5432-1", 1949).salvar()
    Livro("3", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Ficção", "978-0-1111-2222-3", 1943).salvar()

    
    Leitor("1", "João Silva", "Rua A, 123", "912345678", "123456789", "joao@email.com").salvar()
    Leitor("2", "Maria Oliveira", "Rua B, 456", "987654321", "987654321", "maria@email.com").salvar()

   
    Funcionario("1", "Carlos Pereira", "Rua C, 789", "912112233", "654987321", "carlos@email.com").salvar()
    Funcionario("2", "Ana Santos", "Rua D, 321", "987112233", "456789123", "ana@email.com").salvar()

    
    Emprestimo("978-0-1234-5678-9", "1", "1", data_emprestimo=datetime(2024, 11, 1).date()).salvar()
    Emprestimo("978-0-9876-5432-1", "2", "2", data_emprestimo=datetime(2024, 11, 5).date()).salvar()
    print("Dados de teste criados com sucesso!")

def menu_principal():
    """
    Exibe o menu principal e gerencia o fluxo de operações com base na escolha do usuário.

    Opções do Menu:
        1. Gerir Leitores
        2. Gerir Livros
        3. Gerir Funcionários
        4. Gerir Empréstimos
        5. Gerar Relatório Mensal
        6. Carregar Dados de Arquivo
        7. Salvar Dados em Arquivo
        8. Criar Dados de Teste
        9. Sair

    Exemplo:
        >>> menu_principal()
        Sistema de Gestão da Biblioteca
        Escolha uma opção: 1
    """
    while True:
        print("\nSistema de Gestão da Biblioteca")
        print("1. Gerir Leitores")
        print("2. Gerir Livros")
        print("3. Gerir Funcionários")
        print("4. Gerir Empréstimos")
        print("5. Gerar Relatório Mensal")
        print("6. Carregar Dados de Arquivo")
        print("7. Salvar Dados em Arquivo")
        print("8. Criar Dados de Teste")
        print("9. Sair")

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
            criar_dados_teste()
        elif opcao == "9":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def carregar_dados():
    """
    Carrega dados das entidades Livro, Leitor, Funcionário e Empréstimo a partir de arquivos.

    Exemplo:
        >>> carregar_dados()
        Dados carregados com sucesso!
    """
    try:
        Livro.carregar_de_arquivo("livros.pkl")
        Leitor.carregar_de_arquivo("leitores.pkl")
        Funcionario.carregar_de_arquivo("funcionarios.pkl")
        Emprestimo.carregar_de_arquivo("emprestimos.pkl")
        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def salvar_dados():
    """
    Salva dados das entidades Livro, Leitor, Funcionário e Empréstimo em arquivos.

    Exemplo:
        >>> salvar_dados()
        Dados salvos com sucesso!
    """
    try:
        Livro.salvar_em_arquivo("livros.pkl")
        Leitor.salvar_em_arquivo("leitores.pkl")
        Funcionario.salvar_em_arquivo("funcionarios.pkl")
        Emprestimo.salvar_em_arquivo("emprestimos.pkl")
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def menu_leitores():
    """
    Exibe o menu de gerenciamento de leitores, permitindo ao usuário realizar operações como adicionar,
    consultar, atualizar, deletar e listar leitores.

    Opções do Menu:
        1. Adicionar Leitor
        2. Consultar Leitor por ID
        3. Atualizar Leitor
        4. Deletar Leitor
        5. Listar Todos os Leitores
        6. Voltar ao Menu Principal

    Exemplo:
        >>> menu_leitores()
        Gerenciamento de Leitores
        Escolha uma opção: 1
    """
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
    """
    Exibe o menu de gerenciamento de livros, permitindo ao usuário realizar operações como adicionar,
    consultar, atualizar, deletar e listar livros.

    Opções do Menu:
        1. Adicionar Livro
        2. Consultar Livro por ID
        3. Atualizar Livro
        4. Deletar Livro
        5. Listar Todos os Livros
        6. Voltar ao Menu Principal

    Exemplo:
        >>> menu_livros()
        Gerenciamento de Livros
        Escolha uma opção: 1
    """
    while True:
        print("\nGerenciamento de Livros")
        print("1. Adicionar Livro")
        print("2. Consultar Livro por ID")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Listar Todos os Livros")
        print("6. Procurar Livro por Título, Autor ou ISBN")
        print("7. Verificar Disponibilidade de um Livro")
        print("8. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_livro = input("ID do Livro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")
            ano_publicacao = input("Ano de Publicação: ")
            livro = Livro(id_livro, titulo, autor, categoria, isbn, int(ano_publicacao))
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
                print(f"Disponível: {'Sim' if livro.disponivel else 'Não'}")
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
                Livro.atualizar(id_livro, titulo=titulo, autor=autor, categoria=categoria, isbn=isbn, ano_publicacao=int(ano_publicacao))
            else:
                print("Livro não encontrado.")

        elif opcao == "4":
            id_livro = input("ID do Livro: ")
            Livro.deletar(id_livro)

        elif opcao == "5":
            Livro.listar_todos()

        elif opcao == "6":
            termo = input("Digite o título, autor ou ISBN para buscar: ")
            Livro.procurar(termo)

        elif opcao == "7":
            id_livro = input("ID do Livro: ")
            Livro.verificar_disponibilidade(id_livro)

        elif opcao == "8":
            break

        else:
            print("Opção inválida! Tente novamente.")


def menu_funcionarios():
    """
    Exibe o menu de gerenciamento de funcionários, permitindo ao usuário realizar operações como adicionar,
    consultar, atualizar, deletar e listar funcionários.

    Opções do Menu:
        1. Adicionar Funcionário
        2. Consultar Funcionário por ID
        3. Atualizar Funcionário
        4. Deletar Funcionário
        5. Listar Todos os Funcionários
        6. Voltar ao Menu Principal

    Exemplo:
        >>> menu_funcionarios()
        Gerenciamento de Funcionários
        Escolha uma opção: 1
    """
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
    """
    Exibe o menu de gerenciamento de empréstimos, permitindo ao usuário criar, consultar, deletar e listar empréstimos.

    Opções do Menu:
        1. Criar Empréstimo
        2. Consultar Empréstimo por ID
        3. Deletar Empréstimo
        4. Listar Todos os Empréstimos
        5. Voltar ao Menu Principal

    Exemplo:
        >>> menu_emprestimos()
        Gerenciamento de Empréstimos
        Escolha uma opção: 1
    """
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

            erro = False
            erros = []

            livro = Livro.obter(isbn_livro)
            if not livro:
                erros.append("Erro: Livro não encontrado no sistema.")
                erro = True

            leitor = Leitor.obter(numero_leitor)
            if not leitor:
                erros.append("Erro: Leitor não encontrado no sistema.")
                erro = True

            funcionario = Funcionario.obter(id_funcionario)
            if not funcionario:
                erros.append("Erro: Funcionário não encontrado no sistema.")
                erro = True

            if erro:
                for e in erros:
                    print(e)
                continue

            emprestimo = Emprestimo(isbn_livro, numero_leitor, id_funcionario)
            emprestimo.salvar()
            print("Empréstimo criado com sucesso!")

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

    O relatório é gerado com base no mês atual e considera os empréstimos realizados a partir do primeiro dia do mês.

    Args:
        Nenhum

    Returns:
        None: A função apenas exibe os dados processados no console, sem retornar valores.

    Exceções:
        Nenhuma: Esta função não levanta exceções.

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
