# Criando arquivos com Python + Context Manager withMore actions
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# Aula - 186 - 187 - 188 - 189 - 190

# caminho_arquivo = 'C:\\Users\\ANDERSON_SALDANHA\\Desktop\\Curso_python2024\\Arquivos_python\\arquivo.txt'
# caminho_arquivo = 'arquivo.txt'

# with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#     print('Ola mundo')
#     print('Arquivo vai ser fechado')
#     arquivo.write('Atenção\n')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )


# Aula 190 - arquivos json
import json
pessoa = {
    'nome' : 'Luiz Otavio',
    'sobrenome' : 'Miranda',
    'endereco' : [
        {'rua' : 'R1', 'numero' : 32},
        {'rua' : 'R2', 'numero' : 55},
    ],
    'altura' : 1.8,
    'numeros_preferidos' : (2, 4, 6, 8, 10),
    'dev' : True,
    'nada' : None,
}

with open('arquivo_json.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('arquivo_json.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)