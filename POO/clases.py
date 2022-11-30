


#class
class MyClass(): #muy poco usada en la vida real 
    x ='hola, buenos dias'
    edad = 35
    nombre = 'Agustín'
    apellido = 'Aused'

clase = MyClass()
print(clase.nombre)

class Person():
    def __init__(self, name, age): # se ejecuta la funcion init cuando se crea el objeto 
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

persona = Person('Agustin', 18)
print(persona.age)
persona.myfunc()

# methodo del para eliminar del
del persona.age #eliminando propiedades
del persona #eliminado objetos 


class Person:
  def __init__(self, fname, lname): #crea, asigna con la
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, Year):
        Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationYear = Year
        self.graduationMonth = 'march'
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationYear,"and month",self.graduationMonth)


x = Student('Agustin', 'Aused', 2024)
x.welcome()



