"""
Polimorfismo em Python Orientado a Objetos
Polimorfismo e o principio que permite que 
classes derivadas de uma mesma superclasse
tenham metodos iguais (com mesma assiantura)
mas comportamentos dieferentes.
Assinatura do metodo = Mesmo nome e quantidade
de paramentros (retorno nao faz parte da assiantura)
Opiniao + principios que contam:
Assinatura do metodo: nome, parametros e retorno iguais
SO"L"ID
Principio da substituiçao de liskov
Objetos de uma superclasse devem ser substituiveis
por objetos de uma subclasse sem quebrar a aplicaçao
Sobrecarga de metodos (overload) 🐍 = ❌
Sobreposiçao de metodos (override) 🐍 = ✅

Aula 232 - 233

"""
from abc import ABC, abstractmethod
class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False

def notificar(notificacao : Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificaçao enviada')
    else:
        print('Notificaçao NAO enviada')

notificacao_email = NotificacaoEmail('Testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)


