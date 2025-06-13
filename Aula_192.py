'''
Exercicio - Lista de tarefas com desfazer e refazer
todo = [] -> lista de tarefas
todo = ['fazer cafe'] -> Adicionar fazer cafe
todo = ['fazer cafe', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer cafe',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer cafe']
refazer = todo ['fazer cafe']
refazer = todo ['fazer cafe', 'caminhar']
Aulas 192 - 195
'''
import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa =  tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} Adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)
    
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Voce nao digitou uma tarefa.')
        return
    print(f'{tarefa=} Adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def ler(tarefas, caminho_arquivo):
     dados = []
     try:
        with open('lista_tarefas.json', 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
     except FileNotFoundError:
        print('Arquivo nao existe')
        salvar(tarefas, caminho_arquivo)
     return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii= False)
    return dados
     
CAMINHO_ARQUIVO = 'lista_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer' : lambda: refazer(tarefas, tarefas_refazer),
        'clear' : lambda: os.system('cls'),
        'adicionar' : lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

# Logica usando if else

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     continue