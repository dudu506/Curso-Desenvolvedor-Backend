#Abstração e polimorfismo

from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def instrumento(self):
        pass

class violão(Instrumento):
    def tocar(self):
        return "O violão começoe a tocar!"
    
class bateria(violão):
    def fazer_som(self):
        return "A bateria esta tocando!"        
instrumentos = [violão(), bateria()]
for t in instrumentos:
    print(t.mover())