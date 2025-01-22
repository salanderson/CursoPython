# Repetiçoes
# while (enquanto)
# ;Executa uma açao enquanto uma condiçao for verdadeira

condicao = True

while condicao:
    condicao += 1
    nome= input('Digite seu nome: ')
    print(f'Seu nome e {nome}')

    if condicao > 3:
        break