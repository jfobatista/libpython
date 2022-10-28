from libpython.spam.db import Conexao


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='João')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='João'), Usuario(nome='Gabi')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()
