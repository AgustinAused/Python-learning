from random import randint

#funciones
def busquedaSecuencial(n, lista):
    for i in range (len(lista)):
        if (lista[i] == n):
            print("el elemento se encuenta en la posicion: ", i )

def busquedaSecuencialCentinela(n,lista):
    centinela = False
    i = 0 
    while (centinela == False and i < len(lista)):
        if (lista[i] == n):
            centinela = True
        i += 1
    if (centinela == True):
        print("el valor fue encontrado en la posicion: ", i -1)
    else:
        print("el valor no fue encontrado")

#programa main
