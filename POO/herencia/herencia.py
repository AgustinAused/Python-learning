#clase
class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        pass
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre,self.tipo)

class Pikachu(Pokemon):
    def ataque(self, tipoAtaque):
        return '{} tienen un tipo de ataque {}'.format(self.nombre,tipoAtaque)

class Chermander(Pokemon):
    def ataque(self, tipoAtaque):
        return '{} tienen un tipo de ataque {}'.format(self.nombre,tipoAtaque)
    



nuevoPokemon = Pikachu('Agustin', 'acuatico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('explosivo'))
NuevoChermander = Chermander('Nijuashu', 'electrico')
print(NuevoChermander.descripcion())
print(NuevoChermander.ataque('en cadena'))