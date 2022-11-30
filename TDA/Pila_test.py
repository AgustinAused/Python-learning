from pila import Pila
from myPila import My_pila


unaPila : Pila= My_pila()
unaPila.apilar(3)
unaPila.apilar(1)
unaPila.apilar(4)
unaPila.apilar(6)
unaPila.apilar(35)
unaPila.apilar(28)


for numero in [28,35,6,4,1,3]:
    topeActual = unaPila.desapilar()
    print(f'el valor actual es: {topeActual}')
    assert topeActual == numero 

assert unaPila.estaVacia(0)