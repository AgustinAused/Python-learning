#import
from random import randint

#funcion
def ordenarSeleccion(lista):
    for i in range(0, len(lista)-1):
        pos_minimo = i
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[pos_minimo]):
                pos_minimo = j
                if (pos_minimo != i):
                  aux = lista[pos_minimo]
                  lista[pos_minimo] = lista[i]
                  lista[i] = aux
    return lista
#programa main
lista = []
num1 = int(input('introducir cuantosnumeros quieres en la lista'))
for i in range (num1):
    lista.append(randint(1,100))
print(lista)
print(ordenarSeleccion(lista))