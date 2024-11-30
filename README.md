# Instalação

1. Clone este repositório:  
   ```bash
   git clone https://github.com/CristianooSantos/ADC_TRABALHO.git
   cd ADC_TRABALHO
   ```

2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

---

# Sistema de Gestão de Biblioteca

Este é um sistema de gestão de biblioteca desenvolvido em **Python**, projetado para gerenciar livros, leitores, funcionários e empréstimos. Ele inclui funcionalidades como **CRUD** (criação, leitura, atualização e exclusão) de registros, notificações de prazos, relatórios e persistência de dados.

---

## Funcionalidades

### **Gestão de Livros**  
- Adicionar, listar, atualizar e remover livros da biblioteca.

### **Gestão de Leitores**  
- Cadastrar, atualizar, listar e excluir leitores registrados.

### **Gestão de Funcionários**  
- Gerenciar informações dos funcionários da biblioteca.

### **Gestão de Empréstimos**  
- Realizar e controlar empréstimos e devoluções de livros.

### **Relatórios**  
- Gerar relatórios personalizados, como:
  - Livros disponíveis
  - Atrasos
  - Histórico de empréstimos

### **Notificações**  
- Enviar alertas sobre prazos de devolução e empréstimos vencidos.

### **Persistência de Dados**  
- Utiliza arquivos serializados no formato `.pkl` para salvar e carregar os dados do sistema.

---

## Estrutura do Projeto

```plaintext
.
├── src/
│   ├── livros.py           # Módulo para gerenciar livros
│   ├── leitores.py         # Módulo para gerenciar leitores
│   ├── funcionarios.py     # Módulo para gerenciar funcionários
│   ├── emprestimos.py      # Módulo para gerenciar empréstimos
│   ├── utils.py            # Funções auxiliares para o sistema
│   └── main.py             # Arquivo principal que executa o sistema
├── ADC_TRABALHO/           # Pasta para armazenar arquivos de dados
│   ├── livros.pkl          # Arquivo serializado para armazenar dados de livros
│   ├── leitores.pkl        # Arquivo serializado para leitores
│   ├── funcionarios.pkl    # Arquivo serializado para funcionários
│   └── emprestimos.pkl     # Arquivo serializado para empréstimos
├── README.md               # Documentação do sistema
└── requirements.txt        # Dependências do projeto
```

---

Este projeto foi desenvolvido para facilitar a gestão de bibliotecas, otimizando os processos administrativos e a experiência dos utilizadores.