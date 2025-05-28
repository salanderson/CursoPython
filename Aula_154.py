"""  
Entendendo os seus propios modulos python o primeiro modulo
executado chama-se __main__ voce pode importar outro modulo
inteiro ou parte, O python conhece a pasta onde o __main__ esta
e abaixo dele. Ele nao reconhece pastas e modulos acima do __main__
padrao, o python conhece todos os modulos e pacotes presentes nos caminhos
de sys.path

Aula 154 - 155 - 156 - 157 - 158 - 159
"""

# import Aula_153

# import sys

from sys import path

import Aula_157.Mod_Aula_157
from Aula_157.Mod_Aula_157 import soma_numeros
import Aula_157.Mod_Aula_157

# print (*path, sep='\n')

print(soma_numeros(5, 5))
print(Aula_157.Mod_Aula_157.soma_numeros(10, 10))
print()

