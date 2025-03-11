from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSms


class NotificacaoFacade:
    def __init__(self):
        self.notificacoes = [NotificacaoEmail(), NotificacaoSms()]

    def enviar_notificacoes(self, cliente, mensagem):
        for notificacao in self.notificacoes:
            notificacao.enviar_notificacao(cliente, mensagem)
