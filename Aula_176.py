# map para mapear dados Aula 176 - 177


from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }

novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

# Filter Aula 177

# novos_produtos_filter = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos_filter = filter(
    lambda p: p['preco'] > 100,
    produtos
)

print(novos_produtos_filter)