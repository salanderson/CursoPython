"""
Introduçao as funcoes (def) em Python
Funçoes sao trechos de codigo usados para replicar determinada 
açao ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos) e retornar
um valor especifico.
Por padrao, funcoes Python retornam None (nada).
"""

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5 ,6)

def saudacao(nome= 'Sem Nome'):
    print(f'Oi, {nome}')

saudacao()

saudacao('Manoel teco teco')
saudacao('terrorista')


"""
Aula 106 - Argumentos nomeados e argumentos posicionais (nao nomeados) em funçoes

"""

def soma(x ,y ,z):
    # Definiçao
    print(f'{x=} y={y} {z=}' , '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')