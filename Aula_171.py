"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma so vai considerar o tamanho da menor.

Ex:

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

---------------- Resultado
lista_soma = [2, 4, 6, 8]

"""

print('soluçao 1')

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

print('-' * 15)
print('Soluçao 2')

lista_soma2 = []

for i, _ in enumerate(lista_b):
    lista_soma2.append(lista_a[i] + lista_b[i])
print(lista_soma2)

print('-' * 15)
print('Soluçao 3')

lista_soma3 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma3)

print('-' * 15)
print('Soluçao 4')

from itertools import zip_longest
lista_soma4 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue= 0)]
print(lista_soma4)