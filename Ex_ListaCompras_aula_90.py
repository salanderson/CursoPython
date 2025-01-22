"""
Fazer uma lista de compras com listas 
o usuario dever ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Nao permita que o programa quebre com
erros de indices inexistentes na lista.
"""
import os
lista = []

while True:
    print('Selecione a opção')
    opcao = input('[i]inserir [a]apagar [l]listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
          print('Nao foi possivel apagar esta indice')  

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)