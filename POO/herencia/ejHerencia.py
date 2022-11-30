 
import math
import numpy as np
#clase 


class Auto:
    pass
    def __init__(self,marca,modelo,tipo,ruedas,puerta,motor,color):
        self.marca =marca 
        self.modelo = modelo
        self.tipo = tipo 
        self.ruedas = ruedas
        self.puertas = puerta
        self.motor = motor 
        self.color = color 
    def descripcion(self):
       return 'este auto es de {}, modelo {} y es un {}. tiene {} reudas, {} puertas, un motor {} y es de color {}'.format(self.marca,self.modelo,self.tipo,self.ruedas,self.puertas,self.motor,self.color)

nuevoVehicculo = Auto('porche','911 turbo','supercar', 4,2,'V8 turbo','negro')
print(nuevoVehicculo.descripcion())

#eje de video 
class Calculadora:
    def __init__(self,n1):
        self.num = n1 
        self.datos = [0 for i in range(n1)]
    def ingresarDatos(self):
        self.datos = [int(input('ingresar datos: '+ str(i+1)+ '= ')) for i in range(self.num)]

class Operaciones_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        sum = a + b
        print('el resultado de la suma es: ', sum)
    def multi (self):
        a,b = self.datos
        mul = a * b
        print('el resultado de la multiplicacion es: ', mul)
    def resta(self):
        a,b = self.datos
        res = a - b
        print('el resultado de la resta es: ', res)
    def division(self):
        a,b = self.datos
        div = a / b
        print('el resultado de la division es: ', div)

class op_medias(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,4)
        pass

class Raiz(Calculadora):
    def __init__(self,):
       Calculadora.__init__(self,1) 
    
    def Cuadrada(self):
        a, = self.datos
        print('el resulrtado es:', math.sqrt(a))
    def Cubica(self):
        a, = self.datos
        print('el resulrtado es:',np.cbrt(a))
        
class Potencias(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def cuadrado(self):
        a, = self.datos
        elevado = a**2
        print("{} elevado a la potencia 2 es {}".format(a, elevado))

    def cubico(self):
        a = self.datos
        elevado = math.pow(a,3)
        print("{} elevado a la potencia 3 es {}".format(a, elevado))
    
        
#creacion de objetos y imprimir en consola      
#operaciones basicas
op = Operaciones_basicas()
op.ingresarDatos()
op.multi()

valor3 = issubclass(Operaciones_basicas,Calculadora) #verifica si la clase es una sub clase de la segunda clase
print(valor3)

#raices
raices = Raiz()
raices.ingresarDatos()
raices.Cuadrada()
raices.Cubica()
valor = isinstance(raices,Operaciones_basicas) #verifica la herencia y devuelve un dato boolean
valor1 = isinstance(op,Operaciones_basicas) #verifica la herencia y devuelve un dato boolean
print('pertenece a la clase operaciones basica? ',valor)
print('pertenece a la clase operaciones basica? ',valor1)



#potencias
op_potencia = Potencias()
op_potencia.ingresarDatos()
op_potencia.cuadrado()


