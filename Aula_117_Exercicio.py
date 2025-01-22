
# Crie funçoes que duplicam, triplicam. quadriplicam o numero recebido como parametro

def nummero_recebido():
    escolha = ''
    while escolha != 0:
        
        print('-' * 80)
        recebido = int(input('Digite um numero que lhe mostrarei ele dobrado, triplicado ou quadriplicado: '))
        escolha = input('Escolha 1- Dobrado, 2- Triplicado 3- Quadriplicado e 0- para Parar o sistema: ')
        print('-' * 80)

        if escolha == '0':
            break

        elif escolha == '1':

            print('1- Dobrado')
            dobrado = recebido * 2
            print(f'Seu numero dobrado e: {dobrado}')

        elif escolha == '2':
            print('2- Triplicado')
            triplicado = recebido * 3
            print(f'Seu numero Triplicado e: {triplicado}')

        elif escolha == '3':
            print('3- Quadriplicado')
            quadriplicado = recebido * 4
            print(f'Seu numero Quadriplicaod e: {quadriplicado}')

        else :
            print('Escolha errada para a opção, escolha 1, 2 ou 3')
        print('-' * 80)

nummero_recebido()