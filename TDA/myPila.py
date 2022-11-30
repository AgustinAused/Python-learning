
from typing import TypeVar
from Pila import Pila


T = TypeVar('T')
class My_pila(Pila):
    def __init__(self) -> None:
        self.pila = list()
    def aplilar(self,object:T)->None:
        self.pila.append(object)
    def desapilar(self)-> T:
        if (len(self.pila) > 0):
            return self.pila.pop()
        else:
            return None
    def estaVacia(self)->bool:
        return len(self.pila) == 0