"""
Metodo especial __call__
callable e algo que pode ser executado com parenteses
Em classes normais, __call__ faz a instancia de uma classe 
"callable"

"""

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'esta chamando', self.phone)
        return 12434
    
call1 = CallMe('2324456777')
retorno = call1('Anderson Saldanha')
print(retorno)