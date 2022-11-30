
#imports
import math
import numpy as np


#clases
class Calculadora:
    def __init__(self):
        self.num = [int(input('cuantos numeros quere utilizar en la operacion matematica'))] 
        self.datos = [0 for i in range(self.num)]
    def ingresarDatos(self):
        self.datos = [int(input('ingresar datos: '+ str(i+1)+ '= ')) for i in range(self.num)]

class Operaciones_basicas(Calculadora):
    def __init__(self):
        super.__init__(self)

    def suma(self):
        a,b = self.datos
        sum = a + b
        print('el resultado de la suma es: ', sum)
    
    def resta(self):
        a,b = self.datos
        res = a - b
        print('el resultado de la resta es: ', res)
   

class op_medias(Calculadora):
    def __init__(self):
        super().__init__(self)
        pass
    def division(self):
        a,b = self.datos
        div = a / b
        print('el resultado de la division es: ', div)
    def multi (self):
        a,b = self.datos
        mul = a * b
        print('el resultado de la multiplicacion es: ', mul)
class Raiz(Calculadora):
    def __init__(self):
       super.__init__(self,1) 
    
    def Cuadrada(self):
        a, = self.datos
        print('el resulrtado es:', math.sqrt(a))
    def Cubica(self):
        a, = self.datos
        print('el resulrtado es:',np.cbrt(a))
        
class Potencias(Calculadora):
    def __init__(self):
        super.__init__(self,1)
    def cuadrado(self):
        a, = self.datos
        elevado = a**2
        print("{} elevado a la potencia de 2 es {}".format(a, elevado))

    def cubico(self):
        a = self.datos
        elevado = math.pow(a,3)
        print("{} elevado a la potencia de 3 es {}".format(a, elevado))
    def pot (self,num):
        a, = self.datos
        elevado = math.pow(a,num)
        print("{} elevado a la potencia de {} es {}".format(a,num ,elevado))

    
class Cliente:
    def __init__(self) -> None:
        pass
        self.respuesta = input('que operacin quiere hacer? (suma, suma, resta,multiplicaciondivicion raiz ) ')
    def validadcion(self):
        if self.respuesta.lower() =='suma':
            self.persona = Operaciones_basicas()
            self.persona.suma()
        elif(self.respuesta.lower() =='resta'):
            self.persona.resta()
        elif(self.respuesta.lower() =='multiplicacion'):
            self.persona = op_medias()
            self.persona.multi()
        elif(self.respuesta.lower() =='division'):
            self.persona.division()

objeto = Cliente()
objeto.__init__()
objeto.validadcion()