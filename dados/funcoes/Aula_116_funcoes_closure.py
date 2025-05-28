"""  
Closure e funçoes que retornam outras funçoes

"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('bom dia')
s2 = criar_saudacao('boa noite')

for nome in ['Anderson', 'Maria', 'Luiz']:
    print(s1(nome))
    print(s2(nome))