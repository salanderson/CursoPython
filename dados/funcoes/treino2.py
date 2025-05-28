def mensagem(saudacao):
    def retorna_mensagem(nome):
        return f'{saudacao}, {nome}'
    return retorna_mensagem

bom_dia = mensagem('Bom dia')

for nome in ['Anderson', 'Joao', 'Luiz']:
    print(bom_dia(nome))

