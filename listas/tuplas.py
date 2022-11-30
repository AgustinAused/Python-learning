#imports
from random import randint
from traceback import print_tb


#funciones

def imprimir():
    print('hola')

def main():
    pass
#programa main
#creacion de tuplas 
tutle = ("hola", "juan", "agustin", "jose")
tutle1 = (1,5,2,3,45,74,32,2)
tutle2 = (False,True,True,False)

#cambiar el valor (las tuplas son inmitables) 
y = list(tutle)
y[1] = "tu vieja"
tutleMod = tuple(y)
print(tutleMod)

# agregar elementos a una tupla // tambien por el mismo metodo poder eliminar elementos pero con el methodo remove 
y.append('hola buenos dias ')
tutleMod=tuple(y)
print(tutleMod)

#unir tuplas
tuple3 = tutle + tutleMod 


#eliminar tupla por completmo 
del tutleMod


#desempaquetar tuplas 
(palabra1, palabra2,palabra3,palabra4) = tutle
print(palabra1)
print(palabra2)
print(palabra3)
print(palabra4)


#bucles a traves de tuplas 
for i in tutle1:
    print(i) #imprime el valor de i de la tupla

for j in range (len(tutle2)):
    print(tutle2[j]) #imprime por valor de indice 

joinTuple = tutle + tutle2 #unir tuplas 
print(joinTuple)
multiTuple = tutle * 2 #multiplica tuplas 
print(multiTuple)
if __name__ =='__main__':
    main()