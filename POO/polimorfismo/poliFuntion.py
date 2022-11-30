#con funcion
class Tomate:
    def tipo(self):
        print('vegettal')
    def color (self):
        print('rojo')
class Manzana:
    def tipo(self):
        print('fruta')
    def color(self):
        print('verde')


def function(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
function(nuevo_tomate)
nueva_manzana = Manzana()
function(nueva_manzana)