


def repetir (viajes):
    while(viajes > 0):
        viajes = int(input('inrgesar valor correcto'))


def totalGasto(viajes,precio):
    if (viajes <= 20 and viajes >0 ):
        total = precio * viajes
    elif(viajes <= 30 and viajes >20):
        total = (precio * viajes)*0.80
    elif(viajes <= 40 and viajes > 30):
        total = (precio * viajes)*0.70
    
    elif(viajes>  40):
        total = (precio * viajes)*0.60
    else:
        print('la cantida de viajes es incorrecta')
        repetir(viajes)
    return total

def main():
    gastoDeViaje = totalGasto()