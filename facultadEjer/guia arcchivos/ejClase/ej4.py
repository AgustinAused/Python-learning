'''
Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones crear el archivo con el listado si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.
El listado debe estar guardado en el archivo de texto listado.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

import os
def validar(n):
    while True:
        if n.lower()=='si' or n.lower() == 'no':
            return n
        n = input('quiere seguir ingresando? si|no')
def escribir(list):
    try:
        file = open('nombYnum.txt','w')
    except OSError:
        print('error con el archivo')
    else:
        try:
            for i in list:
                nom = i[0]
                num= i[1]
                file.write(f'{nom},{num} \n')
        finally:
            file.close()
def crearAgregar():
    try :
        file = 'nombYnum.txt'
        if os.path.isfile(file):
            file = open('nombYnum.txt','a')
        else:
            file = open('nombYnum.txt','w')
    except OSError:
        print('error con el archivo')
    else:
        try:
            band = ''
            while True:
                nombres = []
                if band.lower() == 'no':
                    break
                nombre = input('ingresar nombre')
                num = int(input(f'ingresar el numero de telefono de {nombre}'))
                file.write(f'{nombre},{num}\n')
                band = input('quiere seguir ingresando? si|no')
                validar(band)
        finally:
            file.close()

def consultaTel():
    try:
        file = open('nombYnum.txt','r')
    except OSError:
        print('error con relacion al archivo')
    else:
        try:
            nombre = input('ingresar nombre para la consulta')
            lista = []
            ok = False
            for i in file:
                i = i.strip('\n')
                cad = i.split(',')
                # print(cad)
                if cad[0].lower() == nombre.lower():
                    print(f'el numero de telefono del cliente {cad[0]} es: {cad[1]} ')
        finally:
            file.close()

def consultarEliminar():
    try:
        file = open('nombYnum.txt','r')
    except OSError:
        print('error con relacion al archivo')
    else:
        try:
            nombre = input('ingresar nombre para la consulta')
            lista = []
            ok = False
            for i in file:
                i = i.strip('\n')
                cad = i.split(',')
                if cad[0].lower() == nombre:
                    ok = True
                    continue
                cad = (cad[0],cad[1])
                lista.append(cad)
        finally:
            file.close()
            if ok == True:
                escribir(lista)
            
def main():
    while True:
        print('1)crear archivo\n2)actulizar archivo\n3)eliminar registro\n4)consultar un registro\n0)salir')
        num = input('ingresar opcion')
        if num =='1':
            crearAgregar()
        elif num =='2':
            crearAgregar()
        elif num == '3':
            consultarEliminar()
        elif num == '4':
            consultaTel()
        else:
            break

if __name__== '__main__':
    main()
        
