'''
criando um programa para montar carros de varias marcas como fabricante e motor

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


gol = Carro('GOL')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
gol.fabricante = volkswagen
gol.motor = motor_1_0

s10 = Carro('S10')
chevrolet = Fabricante('Chevrolet')
motor_2_0 = Motor('2.0')
s10.fabricante = chevrolet
s10.motor = motor_2_0

print(gol.nome, gol.fabricante.nome, gol.motor.nome)
print(s10.nome, s10.fabricante.nome, s10.motor.nome)
