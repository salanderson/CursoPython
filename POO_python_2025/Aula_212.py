'''
@property - um getter no modo Pythonico
getter - um metodo para obeter um atributo
modo pythonico - modo do Python de fazer coisas
@propety e uma propriedade do objeto, ela
e um metodo que se comporta como um atributo
Geralmente e usada nas seguintes situaçoes:
- como getter
- p/ evitar quebrar codigo cliente
p/ habilitar setter
p/ executar açoes ao obter um atributo

'''

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPETY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)