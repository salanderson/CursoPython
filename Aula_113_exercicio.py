# Exercicios com funçoes 

# Crie um fançao que multiplica todos os argumentos 
# nao nomeados recebidos
# Retorne o total para uma variavel e mostre o valor  da variavel


# Segundo Exercicio
# Crie uma função para mostra se o numero e par ou impar.
# Retorne se o numero e par ou impár


# Exercicio 1
def multiplicacao(a, b, c, d, e, f, g, h):
    mult = a * b * c * d * e * f * g * h


    print(f'Total: {mult}')

multiplicacao(1, 2, 3, 4, 5, 6, 7, 8)

# Exercicio 2

def parimpar(a, b):
    a = input('Digite um valor: ')

    if int(a) % int(b) == 0:

        print(f'O numero digitado {a} e par')
    else:
        print(f'O numero digitado {a} e impar')

parimpar(a = 0, b = 2)

# Resoluçao Exercicio 1 do Professor

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(f'Resultado: {multiplicacao}')

# Resoluçao Exercicio 2 do Professor

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} e impar'

print(par_impar(5))
print(par_impar(12))
print(par_impar(7))
print(par_impar(18))