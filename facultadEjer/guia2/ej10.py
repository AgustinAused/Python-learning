
from random import randint
def crear():
    lista = [randint(1,100) for x in range(100) ]
    return lista

def impar(lista):
    listaImpar = [x for x in lista if x % 2!=0]
    print(listaImpar)


lista = crear()
impar(lista)