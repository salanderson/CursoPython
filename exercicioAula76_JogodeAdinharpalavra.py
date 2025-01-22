"""
Faça um jogo para o usuario adivinhar qual 
e a palavra secreta.
- Voce vai propor um palavra secreta
qualquer e vai dar a possibilidade para 
o usuario digitar apenas uma letra.
- Quando o usuario digitar uma letra, voce 
vai conferir se a letra digitada esta na palavra
secreta.

- se a letra digitada estiver na palavra secreta;
exiba *.
Faça a contagem de tentativas do seu usuario.

"""
import os

palavraSecreta = 'carro'
letras_acertadas = ''
tentativas = 0

while True:
    tentativas += 1
    print('Descubra qual e a palavra secreta.')
    letras = input('Digite uma letra: ')

    if len(letras) > 1:
        print('Digite apenas uma letra.')
        continue

    if letras in palavraSecreta:
        letras_acertadas += letras

    palavra_formada = ''
    for letra_secreta in palavraSecreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavraSecreta:
        os.system('cls')   
        print('Voce acertou!! Parabens!')
        print('A palavra secreta e :' ,palavraSecreta)
        print('Numero de tentativas: ' ,tentativas)
        letras_acertadas = ''
        tentativas = 0
        print('#' * 35)      

