'''
Se dispone de un archivo medicamentos.csv que contiene codigo, precio, rubro y  stock de cada uno de los medicamentos.
Los rubros que trabajan son : PEDIATRICO, ODONTOLOGIA , VTALIBRE
El formato de cada registro sera:
CODIGO;PRECIO;RUBRO;STOCK finalizando con un enter o \n
1- Generar el archivo de muestra con 10 registros aproximadamente
2 - Se actualizara de forma masiva el precio en un 25% los medicamentos del rubro VTALIBRE, y se actualizara el archivo en
un nuevo medicamentos_actu.csv
3- Obtener e informar el precio Maximo (Unico) del medicamento del RUBRO ODONTOLOGIA
4- Generar un archivo STOCKBAJO.txt que contenga los codigos de los productos con stock menor a 100 unidades
y la cantidad de stock actual
5- Generar un diccionario con los datos que se obtienen de STOCKBAJO
IMPORTANTE!!!! EL CODIGO DEBERA ESTAR CORRECTAMENTE MODULARIZADO
'''
import os 
def ingresarNum(string):
    while True:
        try:
            num = float(input(f'ingresar {string} del preducto'))
            if num > 0 :
                return num
            continue
        except ValueError:
            print('el valor es incorrecto')
            continue
        except TypeError:
            print('el tipo es incorrecto')
            continue
def valrubro():
    while True:
        string = input(f'ingresar el rubro del producto ')
        if string.upper() == 'PEDIATRICO' or string.upper() =='ODONTOLOGIA' or string.upper() =='VTALIBRE':
            return string.upper()
def validarBand():
    while True:
        string = input('quiere seguir ingresando medicamentos?')
        if string.lower() == 'si' or string.lower()  == 'no':
            if string.lower() == 'no':
                return True
            else:
                return False
def genArchivo():
    try:
        file = open('medicamentos.csv', 'w')
    except OSError:
        print('hubo un error con el archivo')
    else:
        try:
            bandera = False
            while True:
                if bandera:
                    break
                codigo = input('ingresar codigo de producto')
                precio = ingresarNum('precio')
                rubro = valrubro()
                stock = ingresarNum('stock')
                file.write(f'{codigo};{precio};{rubro};{stock} \n')
                bandera = validarBand()
        finally:
            file.close()
def actulizarPrecio():
    try:
        fileActual = open('medicamentos.csv', 'r')
        fileActulizado = open('medicamentos_actu.csv', 'w')
    except OSError:
        print('hubo un error con el archivo')
    else:
        try:
            precioMayor = 0 
            for linea in fileActual:
                tup = linea.strip('\n').split(';')
                if  tup[2] == 'VTALIBRE':
                    precio = float(tup[1])
                    precio *=1.25
                    tup[1]= precio
                if float(tup[1]) > precioMayor:
                    precioMayor = float(tup[1])
                fileActulizado.write(f'{tup[0]};{tup[1]};{tup[2]};{tup[3]}\n')
            print(f'el precio mayor unico que hay en el archivo actualizado es: {precioMayor}')
        finally:
            fileActual.close()
            fileActulizado.close()

def crearStock():
    try:
        fileActual = open('medicamentos.csv', 'r')
        stock = open('STOCKBAJO.txt','w')
    except OSError:
        print('hubo un error con el archivo')
    else:
        try:
            for linea in fileActual:
                elemts =linea.strip('\n').split(';')
                
                if float(elemts[3]) < 100:
                    stock.write(f'{elemts[0]},{elemts[3]}\n')
        finally:
            fileActual.close()
            stock.close()
def geneDiccionario():
    try:
        stock = open('STOCKBAJO.txt', 'r')
    except OSError:
        print('error!!')
    else:
        try:
            dic = {}
            for i in stock:
                cod,cant = i.strip('\n').split(',')
                dic.update({f'{cod}':int(cant)})
            for i in dic:
                print(f'{i}:{dic[i]}')
        finally:
            stock.close()
def main():
    #genArchivo()
    actulizarPrecio()
    crearStock()
    geneDiccionario()


if __name__ == '__main__':
    main()