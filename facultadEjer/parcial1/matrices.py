def matriz(piso,cant):
    return [['X']*cant for i in range(piso)]

def registrarCobro(matriz):
    while True:
        while True:
            numPiso = int(input(f'ingresar el numero de piso es de 1 a 5:\n'))
            if (numPiso >= 1 and numPiso <= 5) or numPiso ==99:
                break
        if numPiso == 99:
            return matriz
        while True:
            numDepa = int(input('ingresar numero de departameto'))
            if numDepa >= 1 and  numDepa <= 15:
                break
        matriz[numPiso-1][numDepa-1] = ' '

def totalRecaudado(matriz):
    total = 0
    for i in matriz:
        for j in i:
            if j == ' ':
                total += 10000
    print(f'el total recaudado es: {total}')

        
def mostrarMatriz(matriz):
    for i in range (len(matriz)):
        print(f'piso {i+1}',end=' ')
        for x in matriz[i]:
            print(f'{x}',end=' | ')
        print()
    
def main():
    matrix = matriz(5,15)
    matrix = registrarCobro(matrix)
    totalRecaudado(matrix)
    mostrarMatriz(matrix)
    
if __name__ == '__main__':
    main()