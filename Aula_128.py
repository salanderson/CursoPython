"""
Metodos uteis:
add, update, clear, discard
Aula 128 - 129 - 130

"""
# s1 = set()
# s1.add('Anderson')
# s1.add(1)
# s1.update(('Ola mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Ola mundo')
# s1.discard('Anderson')

# print(s1)

"""
Operadores uteis:
uniao | uniao (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simetrica ^ - Itens que nao estao em ambos
Aula 129
"""

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s1 ^ s2

# print(s3)

"""
Exemplo de uso de sets
Aula 130

"""
letras = set()
letra_secreta = 'y'
tentativas = 0
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra por vez!')
        continue
    if letra == letra_secreta:
        print('Parabens voce acertou a letra secreta')
        break
    print(letras)
print(f'Numero de tentativas: {tentativas}')
