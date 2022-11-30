#methodo super 
class Mamifero:
    def __init__(self):
        print( self.nombre ,'este es un animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self,nombre):
        print('el leon es un animal de cuatro patas')
        self.nombre = nombre
        super().__init__()

nuevoLeon = Leon('firulais')