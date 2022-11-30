# polimorfismo con herencia

class Aves:
    def volar(self):
        print('la mayoria de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
       print('las aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('la gallina no puede volar')

objetAve = Aves()
objetAve.volar()#acedemos a la clase prinsipal y a su methodo

nuevo_aguila = Aguila()
nuevo_aguila.volar() #usamos el methodo de la clase agila

nueva_gallina = Gallina()
nueva_gallina.volar() #usamos el methodo de la clase gallina
