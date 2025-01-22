nome = input('Digite um nome: ')

print(f'Seu nome era {nome}')

def letra_nome():

    global nome
    nome = input('Digite seu nome novamente: ')
    # lista_nome = range(len(nome))
    lista_nome = [nome]

    for letra in lista_nome:
        letras = letra

        if letras[0] == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'x' or 'z':
            nome = '_' + letras + '_'

letra_nome()
print(f'Agora seu nome e {nome}')