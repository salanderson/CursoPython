"""
    Desempacotamento em chamadas de metodos e funçoes
"""

string = 'ABCD'
lista = ['maria', 'helena', 'eduarda']
tupla = 'Python', 'é', 'legal'

# a, b, c = lista
# print(a, c)

# for item in lista:
#     # print(item)
#     for linha in item:
#         print(linha)

# Desempacotando a lista passando em cada um dos itens com "*" ao inves de usa sep='' e end=''
print(*lista)
print(*string)
print(*tupla)
