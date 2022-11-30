''' 
  enuciado
============
1. Crear una Clase Producto con los siguientes atributos:
 - codigo
 - nombre
 - precio 
Creale, su constructor, getter y setter y una funcion llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.
'''



class Product:
    pass
    def __init__(self, codigo, nombre, precio ):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    def calcular_total(self,unidades):
        precioTotal = self.__precio * unidades 
        return precioTotal
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    def __str__(self) -> str:
        return 'codigo:' + str(self.__codigo)



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
       return f'este auto es de {self.marca}, modelo {self.modelo} y es un {self.tipo}. tiene {self.ruedas} reudas, {self.puertas} puertas, un motor {self.motor} y es de color {self.color}'

nuevoVehicculo = Auto('porche','911 turbo','supercar', 4,2,'V8 turbo','negro')
print(nuevoVehicculo.descripcion())