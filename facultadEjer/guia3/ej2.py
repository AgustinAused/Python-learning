from random import randint

def matriz_impar():
    n = randint(4,10)
    matriz = []
    anterior = 0
    for i in range (n):
        col = []
        for j in range(n):
            if (anterior == j ):
                num = 1 + (2*anterior)
                col.append(num)
            else:
                col.append(0)    
        anterior+=1
        matriz.append(col)
    return matriz

def matriz_decendente():
    n = randint(4,10)
    matriz = []
    anterior = n
    num = 3**n
    for i in range (n): 
        col = []
        for j in range(n):
            if (anterior == j+1 ):
                num = num//3
                col.append(num)
            else:
                col.append(0)    
        anterior-=1
        matriz.append(col)
    return matriz


def repetitivo():
    n = 4
    matriz = []
    anterior = 0
    num = n
    for i in range (n): 
        col = []
        for j in range(n):
            if (anterior >j-1 ):
                col.append(num)
            else:
                col.append(0) 
        num-=1  
        anterior+=1
        matriz.append(col)
    return matriz

def repCol():
    n = 4 
    matriz = []
    num = 8
    for i in range(n):
        col=[]
        for j in range(n):
            col.append(num)
        num//=2
        matriz.append(col)
    return matriz


def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="|")
        print()

def main():
    matriz = matriz_impar()
    mostrarMatriz(matriz)
    print()
    matrizDec = matriz_decendente()
    mostrarMatriz(matrizDec)
    print()
    matrizRep = repetitivo()
    mostrarMatriz(matrizRep)
    print()
    matrizCol=repCol()
    mostrarMatriz(matrizCol)

# main program 
if __name__ == '__main__':
    main()