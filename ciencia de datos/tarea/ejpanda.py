# imports

import  pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#functicon

#main program 


DATOS = pd.read_csv('ciencia de datos\(f)ramework\dirtydata.csv') #leeamos la tabla de datos 
#eliminamos lo datos nulos en la columna calorias 
newDatos = DATOS["Calories"].dropna()
#columna de Calories
mode = newDatos.mode()[0] #buscamos el valor que mas aparece y lo guradamos en un variable 

DATOS["Calories"].fillna(mode,inplace = True) #insertamos el valor de la variable cada vex que aparezca un dato null en la columna de colorias

#columna de Duration
DATOS.loc[7,'Duration'] = 45

#columna de Date
DATOS['Date'] = pd.to_datetime(DATOS['Date']) #le damos a todos lpoo datso en la columna Date el formato Time

DATOS.dropna(subset=['Date'], inplace = True) # eliminamos lo datos nulos en el date 

#datos a sacar //
#sacar los duplicados con el metodo 
DATOS.duplicated()#busca el duplicado 
DATOS.drop_duplicates(inplace=True)#elimina los duplicados

#correlacion entre las columnas para luego graficar 
correlacion = DATOS.corr()
print(correlacion)

print(DATOS.to_string()) # mostramos en la salida la lista modificada

DATOS.plot()

plt.show() 