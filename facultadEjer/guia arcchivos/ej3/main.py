'''
Escribir  un  programa  que  permita  grabar  un  archivo  los  datos  de  lluvia  caída  du-rante un año. Cada línea del archivo se grabará con el siguiente formato:
<dia>;<mes>;<lluvia caída en mm>  por ejemplo  25;5;319
Los  datos  se  generarán  mediante  números  al  azar,  asegurándose  que  las  fechas sean válidas. La cantidad de registros también será un número al azar entre 50 y 200.  Por  último  se  solicita  leer  el  archivo  generado  e  imprimir  un  informe  en  for-mato matricial donde cada columna represente a un mes y cada fila corresponda a los días del mes. Imprimir además el total de lluvia caída en todo el año.
'''

from random import randint

def validar(num, max):
    while True:
        if num > max or num < 0:
            num = randint(0,50)
        

def genArchivo():
    try:
        file = open('lluvias.csv','w')
    except OSError as msg:
        print('ERROR!! ' + msg)
    else:
        try:
            for i in range(randint(50,200)):
                dia = randint(1,50)
                dia = validar()
                mes = randint(1,50)
                
            pass
        except ValueError:
            print('el valor es incorrecto')
        finally:
            file.close()