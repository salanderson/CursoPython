# Faça um programa que peça ao usuario para digitar um numero inteiro, 
# informe se este numero e par ou impar. Caso o usuario nao digite um numero
# inteiro, informe que nao e um  numero inteiro.

numero_inteiro = int(input('Digite um numero: '))

if numero_inteiro % 2 == 0:
    print(numero_inteiro, 'e um numero Par')
if numero_inteiro % 2 != 0:
    print(numero_inteiro, 'e um numero Impar')

print(20 * '-')



# Faça um programa que pergunte a hora ao usuario e, baseando-se no horario 
# descrito, exiba a saudação apropriada. Ex Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

hora_atual = int(input('Digite o horario: '))

if hora_atual >= 0 and hora_atual <= 11:
    print('Bom dia!')
if hora_atual >= 12 and hora_atual <= 17:
    print('Boa tarde!')
if hora_atual >= 18 and hora_atual <= 23:
    print('Boa noite!')

print(20 * '-')

# Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
# menos escreva "Seu nome e curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome e normal", maior que 6 escreva "Seu nome e muito grande".

nome = input('Digite primeiro nome: ')

tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome e curto')
if tamanho >= 5 and tamanho <= 6:
    print('Seu nome e normal')
if tamanho > 6:
    print('Seu nome e muito grande')

print(20 * '-')