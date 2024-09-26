import pytest
from django.urls import reverse
from model_bakery import baker

from viralata.base.models import Projeto
from viralata.django_assertions import assert_contains


@pytest.fixture
def projeto(db):
    return baker.make(Projeto)


@pytest.fixture
def resp(client, projeto):
    return client.get(reverse("base:projeto", args=(projeto.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp):
    assert_contains(resp, "</h1>Intervenção artística em espaços públicos</h1>")


def teste_galeria(request, templates_name):
    assert_contains(request, templates_name, "Foto", "projeto", "titulo")
