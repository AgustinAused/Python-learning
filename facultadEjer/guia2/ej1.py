#imports 
from random import randint
#function
def crearLista():
    lista = []
    cant = randint(10,99)
    for i in range(1,cant):
        num = randint(1000,9999)
        lista.append(num)
    return lista
def suamtoria(lista):
    cont = 0
    for i in lista:
        cont +=i
    return cont

def eliminar(lista,n):
    cont= 0
    for i in lista:
        if i == n:
            cont+=1
    for j in range(cont):
        lista.remove(n)

def main():
    lista = crearLista()
    total = suamtoria(lista)
    print(lista)
    print(f'el total es: {total}')
    numero = int(input( 'ingresar numero que quiere eliminar: '))
    eliminar(lista,numero)
    print(lista)


if __name__ == '__main__':
    main()