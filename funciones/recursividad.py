#imports


import random


def factorialRecursivo(n):
    '''Retorna el factorial de n o -1 si es negativo.'''
    if n ==0 or n == 1:
        return 1
    elif n<0:
        return -1
    else:
        return n * factorialRecursivo(n-1)
#  imprime en cosola los factoriales
print(factorialRecursivo(4))

def crearMatriz(n,desde=10,hasta=30):
    '''Crea una matriz cuadrada con desde y hasta valores.'''
    matriz=[]
    
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(desde,hasta))
    return matriz

def contarRecursivo(matriz,valor, f=0):
  if f == len(matriz):
      return 0
  else:
      #recorro toda una fila:
      sumaFila=0
      for c in range(len(matriz[f])):
          if matriz[f][c] == valor:
              sumaFila += 1
      return sumaFila + contarRecursivo(matriz,valor, f+1)

def contarTodoRecursivo(matriz,valor, f=0, c=0):
    if f == len(matriz):
        return 0
    else:
        if c == len(matriz[f]):
            return 0 + contarTodoRecursivo(matriz,valor, f+1)
        else:
            #si corresponde sumo un elemento
            if matriz[f][c] == valor:
                return 1 + contarTodoRecursivo(matriz,valor, f, c+1)
            else:
                return 0 + contarTodoRecursivo(matriz,valor, f, c+1)
        
def main():
    m = crearMatriz(4)
    print("Matriz creada:")
    for fila in m:
        print(*fila)
    valor = int(input("Ingrese el valor a contar:"))
    # print(f'Forma Recursiva {valor} aparece {contarRecursivo(m,valor)}')  // recorre solo una fila 
    print(f'Forma Recursiva {valor} aparece {contarTodoRecursivo(m,valor)}')
    
main()