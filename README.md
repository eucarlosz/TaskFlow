# 📋 TaskFlow

Sistema web de gerenciamento de tarefas desenvolvido com **Python e Flask**, criado para aplicar na prática conceitos de desenvolvimento Back-end, CRUD, testes automatizados e integração contínua.

O projeto permite criar, visualizar, atualizar e excluir tarefas por meio de uma interface web simples e funcional.

---

## 💻 Sobre o projeto

O **TaskFlow** foi desenvolvido como projeto de estudo para explorar o funcionamento de uma aplicação web utilizando Python no Back-end.

Além das funcionalidades de gerenciamento de tarefas, o projeto utiliza uma estrutura organizada com templates, arquivos estáticos, testes automatizados e workflow de CI.

O objetivo foi ir além da lógica isolada em Python e compreender melhor como diferentes partes de uma aplicação web trabalham juntas.

---

## ✨ Funcionalidades

* ➕ Cadastro de tarefas
* 📋 Visualização das tarefas cadastradas
* ✏️ Atualização de tarefas
* 🗑️ Exclusão de tarefas
* 🔄 Operações CRUD
* 🌐 Interface web
* 🧪 Testes automatizados
* ⚙️ Integração contínua com GitHub Actions

---

## 🛠️ Tecnologias

<p>
  <img alt="Python" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
  &nbsp;
  <img alt="Flask" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"/>
  &nbsp;
  <img alt="HTML5" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"/>
  &nbsp;
  <img alt="CSS3" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"/>
  &nbsp;
  <img alt="Git" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"/>
  &nbsp;
  <img alt="GitHub" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"/>
</p>

**Principais tecnologias e ferramentas:**

* Python
* Flask
* HTML5
* CSS3
* Pytest
* Git
* GitHub
* GitHub Actions

---

## 🧠 Conceitos aplicados

Durante o desenvolvimento foram praticados conceitos como:

* Desenvolvimento Back-end com Python
* Rotas com Flask
* Operações CRUD
* Requisições HTTP
* Templates HTML
* Organização de arquivos estáticos
* Estruturação de aplicações web
* Testes automatizados com Pytest
* Controle de versão com Git
* Integração contínua (CI)
* GitHub Actions

---

## 📁 Estrutura do projeto

```text id="l5ey6o"
TaskFlow/
│
├── .github/
│   └── workflows/
│
├── static/
│   └── css/
│
├── templates/
│
├── tests/
│
├── app.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash id="5j8b0f"
git clone https://github.com/eucarlosz/TaskFlow.git
```

### 2. Entre na pasta

```bash id="xvtegg"
cd TaskFlow
```

### 3. Crie um ambiente virtual

```bash id="7ec9bf"
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows:**

```bash id="4rxbpj"
.venv\Scripts\activate
```

**Linux/macOS:**

```bash id="6kcx44"
source .venv/bin/activate
```

### 5. Instale as dependências

```bash id="tvl95u"
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash id="fv3xj9"
python app.py
```

Depois, acesse no navegador o endereço informado pelo Flask no terminal.

---

## 🧪 Testes

O projeto utiliza **Pytest** para execução de testes automatizados.

Para executar os testes:

```bash id="6evvm3"
pytest
```

Os testes ajudam a verificar o comportamento da aplicação e reduzir o risco de alterações quebrarem funcionalidades existentes.

---

## ⚙️ Integração Contínua

O projeto possui um workflow configurado com **GitHub Actions**.

A automação permite executar verificações do projeto no GitHub, adicionando uma camada de validação ao processo de desenvolvimento.

O workflow está localizado em:

```text id="a7bz5a"
.github/workflows/
```

---

## 📸 Interface

As capturas de tela da aplicação podem ser adicionadas nesta seção para demonstrar visualmente o funcionamento do TaskFlow.

```html id="w8ilvc"
<p align="center">
  <img src="./images/home.png" alt="TaskFlow - Página inicial" width="900">
</p>
```

> Ajuste o nome acima para corresponder exatamente ao arquivo existente na pasta `images`.

---

## 🎯 Objetivo do projeto

O principal objetivo do TaskFlow foi aplicar conhecimentos de **Python em uma aplicação web**, conectando lógica de programação, rotas, interface e operações CRUD.

A inclusão de **testes automatizados e integração contínua** também permitiu explorar práticas importantes utilizadas no desenvolvimento de software além da implementação das funcionalidades.

---

## 🚀 Possíveis evoluções

Como projeto de estudo, o TaskFlow ainda pode evoluir com funcionalidades como:

* Persistência em banco de dados
* Sistema de usuários
* Autenticação
* Priorização de tarefas
* Datas e prazos
* API REST
* Deploy

Esses itens representam possibilidades futuras e **não funcionalidades atuais do projeto**.

---

## 👨‍💻 Autor

**Carlos Eduardo**

Estudante de **Análise e Desenvolvimento de Sistemas — UniFECAF**

<p>
  <a href="https://www.linkedin.com/in/carloseduardocostaf/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>

  <a href="https://github.com/eucarlosz">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>
