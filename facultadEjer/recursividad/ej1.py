def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))


def fibonacci(n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(10))

def numEntero(n):
    if n < 10:
        return 1
    else:
        return 1 + numEntero( n // 10)
    

# print(numEntero(10000))


def convDecimal(n):
    if n == 1:
        return 1
    elif n== 0:
        return 0
    else:
        pass

def sumaNaturalesRecursivo(n):
    '''Suma los N primeros numeros naturales en forma recursiva.'''
    if n < 0:
        return -1
    elif n==0:
        return 0
    else:
        return n + sumaNaturalesRecursivo(n-1)   

def sumarElmentos(matriz,i = 0 ):
    if i == len(matriz):
        return 0
    else:
        return sum(matriz[i]) + sumarElmentos(matriz,i+1)

def mostrarMatriz(matriz,i = 0):
    if i <= len(matriz):
        print()
    else:
        pass


matriz = [[123,123,123,123],[123,123,123,123],[123,123,123,123],[123,123,123,123]]

print(sumarElmentos(matriz))
