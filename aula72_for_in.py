
# texto = 'python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i += 1



# senha_salva = '12345'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:

#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(f'Repetiu {repeticoes}X: ')

# print('Aquele laço acima pode ter repetiçoes infinitas')


texto = 'python'
novo_valor = ''
for letras in texto:
    novo_valor += f'*{letras}'
    print(letras)

print(novo_valor + '*')

