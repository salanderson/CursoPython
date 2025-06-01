"""
Funçoes recursivas e recursividade
- funçoes que podem se chamar de volta
- uteis p/ dividir problemas grnades em partes menores
Toda funçao recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso base que para a recursão
- fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

Aula 179 - 180
"""

# def recursiva(inicio = 0, fim = 10):

#     print(f'inicio = {inicio} fim = {fim}')

#     if inicio >= fim:
#         return fim
    
#     inicio += 1

#     return recursiva(inicio, fim)

# print(recursiva())


# dados factoriais aula 180

def factorial(n):

    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(6))