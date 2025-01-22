"""
Faça um jogo para o usuario adivinhar qual 
e a palavra secreta.
- Voce vai propor um palavra secreta
qualquer e vai dar a possibilidade para 
o usuario digitar apenas uma letra.
- Quando o usuario digitar uma letra, voce 
vai conferir se a letra digitada esta na palavra
secreta.

- se a letra digitada nao estiver na palavra secreta;
exiba *.
Faça a contagem de tentativas do seu usuario.

"""

import os

palavra_secreta = 'peixe'
letras_acertadas = ''

tentativas = 0

print('Descruba a palavra secreta')

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabens voce descobriu a palavra secreta' , palavra_secreta)
        print('Total de tentativas: ' ,tentativas)
        letras_acertadas = ''
        tentativas = 0
