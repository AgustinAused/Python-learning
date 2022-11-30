
class People:
    def __init__(self):
        self.edad = 30
        self.nombre = 'Agustín'
        self.apellido = ''
        self.tuMujer ='se regala en el mercado'

programador = People()
print('la edad es: ', programador.edad )
print('la edad es: ',getattr(programador,'edad'))
print('el programdor sabe algun lenguaje?',hasattr(programador,'lenguajes'))
print('el nombre del programador es: ', programador.nombre,programador.apellido)
setattr(programador,'apellido', 'Aused') #cambia el valor de una poropiedad
print('el nombre del programador es: ', programador.nombre,programador.apellido)
print(programador.tuMujer)
delattr(People,'tuMujer')#elimina el atributo  
print(programador.tuMujer)