from django.urls import reverse
import pytest
from viralata.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse("cores:cores"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Vira Lata Intervenções Artística</title>")


def test_home_link(resp):
    assert_contains(
        resp, f'href="{reverse("cores:cores")}">ViraLata Intervenções Artísticas</a>'
    )


def test_email_link(resp):
    assert_contains(resp, 'href="viralatagrafite@gmail.com"')


def test_conteudo_video(
    resp,
):
    assert_contains(
        resp,
        f"https://player.vimeo.com/video/1003424840?badge=0&autopause=0&player_id=0&app_id=58479&autoplay=1&loop=1",
    )
