#imports
from random import randint

#functions
def cargarDeNotas():
    legajos = []
    nombreYapellido = []
    parcial1= []
    Parcial2 = []
    seguir = True
    while(seguir == True):
        legajo = int(input('ingresar el numero de legajo del alumno'))
        legajos.append(legajo)
        nombre = input('ingresar el nombre y apellido de '+ str(legajo)+'')
        nombreYapellido.append(nombre)
        nota = int(input('ingresar la nota de; primer parcial'))
        parcial1.append(nota)
        nota = int(input('ingresar la nota del segundo parcial'))
        Parcial2.append(nota)
        pregunta = input('quiere seguir ingresando')
        if (pregunta.lower() == 'no'):
            seguir = False
    return legajos, nombreYapellido, parcial1, Parcial2
def promedio(parcial1, parcial2):
    total = 0
    listaPromedio =[]
    for i in range(len(parcial1)):
        total = parcial1[i] + parcial2[i]
        prom = total / 2
        listaPromedio.append(prom)
    return listaPromedio

def promocion(promedio):
    promo = []
    for i in range(len(promedio)):
        if (promedio[i] >= 7 ):
            promo.append('si')
        else:
            promo.append('no')

    return promo





def ordenarSeleccion(promedio,nombre,notas1,notas2,promocion):
    for i in range(0, len(promedio)-1):
        pos_minimo = i
        for j in range(i+1, len(promedio)):
            if (promedio[j] > promedio[pos_minimo]):
                pos_minimo = j
                if (pos_minimo != i):
                  aux = promedio[pos_minimo]
                  promedio[pos_minimo] = promedio[i]
                  promedio[i] = aux 

                  aux = nombre[pos_minimo]
                  nombre[pos_minimo] = nombre[i]
                  nombre[i] = aux

                  aux = notas1[pos_minimo]
                  notas1[pos_minimo] = notas1[i]
                  notas1[i] = aux

                  aux = notas2[pos_minimo]
                  notas2[pos_minimo] = notas2[i]
                  notas2[i] = aux

                  aux =promocion[pos_minimo]
                  promocion[pos_minimo] = promocion[i]
                  promocion[i] = aux
    return promedio,nombre,notas1,notas2,promocion


def mostrarListas(nombres,nota1,nota2,promedio,promocion):
    for i in range(len(nombres)):
        print(nombres[i],   nota1[i],   nota2[i],   promedio[i],   promocion[i])

def main():
    legajos, nombres, pracial1, parcial2 = cargarDeNotas()
    ListaPromedio = promedio(pracial1, parcial2)
    listaPromocion = promocion(ListaPromedio)
    mostrarListas(nombres, pracial1, parcial2,ListaPromedio,listaPromocion)
    promOrd,nombresOrd,parcial1ORd,parcial2ORd,listaPromocionOrd = ordenarSeleccion(ListaPromedio, nombres, pracial1, parcial2,listaPromocion)
    mostrarListas(nombresOrd, parcial1ORd, parcial2ORd,promOrd,listaPromocionOrd)

#main program

main()

