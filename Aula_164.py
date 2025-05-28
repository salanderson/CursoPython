# Variaveis livres + nonlocal

# Aula 164

# print(globals())

# def fora (x):
#     a = x

#     def dentro():
#         print(locals())

#         return a 
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar=''):
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna

# c = concatenar('a')
# print(c('b'))
# print(c('c'))
# print(c('d'))
# final = c()
# print(final)

"""  
Funçoes decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funçoes decoradoras sao funçoes que decoram outras funçoes
Decoradores sao usados para fazer o python usar as funçoes 
decoradoras em outras funçoes
Aula - 165
Decoradores sao "Syntax Sugar" (Açucar sintatico)
Aula 166

"""
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora voce foi decorada')
        return resultado
    return interna

@criar_funcao
def inverter_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverter_string('123')
print(invertida)
