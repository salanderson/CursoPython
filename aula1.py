nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
ano_nascimento = int(input('Digite o ano atual: ')) - int(idade)
maior_de_idade = int(idade) >= 18
altura_metros = input('Digite sua altura: ')
print('*' * 40)

print('Nome: ' , nome)
print('Sobrenome: ' , sobrenome)
print('Idade: ' , idade)
print('Ano de nascimento: ' , ano_nascimento)
print('E maior de idade?: ' , maior_de_idade)
print('Altura em metros: ' , altura_metros)
