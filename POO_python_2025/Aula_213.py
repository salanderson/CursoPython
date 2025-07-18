'''
@property + @setter - getter e setter no modo Pytonico
- como getter
- p/ evitar quebar codigo cliente
- p/ habilitar setter
- p/ executar açoes ao obter um atributo
Atributos que começar com um ou dois underlaines
nao devem ser usados fora da classe.

'''

class Caneta:
    def __init__(self, cor):
         # private / protected
         self._cor = cor
         self._cor_tampa = None

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

def mostrar(caneta):
     return caneta.cor       

caneta = Caneta('Azul')
caneta.cor = 'Rosa'

# getter -> obter valor
print(caneta.cor)
