#propiedades()




class Empleados:
    def __init__(self,nombre,salario,edad):
        self.__nombre = nombre
        self.__salario = salario
        self.__edad = edad
    def __getnombre(self):
        return self.__nombre
    def __setnombre(self , nombre):
        self.__nombre = nombre
    def __delNombre(self):
        del self.__nombre

    
    def __getsalario(self):
        return self.__salario
    def __setsalario(self,salario):
        self.__salario = salario
    def __delsalario(self):
        del self.__salario
    
    def __getedad(self):
        return self.__edad
    def __setedad(self, edad):
        self.__edad = edad
    def __deledad(self):
        del self.__edad

    nombre = property(  fget=__getnombre,
                        fset=__setnombre,
                        fdel=__delNombre,
                        doc="soy la propiedda del nombre" )
    salario = property(  fget=__getsalario,
                        fset=__setsalario,
                        fdel=__delsalario,
                        doc="soy la propiedda del salario")
    edad = property(     fget=__getedad,
                        fset=__setedad,
                        fdel=__deledad,
                        doc="soy la propiedda de la edad" )
    
empleado1 = Empleados('agustin',200,34)
emNombre = empleado1.nombre = 'cacho'
emEdad = empleado1.edad
emSalario = empleado1.salario

print(f'el nombre del empleado es {emNombre}, tiene {emEdad} y por año cobra aproximadamente {emSalario} mil euros ')

