from unittest.mock import Mock

from libpython import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "jfobatista", "id": 99755055, "node_id": "U_kgDOBfIkLw",
        "avatar_url": "https://avatars.githubusercontent.com/u/99755055?v=4"
    }
    github_api.requests.get = Mock(return_value=resp_mock)  # teste isolado
    # agora não é mais necessário fazer a requisiçao do método get dentro da api do github
    # uma vez que atribuimos o valor da requisição com o dicionario resp_mock.json.return_value
    # que é um método json que tem como método o return-value (o retorno da requisicao)
    url = github_api.buscar_avatar('jfobatista')
    assert 'https://avatars.githubusercontent.com/u/99755055?v=4' == url
