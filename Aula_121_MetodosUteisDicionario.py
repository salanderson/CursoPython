# |Metodos uteis dos dicionarios em python
# len - quantas chaves
# keys - iteraveis com as chaves
# values - iteraveis com os valores
# items - iteraveis com chaves e valores
# setdefault - adiciona valor se a chave nao existe 
# copy - retorna uma copia rasa (shallow copy)
# get - obtem uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o ultimo item adicionado
# update - Atualiza um dicionario com outro

# Aula 121 - (Len, Keys, Values, Itens, Setdefault)

# pessoa = {
#     'nome' : 'Luiz Otavio',
#     'sobrenome' : 'miranda',
#     'idade' : 900,
# }

# pessoa.setdefault('idade', 0)

# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave in pessoa:
#     print(chave)


# Aula 122(Copy)

# d1 = {
#     'c1' : 1,
#     'c2' : 2,
#     'l1' : [0, 1, 2],
# }

# d2 = d1.copy()
# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)


# Aula 123(Get, Pop)

p1 = {
    'nome' : 'Luiz',
    'Sobrenome' : 'Miranda',
}

# print(p1['nome'])
# print(p1.get('nome',  'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome' : 'novo valor',
#     'idade' : 30,
# })
# p1.update(nome='novo valor', idade = 31)
# tupla = (('nome', 'novo valor'), ('idade', 35))
lista = [['nome', 'novo valor'], ['idade', 33]]
p1.update(lista)
print(p1)


