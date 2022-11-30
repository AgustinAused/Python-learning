
def ingresasrDatos():
    listaAfiliados = []
    listaInteres = []
    numAfiliado = int(input('ingresar numero afiliado -1para finalizar '))
    while(numAfiliado ==-1):
        while(numAfliado < 999 or numAfliado > 9999):
            numAfliado = int(input('ingresar numero afiliado '))
        interes = int(input('ingresar porque va(0 urgencia, 1 turno )'))
        while(interes != 1 or interes !=0):
           interes = int(input('ingresar porque va(0 urgencia, 1 turno )')) 
        listaAfiliados.append(numAfliado)
        listaInteres.append(interes)
        numAfiliado = int(input('ingresar numero afiliado -1para finalizar '))
    return listaAfiliados, listaInteres


def busquedaPasiente():
    



def main():
    pacientes,condiciones = ingresasrDatos()
    