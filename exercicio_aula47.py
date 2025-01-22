nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade != ' ':
    print(f'Seu nome e:  {nome}')
    print(f'Sua idade e:  {idade}')

    print('Seu nome invertido e:')
    print(nome[::-1])

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços')    

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeiro letra do seu nome e:  {nome[0]}')
    print(f'A ultima letra do seu nome e: {nome[-1]}')

else:
    print('Desculpe, voce deixou campos vazio.')


# anderson
# 01234567