nome = input('digite seu nome: ')
sobrenome = input('digite seu sobrenome: ')
idade = input('digite sua idade: ')
ano_atual = input('digite o ano atual: ')
ano_nascimento = int(ano_atual) - int(idade)

print(f'{nome} {sobrenome} , sua idade e: {idade} anos e voce nasceu em : {ano_nascimento}')   