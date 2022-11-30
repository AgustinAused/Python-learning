#polimorfismo

class Animales:
    def  __init__(self,nombre) -> None:
        pass
        self.nombre = nombre
    def tipoDeAnoimal(self):
        pass
class Leon(Animales):
    def tipoDeAnimal(self):
        print(f'{self.nombre} animal salvaje')

class Perro(Animales):
    def tipoDeAnimal(self):
        print(f'{self.nombre} animal domestico')

nuevoAnimal = Leon('firulais')
nuevoAnimal.tipoDeAnoimal()

nuevoAnimal2 = Perro('bolt')
nuevoAnimal2.tipoDeAnoimal()

#polimorfismo con funcion 

