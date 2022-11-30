#funciones
def crearMatriz():
    but = 9
    fil = 12 
    matriz = []
    for i in  range (fil):
        matriz.append([])
        for j in range(but):
            matriz[i].append('D')
    return  matriz
    

def mostrarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end="|")
        print()

def ingresarDatos(n,param):
    num =int(input(f'ingresar numero de {n}: '))
    while(num > param):
        num =int(input(f'ingresar numero de {n}: '))
    return num 

def buscarReserva(matriz):
    paraMat =[8,6,4,2,1,3,5,7,9]
    fila = ingresarDatos('fila',12)
    butaca =ingresarDatos('butaca',9)
    while fila > 0: 
        butaca =ingresarDatos('butaca',9)
        num = paraMat.index(butaca)
        if 'D'== matriz[fila-1][num]:
            matriz[fila-1][num] = 'R'
            fila = ingresarDatos('fila',12)
            
        else: 
            print('ingresar otros datos porque esta butaca ya esta reservada')
            fila = ingresarDatos('fila',12)


def cantidades(matriz):
    sillasReser = 0
    sillasDisp = 0 
    for i in matriz:
       sillasReser+= i.count("R")
       sillasDisp+=i.count("D")
    return sillasDisp,sillasReser


def main():
    matriz = crearMatriz()
    mostrarMatriz(matriz)
    buscarReserva(matriz)
    mostrarMatriz(matriz)
    disponibles,reservadas = cantidades(matriz)
    print(disponibles,reservadas)

if __name__ == "__main__":
    main()
    