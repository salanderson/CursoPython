"""  
Try, except, else e finally

"""
# a = 18
# b = 0
# c = a / b
# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError:
#     print('Nao e possivel dividir um numero por 0')
# except NameError:
#     print('Nome b nao esta definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO')

# print('CONTINUAR')

"""  
try, except, else e finally
Aula 151

"""

# try:
#     print('ABRIR ARQUIVO')
#     8/0
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
#     print('ERRO DE DIVISAO POR ZERO')
# except IndexError as error:
#     print('IndexError')
# except (NameError, ImportError):
#     print('NameError, ImportError')
# else:
#     print('Nao deu erro')
# finally:
#     print('FECHAR ARQUIVO')

"""  
raise - lançando exceçoes (erros)
Aula 152

"""
def nao_aceita_dividir_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce esta tentando dividir um numero por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float. '
            f'{tipo_n} enviado. '
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceita_dividir_por_zero(d)

    return n / d

print(divide(8, 0))
