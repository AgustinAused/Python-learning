# imports
from dataclasses import dataclass
from mymodule import person1
import datetime
import platform as pl
# function
# my.greeting('Agustin')

# objetos//property
valor = person1['name']
print(valor)


#sistema
x = dir(pl)
x = pl.system()
print(x)

#fecha y dia

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

dia = datetime.datetime(2020,7,12) #crea el dia 
print(dia)
print(x.strftime("%x"))

#matematipas integradas
lista =[62,73,12,42,53,523,57,34,24,7.2,11,32,54]
y = min(lista)
b = max(lista)
print(y)
print(b)
