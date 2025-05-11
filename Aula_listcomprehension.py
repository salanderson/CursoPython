"""
Formas de copiar listas em python  
"""

# numeros = [1, 2, 3, 4, 5]

# novos_numeros = numeros.copy()

# copiadenumeros = [numero for numero in numeros] # Listcomprehension

# lista_numeros_vazia = []

# for numero in numeros:
#     lista_numeros_vazia.append(numero)

# numeros[0] = 20


# print(novos_numeros)
# print(numeros)
# print(copiadenumeros)
# print(lista_numeros_vazia)

# Metodo filter

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# novos_numeros = [numero for numero in numeros if numero > 5]
# print(numeros)
# print(novos_numeros)

# nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
# novos_nomes = [
#     f'{nome[:-1].lower()}{nome[-1].upper()}'
#     for nome in nomes
# ]

# print(novos_nomes)

numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)