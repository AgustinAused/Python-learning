
class Cliente:
    def __init__(self):
        self.__file = open("ciencia de datos\ejemplos\Libro1.csv")
        self.__fileRead= self.__file.read()
        self.__file.close()

    def getDevolver(self): 
        return self.__fileRead

   
usuario = Cliente()
tabla_de_datos = usuario.getDevolver()

print(tabla_de_datos)










