from django.urls import reverse
import pytest
from viralata.django_assertions import assert_contains


@pytest.fixture
def resp(
    client,
):
    resp = client.get(reverse("cores:home"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title> ViraLata Intervenções Artísticas </title>")


""" 
def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"') """
