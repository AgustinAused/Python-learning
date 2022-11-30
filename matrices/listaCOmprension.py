#imports
from random import randint

#functios
# def  crearListas():
#     lista = []
# 10    for 

def crearMatriz():
    filas = int(input('ingresar canitdad de filas '))
    columnas = int(input('ingresar cantidad de columnas '))
    Matriz = []
    for i in range (filas):
        Matriz.append([])
        for j in range (columnas):
            numero = randint(1,100)
            while(numero%2 !=0):
                numero = randint(1,100)
            Matriz[i].append(numero)
    return Matriz  

def matrizCuadrada(matriz):
    for i in matriz:
        print( i) 
def main():
    matriz = crearMatriz()
    print(matriz)
    matrizCuadrada(matriz)
    print(matriz[1][2])



#programa main 
main()