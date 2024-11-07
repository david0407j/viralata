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


def test_arte_urls(
    resp,
):
    assert_contains(resp, "arte")


def test_galeria_urls(resp):
    assert_contains(resp, "galeria")


def test_projeto_urls(resp):
    assert_contains(resp, "projeto")
