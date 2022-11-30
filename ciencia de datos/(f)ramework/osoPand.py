
import pandas as pd
from random import randint
#funtion


def creaLista(valor):
    lista = []
    for i in range (valor):
        lista.append(randint(1,20))
    return lista


#main program
#convierte una matriz unidimencional en serie(1 en documentacion) 
print('Series')
lista = creaLista(5) #matriz unidimencional
tabla = pd.Series(lista,index=["primero","segundo","tercero","cuarto","quinto"]) 
print(tabla)

print('valor del elemento de la serie anterior',tabla[2])

lista1 ={"dia1":320,"dia2":420,"dia3":540,"dia4":320,"dia5":420,"dia6":540} #diccionario

myVar = pd.Series(lista1)
print(myVar)





#dataframe(2 en documentacion)
print('DataFrame')
mydataset = { #objets
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(myvar.loc[0])
print(myvar.loc[[0,2]])

myvar = pd.DataFrame(mydataset, index=["dia1","dia2","dia3"])
print(myvar)


# leer csv(archivo) en pruebas 
datos = pd.read_csv('ciencia de datos\(f)ramework\data.csv')
print('tabla de datos')
print(datos.to_string())
print('datos')
print(datos.head()) #imprime en consola las ultimas cinto filas 
print(datos.tail()) #imprime en consola las ultimas cinco filas 


print('informacion de la tabla de datos ')
print(datos.info()) # nos muestra informacion importante  



#limpieza de datos// .dropna() o .dropna(inplace = True)  // dataframe["columna"].fillna(valor , inplace = True)
DatosSucios = pd.read_csv('ciencia de datos\(f)ramework\dirtydata.csv') 
# newDatos1 = DatosSucios.dropna() // crea un nuevo dataframe 
# DatosSucios.dropna(inplace = True) // remplaza el dataframe original 
print(DatosSucios.to_string()) #imprime el dataframe
DatosSucios["Calories"].fillna(0, inplace = True)


#para cambiar el formato de una columna es con un data
DatosSucios.dropna(subset=['Date'], inplace = True)
DatosSucios['Date'] = pd.to_datetime(DatosSucios['Date'])
print(DatosSucios.to_string())


#Finding Relationships(relacion de datos)
tablaCorec = DatosSucios.corr()#busca la relacion entre cada calumna

print(tablaCorec)
