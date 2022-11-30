# clases 
import math


class Pastel:
    def __init__(self,ingredientes):
        pass
        self.ingredientes = ingredientes
    def __repr__(self):
        pass
        return f'pastel({self.ingredientes !r})'
    
    @classmethod
    def pastelChoco(cls):
        return cls(['harina', 'leche', 'chocolate','azucar'])
    @classmethod
    def pastelVainilla(cls):
        return cls(['harina', 'leche', 'vainilla','azucar'])

pastelChoco = Pastel.pastelChoco()
print(pastelChoco)

pastelVai = Pastel.pastelVainilla()
print(pastelVai)


#metodos estaticos

class Auto:
    def __init__(self,marca,tamaño):
        pass
        self.marca = marca 
        self.tamaño = tamaño 
    def __repr__(self):
        pass
        return (f'auto ({self.marca},'f'{self.tamaño})')
    def año(self):
        return self.tamaño_año(self.tamaño)
    
    
    @staticmethod 
    def tamaño_año(tamaño):
        return tamaño ** 2 / math.pi

nuevoAuto = Auto('Porche',2.45)
print('el tamañó',nuevoAuto.tamaño)
print('el la marca',nuevoAuto.marca)

tamañoAuto = nuevoAuto.tamaño_año(4)
print('el tamaño de el auto con laoperacion',tamañoAuto)
