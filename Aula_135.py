"""
Empacotamento e desempacotamento de dicionarios
Aula 135

"""
a, b = 1, 2
a, b = b, a

# print(a, b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
}
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# args (ja vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('Nao nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos_nomeados(nome= 'Anderson', qlq= 123)

configuracoes = {
    'args1' : 1,
    'args2' : 2,
    'args3' : 3,
    'args4' : 4,
}

mostrar_argumentos_nomeados(**configuracoes)

