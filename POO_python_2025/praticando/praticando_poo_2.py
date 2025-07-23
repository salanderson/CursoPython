'''
Criando um sistema carros com fornecedor e o motor ultilizado no carro

'''

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.fabricante = None
        self.motor = None


    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome


onyx = Carro('Onyx')
chevrolet = Fabricante('Chevrolet')
motor_1_4 = Motor('1.4')
onyx.fabricante = chevrolet
onyx.motor = motor_1_4

mobi = Carro('Mobi')
fiat = Fabricante('Fiat')
motor_1_0 = Motor('1.0')
mobi.fabricante = fiat
mobi.motor = motor_1_0

print(onyx.nome, onyx.fabricante.nome, onyx.motor.nome)
print('-' * 20)
print(mobi.nome, mobi.fabricante.nome, mobi.motor.nome)