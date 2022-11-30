#imports 
from csv import list_dialects
from random import randint
#funciones
def crearLista():
    lista = []
    valor = int(input('cuantos valores desea insertar en la lista'))
    for i  in range(valor):
        numero = randint(1,100)
        lista.append(numero)
    print(lista)
    return(lista)
def ListaPares(lista):
    listaPar = []
    i = 0
    while (i < len(lista)):
        if (lista[i] %2 ==0):
            listaPar.append(lista[i])
        i +=1
    print(listaPar)
    return listaPar
def ListaImpares(lista):
    listaImpar = []
    i = 0
    while (i < len(lista)):
        if (lista[i] %2 != 0):
            listaImpar.append(lista[i])
        i +=1
    print(listaImpar)
    return listaImpar
    


def main():
    lista = crearLista()
    listaPar = ListaPares(lista)
    ListaImpar = ListaImpares(lista)


#programam main
main()