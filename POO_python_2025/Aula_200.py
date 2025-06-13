# Metodos em instancias de classes python
#Hard coded  - >   E algo que foi escrito diretamente no codigo

class Carro:
    def __init__(self, nome):
        self.nome = nome 

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome ='Celta')
print(celta.nome)
celta.acelerar()

# Aula - 201
# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instancia da class (objeto) - Tem os dados
# Uma classe pode gerar varias instancias 
# Na classe o self e a propia instancia

# Aula - 202
# Escopo da classe e de metodos da classe

class Animal:
    # nome = 'Leão'
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimentando):
        return f'{self.nome} esta comendo {alimentando}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome='Leao')
print(leao.nome)
print(leao.executar('maçã'))