"""
Classes abstratas - Abstract Base Class (abc)
ABCs sao usadas como contratos para a definição 
de novas classes. Elas podem forçar outras classes 
a criarem metodos concretos. Tambem pode ter metodos
concretos por elas mesmas. @abstracmetods sao metodos 
que nao tem corpo. As regras para classes abstratas com
metodos abstratos e que elas NAO PODEM ser instanciadas
diretamente.
Metodos abstratos DEVEM ser implementados nas subclasses
(@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta
E possivel criar @property @setter @classmethod @staticmethod
e @method como abstratos, para isso use @abstractmethods como decorator
mais interno.

Aula 230 - 231

"""

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self,msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('Oi')