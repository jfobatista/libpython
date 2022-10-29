import pytest

from libpython.spam.enviador import Enviador
from libpython.spam.main import EnviadorDeSpam
from libpython.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtde_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='João', email='jonesjoao@gmail.com'),
            Usuario(nome='Gabi', email='gabi@gmail.com')
        ],
        [
            Usuario(nome='João', email='jonesjoao@gmail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao,
                      usuarios):  # testar quantos spam foram enviados, dessa forma, entender quantas vezes
    # o método enviador foi chamado e quantos usuários foram salvos na sessão
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    # busca os usuarios do banco de dados pela sessao e envia os emails pelo enviador
    enviador_de_spam.enviar_emails(
        'jonesjoao_@hotmail.com',
        'Jogo',
        'Ruim'
    )
    assert len(usuarios) == enviador.qtde_emails_enviados



def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='João', email='jonesjoao@gmail.com')
    # testar quantos spam foram enviados, dessa forma, entender quantas vezes
    # o método enviador foi chamado e quantos usuários foram salvos na sessão
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    # Injeção de dependencia - para que enviadordespam funcione, ele depende de sessao e enviador
    # podemos trocar o enviador por outro
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    # busca os usuarios do banco de dados pela sessao e envia os emails pelo enviador
    enviador_de_spam.enviar_emails(
        'gabi@hotmail.com',
        'Jogo',
        'Ruim'
    )
    assert enviador.parametros_de_envio == (
        'gabi@hotmail.com',
        'jonesjoao@gmail.com',
        'Jogo',
        'Ruim'
    )
