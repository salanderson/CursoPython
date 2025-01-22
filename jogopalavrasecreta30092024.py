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

palavra_secreta = 'aviao'
letra_certa = ''
tentativas = 0

while True:
    tentativas += 1
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letra_certa += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ' ,palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Voce acertou parabens || A palavra secreta e: ' ,palavra_secreta)
        print('Seu numero de tentativas foi: ' ,tentativas)
        letra_certa = ''
        tentativas = 0


