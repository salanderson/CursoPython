lista_nome = ['Anderson', 'Maria', 'Joao']

def mensagem (saudar):
    def saudar_nome(nome):
        return f'{saudar}, {nome}'
    return saudar_nome

bom_dia = mensagem('Bom dia')

for nome in lista_nome:
    print (bom_dia(nome))

    
