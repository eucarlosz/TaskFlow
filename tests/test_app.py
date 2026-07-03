import pytest
from app import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True

    with app.test_client() as cliente:
        yield cliente


def test_pagina_inicial(cliente):
    resposta = cliente.get("/")

    assert resposta.status_code == 200