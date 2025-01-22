# pessoa = dict(nome='Luiz Otavio', Sobrenome='Miranda')

# pessoa = {
#     'nome': 'Luiz Otavio',
#     'Sobrenome': 'Miranda',
#     'idade' : 18,
#     'altura' : 1.8,
#     'endereços' : [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 321},
#     ],
# }
# print(pessoa, type(pessoa))

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otavio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome', None))

if pessoa.get('sobrenome', None):
    print('Existe')
else:
    print('Nao existe')
