#Decoradores com parametros
# Aula 167

# def fabrica_de_decoradores(a=None, b=None, c=None):
#     def fabirca_de_funcoes(func):
#         print('Decoradora 1')

#         def aninhada(*args, **kwargs):
#             print('Parametros do decorador, ', a, b, c)
#             print('Aninhada')
#             res = func(*args, **kwargs)
#             return res
#         return aninhada
#     return fabirca_de_funcoes

# @fabrica_de_decoradores(1, 2, 3)
# def soma(x, y):
#     return x + y

# decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x, y : x * y)

# dez_mais_cinco = soma(10, 5)
# dez_vezes_cinco = multiplica(10, 5)

# print(dez_mais_cinco)
# print(dez_vezes_cinco)

"""  
Ordem dos decoradores
Aula - 168
"""
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return  sua_nova_funcao
    return decorador

@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')

def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)