from unittest.mock import Mock
import pytest
from libpython import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/99755055?v=4"
    resp_mock.json.return_value = {
        "login": "jfobatista", "id": 99755055, "node_id": "U_kgDOBfIkLw",
        "avatar_url": url
    }
    get_mock = mocker.patch('libpython.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('jfobatista')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('jfobatista')
    assert 'https://avatars.githubusercontent.com/u/99755055?v=4' == url
