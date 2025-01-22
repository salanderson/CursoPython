#Tuplas sao imutaveis nao e possivel alterar os indices igual altera nas listas

# Enumerate - enumera iteraveis (indices)

lista = ['maria', 'joao', 'davi', 'testando']

lista.append('Jose')

for indices, nome in enumerate(lista):
    print(indices, nome)
