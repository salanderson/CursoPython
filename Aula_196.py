"""
Controlando a quantidade de argumentos posicionais e nomeados em funçoes
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
Positional - only Parameters (/) - Tudo ante da barra deve ser APENAS posicional.
PEP 570 - Python Positional - Only Parameters
https://peps.python.org/pep-0570/
keyword-Only Arguments (*) - * sozinho Nao Suga valores
PEP 3102 - keyword-Only Arguments
https://peps.python.org/pep-3102/

"""

def soma (x, y):
    print(x + y)

soma(1, 2)
soma(x=1, y=2)