'''
Aula 223 - 224 - 225 - 226

Herança Multipla - Python Orientado a Objetos
Quer dizer que no Python, uma classe pode estender
varias outras classes.
herança simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança multipla e mixins
Log -> Filelog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança multipla e mixins 
Log -> FileLog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, FileLog)

Python 3 usa C3 superclass linearization 
para gerar mro
Voce nao precisa estudar isso (e complexo)
https://en.wikipedia.org/wiki/C3_linearization

Para saber a ordem de chamada dos metodos
Use o metodo de classe Classe.mro()
Ou o atributo __mro__ (Dunder - Double Underscore)

'''

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    def quem_sou(self):
        print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
print(D.mro())