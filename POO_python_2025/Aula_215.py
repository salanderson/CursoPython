'''
Relaçoes entre classes: associação, agregaçao e composiçao 
Associaçao e um tipo de relaçao onde os objetos estao ligados
dentro do sistema.
Essa e a relaçao mais comum entre objetos e tem subconjuntos
como agregaçao e composiçao (que veremos depois).
Geralmente, temos uma associaçao quando um objeto tem 
um atributo que especifica outro objeto
A associaçao nao especifica como um objeto controla
o ciclo de vida de outro objeto

Aula 215 - 216

'''

# class Escritor:
#     def __init__(self, nome):
#         self.nome = nome

#     @property
#     def ferramenta(self):
#         return self._ferramenta
    
#     @ferramenta.setter
#     def ferramenta(self, ferramenta):
#         self._ferramenta = ferramenta

# class FerramentaDeEscrever:
#     def __init__(self,  nome):
#         self.nome = nome

#     def escrever(self):
#         return f'{self.nome} esta escrevendo'
    

# escritor = Escritor('Luiz')
# caneta = FerramentaDeEscrever('Caneta Bic')
# maquina_de_escrever = FerramentaDeEscrever('Maquina')
# escritor.ferramenta = maquina_de_escrever

# print(caneta.escrever())
# print(maquina_de_escrever.escrever())
# print(escritor.ferramenta.escrever())

#-----------------------------------------------------------------
# Aula - 216


class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        # self._produtos.append(produto)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())