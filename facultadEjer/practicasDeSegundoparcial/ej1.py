'''
Construir una función reciba el archivo de cotizaciones y devuelva un diccionario con los datos del archivo por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior y cree un archivo en formato csv con el mínimo, el máximo y la media de dada columna.
'''
import os

def importarArchivo():
    try:
        file = open('practicasDeSegundoparcial\cotizacion.csv','r')
    except OSError as msg:
        print('ERROR!!! hubo un error con el archivo')
        eror = open('Error.txt','w')
        eror.write(str(msg))
        eror.close()
    else:
        try:
            dic = {}
            num = 0
            for i in file:
                num += 1
                conj = i.strip('\n')
                conj = conj.split(';')
                dic.update({f'col {num}': conj}) 
        finally:
            file.close()
            return dic

def crearArchivo(dics):
    try:
        file = open('cotiz.csv','w')
    except OSError as msg:
        print('ERROR!!! hubo un error con el archivo')
        if os.path.exists:
            eror = open('Error.txt','a')
        else:
            eror = open('Error.txt','w')
        eror.write(str(msg))
        eror.close()
    else:
        try:
            for i in range(2,len(dics)):
                value = dics[f'col {i}']
                maximo = float(value[2].replace(',','.'))
                minimo = float(value[3].replace(',','.'))
                media = (maximo + minimo)/2
                file.write(f'{minimo};{maximo};{media}\n')
        finally:
            file.close()

def main():
    diccionario = importarArchivo()
    crearArchivo(diccionario)
if __name__ == '__main__':
    main()
