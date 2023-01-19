


import random


class Pila():
# metodos
    def __init__(self):
        self.pila = []
    def apilar(self, n):
        self.pila.append(n)
    def desapilar(self):
        return self.pila.pop()
    def tope(self):
        return self.pila[-1]
    def pilaVacia(self):
        return len(self.pila) == 0 
    def mostrarPila(self):
        while not self.pilaVacia():
            print(self.tope())
            self.desapilar()
    def ordenarPila(self):
        for i in range(0, len(self.pila)-1):
            for j in range(i+1, len(self.pila)):
                if (self.pila[i] > self.pila[j]):
                    aux = self.pila[j]
                    self.pila[j] = self.pila[i]
                    self.pila[i] = aux
            
        return self.pila
        





pilaNums = Pila()

for i in range(10):
    # num = int(input('ingresar num'))
    # num = random.randint(1,400)
    pilaNums.apilar(random.randint(1,500))

# print(pilaNums.pilaVacia())
# print(pilaNums)
# print(pilaNums.pila)

# pilaNums.mostrarPila()
pilaNums.reemplazar()


