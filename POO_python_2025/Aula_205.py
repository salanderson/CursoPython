# __dict__ e vars para atributos de intancia
# Aula - 205

class Pessoa:
    ano_atual  = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Joao', 35)

print(p1.get_ano_nascimento())

dados = {'nome': 'Joao', 'idade': 35}
p1 = Pessoa(**dados)

# p1.nome = 'EITA'
# print(p1.idade)
# p1.__dict__['outra'] = 'outra'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print( vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)