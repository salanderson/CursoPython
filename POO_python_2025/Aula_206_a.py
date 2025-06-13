# Exercicio - salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instancias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

caminho_arquivo = 'aula_206.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Anderson', 34)
p2 = Pessoa('teste', 0)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

bd = [vars(p1), p2.__dict__]

def fazer_dump():
    with open(caminho_arquivo, 'w') as arquivo:
        print('Fazendo Dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Ele e o __main__')
    fazer_dump()