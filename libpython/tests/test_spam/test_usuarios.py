import pytest

from libpython.spam.db import Conexao


@pytest.fixture
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.rollback()
    sessao_obj.fechar()


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='João')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='João'), Usuario(nome='Gabi')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

