class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        if not remetente:
            raise EmailInvalido('Email de remetente vazio.')
        return 'jonesjoao@gmail.com'


class EmailInvalido(Exception):
    pass
