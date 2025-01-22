def criar_saudacoes(saudacao):
    def saudar(nome):
        return f'{nome}, {saudacao}'
    return saudar
    
saudacao_dia = criar_saudacoes('Bom dia')
saudacao_noite = criar_saudacoes('Boa noite')

for nome in ['Anderson', 'Trevor', 'Franklin', 'Maikon']:
    print(saudacao_dia(nome))
    print(saudacao_noite(nome))