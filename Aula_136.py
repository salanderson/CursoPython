""" 
List comprehension em Python
List comprehension e uma forma rapida para criar listas
a partir de iteraveis
Aula 136
""" 
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print((lista))

