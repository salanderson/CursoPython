# reduce - faz a reduçao de um iteravel em um valor
from functools import reduce

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

total = 0
for p in produtos:
    total += p['preco']
print(f'Valor total: {total}')

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto, '\n')
    return acumulador + produto['preco']

total_reduce = reduce(
    funcao_do_reduce,
    produtos,
    0
)

total_lambda = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('Total: ', total_reduce)
print('Total com lambda', total_lambda)
