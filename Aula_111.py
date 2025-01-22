"""
args - Argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre -  te desempacotamento
x, y, *resto = 1, 2, 3,4
print(x, y, resto)

# def soma(x, y):
#   return x + y

def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, '+' ,numero)
        total += numero
        print('Total =', total)
    print(f'Total final {total}')

soma(1, 2, 3, 4, 5, 6)