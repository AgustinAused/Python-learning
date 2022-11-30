#imports 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#funciones






#creamos matrices en numpy
x = np.array([1,2,4,3])
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n = np.arange(1,10,1)# hace los mismo qeu un rango pero en una matriz unidimencional
z = n.reshape(3,3)# agaarra una matriz unidimencional y hace una matriz bidimensional
v = a.flatten()#convierte una matriz bidimencional en una unidimencional 
c = a.reshape(9)#convierte una matriz bidimencional en una unidimencional 
print(a.ndim)#cantidad de simenciones ej 2
print(a.size)#cantidad de elementos ej 9
print(a.shape)#tupla con la dimensiones de la matriz ej 3x3
print(z,' con la funcion reshape pero de una matriz uni a bi')#impriemunamatriz de la cantida ingresada
print(c,' con la funcion reshape de bi(2) a uni(1)')#impime una matriz unidimencional 
print(v,' con la funcion flatten de bi(2) a uni(1)')#impime una matriz unidimencional 


#Indexación y corte (indexing and slicing)
print('Indexación y corte (indexing and slicing)')
print(v[0:4])
print(v[-4:])


#condicion
condi = v[(v>3) & (v%2 ==0)]
print(condi)


#operaciones 
suma = v.sum()
minimo = v.min()
maxmimo = v.max()
vCuadrado =v*2
print('suma: ',suma,' minimo: ',minimo,' maximo: ',maxmimo, ' matriz multiplicada por dos: ',vCuadrado)
media =np.mean(v)
mediana = np.median(v)
varianza =np.var(v)
desEstandar =np.std(v)
print('media: ', media,' mediana: ',mediana,' varianza: ',varianza,'desvioacion estandar: ',desEstandar )



#matplotlib
x = np.linspace(0, 20, 100)  
plt.plot(x, np.cos(x))       
plt.show() 


#pandas  


#objeto
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)