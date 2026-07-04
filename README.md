# 📋 TaskFlow

Sistema web para gerenciamento de tarefas desenvolvido com Python e Flask como projeto da disciplina de Engenharia de Software da UniFECAF.

## 📖 Sobre o projeto

O TaskFlow foi criado para facilitar o controle de tarefas do dia a dia. O sistema permite cadastrar, editar, visualizar e excluir tarefas, além de acompanhar a prioridade e o status de cada uma.

Durante o desenvolvimento foram utilizados conceitos de versionamento com Git, hospedagem no GitHub, integração contínua com GitHub Actions e testes automatizados com Pytest.

---

## 🚀 Funcionalidades

- Cadastro de tarefas
- Edição de tarefas
- Exclusão de tarefas
- Definição de prioridade
- Controle de status
- Interface web responsiva
- Testes automatizados
- Integração contínua com GitHub Actions

---

## 🛠 Tecnologias utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- Git
- GitHub
- GitHub Actions
- Pytest

---

## 📂 Estrutura do projeto

```
TaskFlow
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── editar.html
│
├── tests/
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ▶️ Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/eucarlosz/TaskFlow.git
```

Entre na pasta:

```bash
cd TaskFlow
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

Windows

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

Depois acesse:

```
http://127.0.0.1:5000
```

---

## 🧪 Testes

Para executar os testes utilize:

```bash
pytest
```

---

## 📷 Imagens

### Tela inicial

*(Adicionar captura de tela do sistema.)*

### Tela de edição

*(Adicionar captura de tela da edição.)*

### GitHub Actions

*(Adicionar captura da execução dos testes.)*

---

## 📌 Melhorias futuras

- Login de usuários
- Banco de dados SQLite
- Pesquisa de tarefas
- Filtros por prioridade e status
- Datas de vencimento
- Responsáveis pelas tarefas

---

## 👨‍💻 Autor

Carlos Eduardo

Projeto desenvolvido para a disciplina de Engenharia de Software — UniFECAF.