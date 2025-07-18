'''
Relaçoes entre classes: associação, agregaçao e composiçao
Composiçao e uma especializaçao da agregaçao 
Mas nela, quando o objeto "pai" for apagado, todas
as referencias dos objetos filhos tambem são apagadas.

'''
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self,  rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando,', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua Alfandega', 454)
endereco_externo = Endereco('Av Saude', 23454)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.lista_endereco()

del cliente1

print('Aqui termina o codigo')

