from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = []

@app.route("/")
def inicio():
    return render_template("index.html", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():

    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade
    }

    tarefas.append(tarefa)

    return render_template("index.html", tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)