'''
criando um programa para montar um carro com motor e fornecedor

'''
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome


voyage = Carro('Voyage')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
voyage.fabricante = volkswagen
voyage.motor = motor_1_0

print(voyage.nome, voyage.fabricante.nome, voyage.motor.nome)