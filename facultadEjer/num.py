from random import randint


def mostrarMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end='|')
        print()

def crearMatriz(n=3):
    matriz =[]
    for i in range(n):
        col= []
        for j in range(n):
            num = int(input('ingresar numero'))
            # num = randint(1,50)
            col.append(num)
        matriz.append(col)
    return matriz


def inicializarMatriz(n):
    matriz = []
    for i in range(n):
        col=[]
        for j in range(n):
            col.append(0)
        matriz.append(col)
    return matriz



def mat(n):
    mat = inicializarMatriz(n)
    for i in mat:
        for j in i:
            num = randint(0,n**2)
            while recMatriz(mat,num)!=False:
                num = randint(0,n**2)
            mat[i][j]
     


def recMatriz(matriz,num):
    for i in matriz:
        if (num in i):
            return True          
    return False 
