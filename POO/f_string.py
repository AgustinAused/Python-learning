

# % .format
nombre = 'Agustin'
curso= "python"
horas = 19
print("tutoriales de % s en % s horas"%(curso,horas))

print("tutoriales de {} en {} horas".format(curso, horas))

#f-string
frase = f'hola buenos dia. me llamo {nombre} y soy progrmador en {curso}, tengo {horas} años'
print(frase)
class Student:
    def __init__(self,nombre,apellido, edad, lenguaje):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.lenguaje = lenguaje
    def __repr__(self) :
        frase = f'mi nombre es {self.nombre} { self.apellido} , tengo {self.edad}. soy programador en {self.lenguaje} '
        return frase

newStudent = Student('Agustin','Aused',19, "python")
nS = newStudent.__str__()
print(f'{newStudent !r}')