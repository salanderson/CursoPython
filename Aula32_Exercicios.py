# Faça um programa que peça ao usuario para digitar um numero inteiro, 
# informe se este numero e par ou impar. Caso o usuario nao digite um numero
# inteiro, informe que nao e um  numero inteiro.

numero_int = int(input('Digite um numero: '))

if numero_int % 2 == 0:
    print('Numero e par')
else:
    print('Numero e impar')


# Faça um programa que pergunte a hora ao usuario e, baseando-se no horario 
# descrito, exiba a saudação apropriada. Ex Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

horario_atual = int(input('que horas sao: '))

if horario_atual >= 0 and horario_atual <= 11:
    print('Bom dia')
if horario_atual >= 12 and horario_atual <= 17:
    print('Boa Tarde')    
if horario_atual >= 18 and horario_atual <= 23:
    print('Boa noite') 

# Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
# menos escreva "Seu nome e curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome e normal", maior que 6 escreva "Seu nome e muito grande".


nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print ('Quantidade de letras = ', tamanho, ',Seu nome e curto')
if tamanho == 5 or tamanho == 6:
    print('Quantidade de letras = ', tamanho, ',Seu nome e normal')
if tamanho > 6:
    print('Quantidade de letras = ', tamanho, ',Seu nome e muito grande')   





