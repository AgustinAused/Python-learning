#imports

#function
def ingresar():
    n = int(input("ingresar numero de filas y columnas: "))
    while (n < 0 ):
        n = int(input("ingresar numero de filas y columnas: "))
    return n
def crearMatriz():
    n = ingresar()
    filas = []
    for i in range (n):
        col = []
        for j in range(n):
            num = int(input('ingresar num'))
            col.append(num)
        filas.append(col)
    return filas

def mostrar(filas):
    for i in range(len(filas)):
        for j in range(len(filas[i])):
            print(filas[i][j], end=", ")
        print()

def main():
    filas = crearMatriz()
    mostrar(filas)

# main program 
if __name__ == '__main__':
    main()