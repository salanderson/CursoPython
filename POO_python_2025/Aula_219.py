# Aulas 219 - 220

'''
Composiçao - E dono de, Herança - E um 
Herança vs Composiçao
Classe principal (Pessoa)
-> super class, base class, parent class
Classes filhas (cliente)
-> sub class, child class, derived class 

'''

class Pessoa:
    cpf = '123'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem sai da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'blablabla'

c1 = Cliente('Anderson', 'Saldanha')
c1.falar_nome_classe()

a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)  
