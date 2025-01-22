"""
Closure e funçoes que retornam outras funçoes

"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia!')
falar_boa_noite = criar_saudacao('Boa noite!')

for nome in ['Anderson', 'Trevor', 'Franklin']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))