#import
from random import randint

#funciones
def ordenarBurbuja(lista):
    
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] > lista[j]):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
        
    return lista
        


def ordenarBurbujaDescendente(lista):
    
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] < lista[j]):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
        
    return lista


#programa main
lista = []
num1 = int(input('introducir cuantosnumeros quieres en la lista'))
for i in range (num1):
    lista.append(randint(1,100))
print(lista)
print(ordenarBurbuja(lista))

