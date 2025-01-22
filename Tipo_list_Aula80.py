# string = 'ABCDE' # 5 caracteres (len)


# lista = [123, True, 'Luiz Otavio', 1.2, []]

# print(lista[2])

# lista[1] = False
# lista[2] = 'Maria M'
# lista[3] = 50.0
# lista[4] = ['A', 2, 'B', 3]

# print(lista[-3])
# print(lista)

# Minha soluçao do exercicio

# lista = ['abc', 'def', 'fgh']

# for letras in lista:
#     print(letras, lista.index(letras))

# Exercicio Resolvido

lista = ['abc', 'def', 'fgh']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

