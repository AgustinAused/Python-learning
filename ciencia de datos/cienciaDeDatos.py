#imports
import math
from random import randint


#funciones 

def crearLista():
    valor = int (input('cuantos valores queres que tenga la lista'))
    lista = []
    for i in range(valor):
        num = randint(1,1000)
        lista.append(num)
    return lista


def media(list):
    total = 0
    for i in list:
        total +=i
    resultado = total / len(list)
    return resultado

def varianza(lista,numMedia):
    MEDIA = numMedia
    total = 0 
    resultado = 0 
    
    for i in lista:
        resultado = (i - MEDIA)**2
        total += resultado
        varianza = total / len(lista)
    return varianza 

def lista2(lista,numEstandar,MEDIA):
    listab = []
    for i in lista:
        if(i > (MEDIA - numEstandar)  and i < (MEDIA + numEstandar)):
            listab.append(i)
    return listab
def mediana(lista):
    num = len(lista)
    if (len(lista) % 2 == 0):
        medio =  num / 2
        num1 = lista[int(medio)-1]
        num2 = lista[int(medio)]
        resultado = num1 + num2
        resultado /=2
        return resultado
    else:
        medio = round(len(lista) / 2)
        resultado = lista[medio]
    return resultado  



def main():
    #creamos la lsita de datos a manipular
    lista = crearLista()
    mediaNum = media(lista)
    print('esta es la lista ',lista,'esta es la media ',mediaNum)
    #aca utilizxamos la funcion media que lo que hace es sacar la media de uan lista
    mediaNum =media(lista)
    print('esta es la media',mediaNum)

    #aca sacamos la varianza de la lista
    numVarianza = varianza(lista, mediaNum)
    print('esto es la varianza',numVarianza)

    #aca sacamos la raiz cuadrada de la cvarianza para obtener la desviación estandar
    numVarRaiz= math.sqrt(numVarianza)
    print(numVarRaiz)
    ''' 
    Una desviación estándar baja indica que los valores tienden a estar cerca de la media del conjunto,
    mientras que una desviación estándar alta indica que los valores se distribuyen en un rango más amplio. 
    '''

    # acca lo que hacemos es con la desviación estandar y la media ver que valores estan alli en el medio

    listEstandar =  lista2(lista,numVarRaiz,mediaNum)
    print(listEstandar)


    numMediana = mediana(lista)
    print('numero mediana de la lista',numMediana)

#programa main
main()