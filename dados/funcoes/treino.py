def cria_mensagem(mensagem):
    def executar_mensagem(nome):
        return f'{mensagem}, {nome}'
    return executar_mensagem

nova_mensagem = cria_mensagem('bom dia')

for nome in ['Anderson', 'Joao', 'maria']:
    print(nova_mensagem(nome))

