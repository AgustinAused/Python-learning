#imports
from random import randint

#funciones
def ordenarInsercion(lista):
    for j in range(1, len(lista)): 
        i = j - 1
        pos_actual = j 
        while (i >= 0):
            if (lista[i] > lista[pos_actual]):
                aux = lista[pos_actual]
                lista[pos_actual] = lista[i]
                lista[i] = aux
                pos_actual = i
            i = i - 1
    return lista

#progrma prinsipal
lista = []
num1 = int(input('introducir cuantosnumeros quieres en la lista'))
for i in range (num1):
    lista.append(randint(1,100))
print(lista)
print(ordenarInsercion(lista))