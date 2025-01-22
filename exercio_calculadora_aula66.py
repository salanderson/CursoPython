
while True:
    
    valor1 = input('Digite o valor: ')
    valor2 = input('Digite o valor2: ')

    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    val_1_float = 0
    val_2_float = 0

    try:
      val_1_float = float(valor1)
      val_2_float = float(valor2)  
      numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{val_1_float} + {val_2_float} =  ', val_1_float + val_2_float)
    
    elif operador == '-':
        print(f'{val_1_float} - {val_2_float} = ', val_1_float - val_2_float)

    elif operador == '*':
        print(f'{val_1_float} * {val_2_float} = ', val_1_float * val_2_float)

    elif operador == '/':
        print(f'{val_1_float} / {val_2_float} = ', val_1_float / val_2_float)
    
    else:
        print('Houve erros nao tratados nao operaçao.')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break