#funciones del lenguaje 
 

from random import randint


lista = []
for i in range(randint(1,20)):
    lista.append(randint(1,200))
print(lista)
lista.sort()
print(lista)
num = len(lista)
print(num)

