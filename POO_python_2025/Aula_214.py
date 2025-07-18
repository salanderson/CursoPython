# Encapsulamento (modificadores de acesso : public, protected, provate)
# Python Nao Tem modificadores de acesso
# Mas podemos seguir as seguintes convençoes
#     (sem underline) = public
#         pode ser usado em qualquer lugar
# _   (um underline) = protected
#         nao DEVE ser usado fora da classe 
#         ou suas subclasses.
# __  (dois underlines) = private
#         "name mangling" (desfiguração de nomes) em Python
#         so Deve ser usado na classe em que foi declarado.

class Foo:
    def __init__(self):
        self.public = 'isso e publico'
        self._protected = 'isso e protegido'
        self.__exemplo = 'isso e private'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        print(self.__exemplo)
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    
f = Foo()
print(f.public)
print(f.metodo_publico())