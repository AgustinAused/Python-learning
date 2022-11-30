
#imports 
from random import randint


#funciones



#programa  main

lista = [ randint(1,100) for valor in range(10)]
print(lista)

listaPares = []
 
for valor in lista:
    if (valor % 2 == 0):
        listaPares.append(valor**2)







