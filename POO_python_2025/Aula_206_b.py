import json

from Aula_206_a import caminho_arquivo, Pessoa, fazer_dump

fazer_dump()

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)