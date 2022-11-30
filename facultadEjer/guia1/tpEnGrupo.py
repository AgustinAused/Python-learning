"""
"""
#import
from random import randint
def ingresar():
    cnt = int(input( 'iungresar cantidad de naranjas'))
    return cnt


def proceso(naranjas):
    PesoMaximo = 500000
    CantNaranjJugo=0
    CantNaranjCajon=0
    CantNaranjSobra=0
    CantCamionLleno=0
    CantCajonLleno=0
    CantCajonSobra=0
    PesoNaranja=0
    PesoCajon=0
    PesoCamion=0
    i=0
    while(naranjas >= i ):
        PesoNaranja = randint(150,350)
        if (PesoNaranja >= 200 and PesoNaranja <= 300 ):
            cnc +=1
            PesoCajon += PesoNaranja
            i += 1
            if (CantNaranjCajon == 100):
                if((PesoCajon+PesoCamion) > PesoMaximo):
                    CantCamionLleno += 1
                    PesoCamion += PesoCajon
                    PesoCajon = 0
                    CantNaranjCajon = 0
                    CantCajonLleno += 1
                    CantCajonSobra += 1
                else:
                    PesoCajon + PesoCamion  
        else:
            CantNaranjJugo +=1
            i += 1





