'''
super() e a super classe na sub classe
Classe principal (Pessoa)
-> super class, base class, parent class
Classes filhas (cliente)
-> sub class, child class, derived class

Aula 121 - 122

'''

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())


class A:
    atributo_a = 'Valor A'

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor B'

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'Valor C'

    def metodo(self):
        super().metodo()
        super(B, self).metodo()
        super(A, self).metodo()
        print('C')


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()