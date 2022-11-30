 

class Personas:
    pass
    def __init__(self,nombre,años):
        self.nombre= nombre
        self.años = años
    def description(self):
        return '{} tiene {}'.format(self.nombre,self.años)

    def comentario(self,com):
        return '{} dice:- {}'.format(self.nombre, com)

program = Personas('Agustin',18)
print(program.description())
print(program.comentario('hola, buenos dias. soy un  programdor junior con conocimientos en javaScript,python,html,css,etc. '))



#modificar un atributo 
class Email:
    pass
    def __init__(self) -> None:
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

myCorreo = Email()
myCorreo.enviar_correo()
print(myCorreo.enviado)
