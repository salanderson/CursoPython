"""
Criando Exceptions em Python Orientado a Objetos
Para criar uma Exception em Python, voce so 
precisa herdar de alguma exceçao da linguagem.
A recomendação da doc e herdar de Exception.
https://docs.python.org/3/library/exceptions.html
Criando exceçoes (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceçoes
Relançando exceçoes
Adicionando notas em exceçoes (3.11.0)

Aula 234 - 235 - 236

"""

class MeuError(Exception):
    ...

class OutroError(Exception):
    ...


def levantar():
    excecao = MeuError('A', 'b', 'c')
    excecao.add_note('Olha a nota 1')
    excecao.add_note('voce errou isso')
    raise excecao

try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args) 
    print()
    excecao = OutroError('Vou lançar de novo')
    excecao.add_note('Mais uma nota')
    excecao.__notes_ = error.__notes__.copy()
    raise excecao
