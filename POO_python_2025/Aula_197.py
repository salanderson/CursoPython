"""
class - Classes sao doldes para criar novos objetos
As classes geram novos objetos (instancias) que
podem ter seus propios atributos e metodos.
Os objetos gerados pela classe podem usar seus dados 
internos para realizar varias açoes.
Por convençao, usamos PascalCase para nomes de classes.

"""

# Aula - 197 - 198

# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# class Pessoa:
#     ...

# p1 = Pessoa()
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otavio'

# p2 = Pessoa()
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

# print(p1.nome)
# print(p1.sobrenome)

# print(p2.nome)
# print(p2.sobrenome)

#Aula 199

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Otavio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otavio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

 


