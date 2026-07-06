from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []
contador_id = 1


def obter_estatisticas():
    return {
        "total": len(tarefas),
        "pendentes": len([t for t in tarefas if t["status"] == "Pendente"]),
        "andamento": len([t for t in tarefas if t["status"] == "Em andamento"]),
        "concluidas": len([t for t in tarefas if t["status"] == "Concluída"]),
    }


@app.route("/")
def inicio():

    filtro = request.args.get("status", "Todos")

    if filtro == "Todos":
        tarefas_filtradas = tarefas
    else:
        tarefas_filtradas = [
            tarefa for tarefa in tarefas
            if tarefa["status"] == filtro
        ]

    estatisticas = obter_estatisticas()

    return render_template(
        "index.html",
        tarefas=tarefas_filtradas,
        total=estatisticas["total"],
        pendentes=estatisticas["pendentes"],
        andamento=estatisticas["andamento"],
        concluidas=estatisticas["concluidas"],
        filtro=filtro
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    global contador_id

    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]
    status = request.form["status"]

    nova_tarefa = {
        "id": contador_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": status,
    }

    tarefas.append(nova_tarefa)
    contador_id += 1

    return redirect(url_for("inicio"))


@app.route("/excluir/<int:id>")
def excluir(id):
    global tarefas

    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != id]

    return redirect(url_for("inicio"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa is None:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        tarefa["titulo"] = request.form["titulo"]
        tarefa["descricao"] = request.form["descricao"]
        tarefa["prioridade"] = request.form["prioridade"]
        tarefa["status"] = request.form["status"]

        return redirect(url_for("inicio"))

    return render_template("editar.html", tarefa=tarefa)


if __name__ == "__main__":
    app.run(debug=True)