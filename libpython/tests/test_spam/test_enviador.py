from libpython.spam.enviador import Enviador


def test_criar_enviador():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    remetente = 'jonesjoao@gmail.com'
    resultado = enviador.enviar(
        remetente,  # destinatário
        'jonesjoao_@hotmail.com',  # remetente
        'Python',  # assunto
        'Linguagem Python, OO'  # corpo do email
    )
    assert remetente in resultado
