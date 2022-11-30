# imports

import numpy as np
from random import randint

# functions
def crearLista(valor):
    lista =[]
    for i in range (valor):
        lista.append(randint(1,200))
    return lista

# main program


#creando matrices con numpy

lista = crearLista(8)

# matriz = np.ndarray(lista) otra forma de hacer una matriz
# print(matriz)

matriz2 =np.array(lista)
print(matriz2)


# la funcion array conviente cualquier objeto en matriz
arr = np.array((1, 2, 3, 4, 5, 6))
print(arr) 
#matrices bidimencionales
bi = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(bi)
#arrays tridimencionales
ar = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(ar)

#le atributo ndim te duevilve la cantidad de dimenciones 
print(arr.ndim)
print(bi.ndim)
print(ar.ndim)


#Access Array Elements

print('aca accedemos a la matriz unidimencional ',arr[1])

print('aca accedemos a la matriz bimencional ',bi[1,0])

print('aca accedemos a la matriz tridimencional ',ar[0,1,2])
#por pasos lista[desde:hasta donde:paso] ej bi[1:3]bi[1:3:2]

print(arr[1:4])
print(arr[-3:-1])
print(arr[1:4:2]) 
print(arr[::2])
#slicing en matrices bi-dimencional
print(bi[1, 1:4])
print(bi[0:2, 2])


#copy() //view()
x = arr.copy() #copia  y no se ve afectado el original 
y = arr.view() #ve y modifica el original 
print(x)
#array join
conjunto =np.concatenate((arr,x)) #unir arrays
conjunto = conjunto.reshape(3,4)
print(conjunto)
