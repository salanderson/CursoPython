"""
Combinations, permutations e product - iteratools
combinaçao - ordem nao importa - iteravel + tamanho do grupo
permutaçao - ordem importa
produto - ordem importa e repete valores unicos

"""

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'joao', 'Joana', 'Leticia', 'Luiz',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['algodao', 'poliester'],
    ['masculino', 'feminino'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
