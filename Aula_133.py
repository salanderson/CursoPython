"""
Funçao lambda em python
A funçao lambda e uma funçao como qualquer outra
em python. Porem, sao funçoes anonimas que contem 
apenas uma linha. Ou seja, tudo deve ser contido 
dentro de uma unica expressão.
Aula - 133

"""

lista = [
    {'nome' : 'Anderson', 'sobrenome' : 'Saldanha'},
    {'nome' : 'Maria', 'sobrenome' : 'Oliveira'},
    {'nome' : 'Daniel', 'sobrenome' : 'Silva'},
    {'nome' : 'Eduardo', 'sobrenome' : 'Moreira'},
    {'nome' : 'Aline', 'sobrenome' : 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()
    
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)