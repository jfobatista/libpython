from libpython.spam.modelos import Usuario


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='João', email='jonesjoao@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='João', email='jonesjoao@gmail.com'),
                Usuario(nome='Gabi', email='gabi@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

