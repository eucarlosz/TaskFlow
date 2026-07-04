# 📋 TaskFlow

Sistema web de gerenciamento de tarefas desenvolvido como atividade prática da disciplina de Engenharia de Software da UniFECAF.

## 📖 Sobre o Projeto

O TaskFlow é uma aplicação web que permite cadastrar, visualizar, editar e excluir tarefas, auxiliando no gerenciamento das atividades de uma equipe utilizando conceitos de metodologias ágeis.

O projeto foi desenvolvido utilizando boas práticas de Engenharia de Software, incluindo versionamento com Git, hospedagem no GitHub, testes automatizados com Pytest e integração contínua utilizando GitHub Actions.

---

# 🎯 Objetivos

- Gerenciar tarefas de forma simples e organizada.
- Aplicar conceitos de Engenharia de Software.
- Utilizar metodologia ágil (Kanban).
- Implementar testes automatizados.
- Utilizar Integração Contínua (CI) com GitHub Actions.

---

# 🚀 Tecnologias Utilizadas

- Python 3.13
- Flask
- HTML5
- CSS3
- Git
- GitHub
- Pytest
- GitHub Actions

---

# 📁 Estrutura do Projeto

```
TaskFlow/
│
├── app.py
├── requirements.txt
├── pytest.ini
├── README.md
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
└── .github/
    └── workflows/
        └── ci.yml
```

---

# ⚙️ Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/eucarlosz/TaskFlow.git
```

## 2. Entrar na pasta

```bash
cd TaskFlow
```

## 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

## 4. Ativar o ambiente virtual

Windows

```bash
.venv\Scripts\activate
```

## 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 6. Executar o projeto

```bash
python app.py
```

---

# ✅ Funcionalidades

- Cadastro de tarefas
- Listagem de tarefas
- Edição de tarefas
- Exclusão de tarefas
- Definição de prioridade

---

# 🧪 Testes Automatizados

O projeto utiliza **Pytest** para validar automaticamente o funcionamento da aplicação.

Os testes são executados localmente e também pelo GitHub Actions sempre que um novo commit é enviado ao repositório.

---

# 🔄 Integração Contínua

Foi configurado um workflow utilizando **GitHub Actions**, responsável por:

- Instalar as dependências do projeto.
- Executar os testes automatizados.
- Validar a aplicação a cada novo push.

---

# 📋 Metodologia Ágil

Durante o desenvolvimento foi utilizado o método **Kanban**, organizando as atividades nas colunas:

- To Do
- In Progress
- Done

Essa organização facilitou o acompanhamento da evolução do projeto.

---

# 🔄 Mudança de Escopo

Durante o desenvolvimento foi simulada uma alteração no escopo do projeto.

Inicialmente o sistema permitia apenas o gerenciamento básico das tarefas.

Como melhoria, foi planejada a implementação de autenticação de usuários e armazenamento das tarefas em banco de dados SQLite, permitindo maior segurança e persistência das informações.

Essa alteração foi registrada no quadro Kanban e documentada conforme solicitado pela atividade.

---

# 👨‍💻 Autor

Carlos Eduardo

Projeto desenvolvido para a disciplina de **Engenharia de Software** — UniFECAF.