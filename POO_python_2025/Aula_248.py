"""
Metaclasses sao o tipo das classes 
Em PYTHON, Tudo e um Objeto (Classes tambem)
Então, qual e o tipo de uma classe? (type)
Seu objeto e uma instancia da sua classe
Sua classe e uma instancia de type (type e uma metaclass)
type('Name', (Bases), __dict__)

Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
__new__ da metaclass e chamado e cria a nova classe
__call__ da metaclass e  chamado com os argumentos e chama:
__new__ da class com os argumentos ( cria a instancia)
__init__ da class com os argumentos
__call__ da metaclass termina a execuçao

Metodos importantes da metaclass
__new__(mcs, name, bases, dct) (Cria a classe)
__call__(cls, *args, **kwargs) (Cria e inicializa a instancia)

"Metaclasses sao magias mais profundas do que 99% dos usuarios
deveriam se preocupar. Se voce quer saber se precisa delas,
nao precisa (as pessoas que realmente precisam delas sabem 
com certeza que precisam delas e nao precisam de uma explicaçao
sobre o porque)."
- Tim Peters (CPython Core Developer)

Aulas 248 - 249 - 250
"""

# object acima

# class Foo:
#     ...


# Foo = type('Foo', (object), {})
# f = Foo()

# # print(isinstance(f, Foo))

# print(type(f))
# print(type(Foo))

def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')
        return cls    
    
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')
        return instancia

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome
    
    def falar(self):
        print('FALANDO...')


p1 = Pessoa('Anderson')
p1.falar()