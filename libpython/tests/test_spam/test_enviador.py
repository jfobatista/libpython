import pytest

from libpython.spam.enviador import Enviador, EmailInvalido


def test_criar_enviador():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['jonesjoao@gmail.com', '123@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,  # destinatário
        'jonesjoao_@hotmail.com',  # remetente
        'Python',  # assunto
        'Linguagem Python, OO'  # corpo do email
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['jonesjoao', '']
)
def test_remetente_invalido(remetente):  # validar o email do remetente
    enviador = Enviador()
    with pytest.raises(EmailInvalido):  # gerenciador de contexto, lança exceção de email invalido
        resultado = enviador.enviar(
            remetente,  # destinatário
            'jonesjoao_@hotmail.com',  # remetente
            'Python',  # assunto
            'Linguagem Python, OO'  # corpo do email
        )
        assert remetente in resultado
