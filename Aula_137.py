"""
Introduçao a List comprehension em Python
List comprehension e uma forma rapida para criar listas 
a partir de iteraveis.
print(list(range(10)))

Aula 137 - 138 - 139
"""

# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]

# # print(lista)

# # mapeamento de dados em list comprehension
# produtos =[
#     {'nome' : 'p1', 'preco' : 20,},
#     {'nome' : 'p2', 'preco' : 10,},
#     {'nome' : 'p3', 'preco' : 30,},
# ]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# # print(*novos_produtos, sep='\n')

# novos_produtos = [
#     {**produto, 'preco' : produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
# ]

# # print(novos_produtos)


lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]
print(lista)
