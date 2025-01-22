# numero = input('Digite um numero: ')

# if int(numero) % 2 == 0:
#     print(f'O Numero {numero} e par')
# else:
#     print(f'O Numero {numero} e impar')



# HoraAtual = input('digite a hora atual: ')


# if int(HoraAtual) >= 0 and int(HoraAtual) <= 11:
#     print(f'Hora atual: {HoraAtual} Horas, Bom dia!')
    
# elif int(HoraAtual) >= 12 and int(HoraAtual) <= 17:
#     print(f'Hora atual: {HoraAtual} Horas, Boa tarde')
    
# elif int(HoraAtual) >= 18 and int(HoraAtual) <= 23:
#     print(f'Hora atual: {HoraAtual} Horas, Boa noite')
    
# elif int(HoraAtual) == 00: 
#     print(f'Hora Atual: {HoraAtual}')
    

nome = input('Digite seu nome: ')

if len(str(nome)) <= 4:
    print(f'Seu nome {nome} é curto', 'e tem ' ,len(nome), 'Letras')

if len(str(nome)) >= 5 and len(str(nome)) <= 6:
    print(f'Seu nome {nome} è normal', 'e tem ' ,len(nome), 'Letras')

if len(str(nome)) > 6:
    print(f'Seu nome {nome} é muito grande', 'e tem ' ,len(nome), 'Letras')
