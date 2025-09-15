"""
__new__ e __init__ em classes Python
__new__ e o metodo responsavel por cirar e 
retornar o novo objeto. Por isso, new recebe cls.
__new__ DEVE retornar o novo objeto
__init__ e o metodo responsavel por inicializar
a instancia. Por isso, init recebe self.
__init__ NAO DEVE retornar nada (None)
object e a super classe de uma classe


Aula 240
"""

class A:
    def __new__(cls):
        print('Antes de criar a inst')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.x = 123
        return instancia
    
    def __init__(self):
        print('Sou o init')

    def __repr__(self):
        return 'A()'
    
a = A()
print(a)
