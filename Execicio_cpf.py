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

import re
import sys

# cpf_recebido = '746.824.890-70'.replace('.', '').replace('-', '')

cpf_recebido = input('Digite o nove numero para gerar seu cpf : ')
cpf_recebido  = re.sub(r'[^0-9]', '', cpf_recebido)

entrada_e_sequencial = cpf_recebido == cpf_recebido[0] * len(cpf_recebido)

if entrada_e_sequencial:
    print('Voce enviou dados sequenciais')
    sys.exit()

nove_digito = cpf_recebido[:9]
contador_regressivo_1 = 10

resultado_digito1 = 0
for digito_1 in nove_digito:
    resultado_digito1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0 
print(f'O primeiro digito do cpf e {digito_1}')


"""
calculo do segundo digito do CPF
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
# cpf = '74682489070'
"""
dez_digitos = nove_digito + str(digito_1)
contador_regressivo_2 = 11
resultado_digito2 = 0

for digito_2 in dez_digitos:
    resultado_digito2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
    
digito_2 = (resultado_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'O segundo digito do cpf e {digito_2}')

cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'

print(cpf_gerado)