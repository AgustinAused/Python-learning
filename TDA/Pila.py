#imports
import abc
from typing import TypeVar

T = TypeVar('T')
class Pila(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apilar(self,object:T) -> None:
        pass
    @abc.abstractmethod
    def desapilar(self,)-> T:
        pass
    @abc.abstractmethod
    def estaVacia(self)->bool:
        pass