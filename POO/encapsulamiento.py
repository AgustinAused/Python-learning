#encaposulamiento

class Cliente:
    def __init__(self) -> None:
        pass
        self.__codigo = 4321
    def getCodigo(self):
        return self.__codigo
    def __cuenta(self):
        print('estas accediendo a la cuenta...')

persona = Cliente()
#objeto._nombreclase__nombre atributo
valor=persona._Cliente__codigo
print(valor)
persona._Cliente__cuenta()