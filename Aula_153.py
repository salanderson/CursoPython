"""  
Modulos padrao do python (import, from, as e *)
inteiro - import nome_modulo
Vantagens: voce tem o namespace do  mudulo
Desvantagens: nomes grandes

import sys

plataform = 'A MINHA'
print(sys.platform)
print(platform)

partes - from nome_modulo import objeto1, objeto2
Vantagens: nomes pequenos
Desvantagens: Sem o namespace do modulo

from sys import exit, platform
print(platform)

alias 1 - import nome_modulo as apelido

import sys as s

alias 2 - from nome_modulo import objeto as apelido
Vantagens: voce pode reservar nomes para seu codigo
Desvantagens: pode ficar fora do padrao da linguagem

má pratica - from  nome_modulo import *
Vantagens: importa tudo de um modulo
Desvantagens: importa tudo de um modulo

"""
from sys import exit, platform

print(platform)
exit()