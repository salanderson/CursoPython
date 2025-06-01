"""  
Aula - 169 a 170
Exercicio - Unir listas
Crie uma  funçao zipper (como o zipper de roupas)
O trabalho dessa funçao sera unir duas listas na ordem
use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', MG)]
"""
print('Com funçao')
def zipper(lista1, lista2):
   intervalo_maximo = min(len(l1), len(l2))
   return [(l1[i], l2[i]) for i in range(intervalo_maximo)] 

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))

# Exemplo com o zip

print('-' * 70)
print('Com o ZIP')
list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(list1, list2)))

# usando a funçao ziperlongest

print('-' * 70)
print('zip com zip_longest')

from itertools import zip_longest
print(list(zip_longest(list1, list2, fillvalue='SEM CIDADE')))




