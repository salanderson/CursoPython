# Dictionary Comprehension e Set Comprehension
# Aula 141

# produto = {
#     'nome' : 'Caneta Azul',
#     'preco' : 2.5,
#     'categoria' : 'Escritorio'
# }

# dc = {
#     chave : valor.upper()
#     if isinstance(valor, str) else ValueError
#     for chave, valor 
#     in produto.items()
#      if chave != 'categoria'
# }

# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor a'),
#     ('c', 'valor a'),
# ]

# dc = {
#     chave : valor 
#     for chave, valor in lista
# }

# s1 = {i for i in range(10)}
# print(s1)

"""  
isinstance - para saber se objeto e de determinando tipo
Aula 142
"""
# lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, 
#          {'nome' : 'Luiz'}]

# for item in lista:
#     if isinstance(item, set):
#         print('SET')
#         item.add(5)
#         print(item, isinstance(item, set))

#     elif isinstance(item, str):
#         print('STR')
#         print(item.upper())

#     elif isinstance(item, (int, float)):
#         print('NUM')
#         print(item, item * 2)
    
#     else:
#         print('OUTRO')
#         print(item)

"""  
Valores Truthy e Falsy, Tipos Mutaveis e Imutaveis
Mutaveis [] {} set()
Imutaveis () "" 0 0.0 None False range(0, 10)
 Aula 143

"""
# lista = []
# dicionario = {}
# conjunto = set()
# tupla = ()
# string = ''
# inteiro = 0
# flutuante = 0.0
# nada = None
# falso = False
# intervalo = range(0)

# def falsy(valor):
#     return 'falsy' if not valor else 'truthy'

# print(f'TESTE', falsy('TESTE'))
# print(f'{lista=}', falsy(lista))
# print(f'{dicionario=}', falsy(dicionario))
# print(f'{conjunto=}', falsy(conjunto))
# print(f'{tupla=}', falsy(tupla))
# print(f'{string=}', falsy(string))
# print(f'{inteiro=}', falsy(inteiro))
# print(f'{flutuante=}', falsy(flutuante))
# print(f'{nada=}', falsy(nada))
# print(f'{falso=}', falsy(falso))
# print(f'{intervalo}', falsy(intervalo))

"""  
dir, hasattr e getattr em Python
Aula 144
"""
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
     print('Existe')
     print(getattr(string, metodo))
else:
     print('Nao existe o metodo', metodo)


