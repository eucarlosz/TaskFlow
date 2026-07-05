from app import app


def test_pagina_inicial():
    cliente = app.test_client()
    resposta = cliente.get("/")

    assert resposta.status_code == 200


def test_adicionar_tarefa():
    cliente = app.test_client()

    resposta = cliente.post(
        "/adicionar",
        data={
            "titulo": "Teste",
            "descricao": "Descrição de teste",
            "prioridade": "Alta",
            "status": "Pendente",
        },
        follow_redirects=True,
    )

    assert resposta.status_code == 200
    assert b"Teste" in resposta.data


def test_pagina_editar_inexistente():
    cliente = app.test_client()

    resposta = cliente.get("/editar/999", follow_redirects=True)

    assert resposta.status_code == 200