from libpython.spam.enviador import Enviador
from libpython.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    # busca os usuarios do banco de dados pela sessao e envia os emails pelo enviador
    enviador_de_spam.enviar_emails(
        'jonesjoao_@hotmail.com',
        'Jogo',
        'Ruim'
    )
