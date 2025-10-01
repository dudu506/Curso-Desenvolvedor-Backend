#Abstração e polimorfismo

from abc import ABC, abstractmethod
"""
class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass

class Violão(Instrumento):
    def tocar(self):
        return "O violão começou a tocar!"
    
class bateria(Instrumento):
    def tocar(self):
        return "A bateria esta tocando!"        
instrumentos = [Violão(), bateria()]
for  i in instrumentos:
    print(i.tocar())
"""

class funcionario(ABC,):
    @abstractmethod
    def calcular_pg(self):
      pass

class Assalariado(funcionario):
    def calcular_pg(self):
        return f"esse é o seu salario fixo 3500"

class Horista(funcionario):
    def calcular_pg(self,):
        return  "o seu salario é R$13 por hora e durente 9 horas de trabalho seu salario será de R$117"
    
funcionario = [Assalariado(), Horista()]
for i in funcionario:
    print(i.calcular_pg())