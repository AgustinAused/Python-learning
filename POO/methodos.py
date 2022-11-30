

# creamos la class  y luego hacemos un methodo que es una funciuonn dentro de una clase
class Matematica:
    def suma(self,num1,num2): # es un methodo 
        self.n1 = num1
        self.n2 = num2
        total = self.n1 + self.n2
        return total

#llamamos a la clase matematica
sum = Matematica()
resultado = sum.suma(4,5)           #aca llamammos al methodo suma

#imprimos el resultado de la suma
print(resultado)


#otra forma de hacer y buena practica 
class Ropa:
    def __init__(self):
        self.marca = 'Dior'
        self.modelo ='Basic'
        self.color = 'Negro'
        self.talle = 'XL'

pantalon = Ropa()
print(pantalon.marca, pantalon.modelo)




#ejercicio 
class Calculadora:
    def __init__(self, num1, num2):
        self.n1= num1
        self.n2 = num2
    def suma(self):
            total = self.n1 + self.n2
            return total 
    def multi (self):
            total = self.n1 * self.n2
            return total 
    def resta(self):
            total = self.n1 - self.n2
            return total 
    def division(self):
            total = self.n1 / self.n2
            return total 

operation = Calculadora(200,30)
valor1= operation.resta()
valor2= operation.suma()
valor3= operation.multi()
valor4= operation.division()

print('el resultado de la resta es: ',valor1)
print('el resultado de la suma es: ',valor2)
print('el resultado de la multiplicacion es: ',valor3)
print('el resultado de la division es: ',valor4)

