from random import randint
from traceback import print_tb

#funciones 

def crearLista():
    lista = []
    for i in range(10):
        lista.append(randint(1,100))
    return lista


lista = crearLista()
print(lista)

lista1 = crearLista()

#copiar listas
myList = lista.copy()   #metodo copy coppia la lista

thisLista = list(lista) #usar el metodo para copiar la lista 
print(thisLista)


#unir listas
#1er forma
joinList = lista + lista1 
print(joinList)
#2da forma
for x in lista1:
  lista.append(x)
print(lista)
#3ra forma 
myList.extend(lista1)
print(lista)



