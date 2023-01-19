'''
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci(n):
    fibo = 0
    while fibo <= 50 :
        print(fibo)
        


def fib():
    for x in range(50):
        if x < 2:
            print(x) 
        else:
            # fn = fn-1 + fn-2
            print((x-1) + (x-2))

fib()