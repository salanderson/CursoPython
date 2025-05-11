"""  
Generate expression, Iterables e Iteratores em Python

"""
# Aula 145

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__e__next__

# Aula 146
"""  
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(lista)
print(generator)

for n in generator:
    print(n)

"""


"""  
# Aula 147

Introduçao as Generator fnctions em Python
generation = (n for n in range(100))

"""
# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1

#         if n >= maximum:
#             return

# gen = generator()
# for n in gen:
#     print(n)

"""  
Aula 148

Yield from

"""

def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('Terminou gen1')

def gen3():
    print('Começou gen3')
    yield 10
    yield 20
    yield 30
    print('Terminou gen3')

def gen2(gen=None):
    print('Começou gen2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Terminou gen2')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)

for numero in g2:
    print(numero)

for numero in g3:
    print(numero)