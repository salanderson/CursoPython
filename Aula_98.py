"""
Calculo do primeiro digito do CPF
CPF : 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem
regressiva começando de 10

Ex: 746.824.890-70 (74682489070)
    10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

    Somar todos os resultados:
    70+36+48+56+12+20+32+27+0 = 301
    Multiplicar o resultado anterior por 10
    301 * 10 = 3010
    Obter o resto da divisao da conta anterior por 11
    3010 % 11 = 7
    Se o resultado anterior for maior que 9:
        resultado e 0
    contrario disso:
        resultado e o valor da conta

    O primeiro digito do cpf e 7
"""

cpf_enviado = '74682489070'
nove_digitos =  cpf_enviado[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


"""
Calculo do segundo digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11

Ex.: 746.824.890-70 (74682489070)
    11  10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0   7 <-- PRIMEIRO DIGITO
    77  40  54  64  14  24  40  36  0   14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obeter o resto da divisao da conta anterior por 11
3630 % 11 = 0
Se o resultador anterior for maior que 9:
    resultado e 0
contrario disso:
    resultado e o valor da conta
O segundo digito do cpf e 0

"""
# cpf = '36440847007'

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
print(dez_digitos)
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2 
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 *10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
print(dez_digitos)
print(cpf_gerado)
if cpf_enviado == cpf_gerado:
    print(f'CPF: {cpf_enviado} é valido')
else:
    print('CPF invalido')
    


