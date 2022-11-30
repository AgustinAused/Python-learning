'''
Se dispone de un archivo articulos.csv que contiene codigo, descripcion, rubro y precio unitario de cada uno de los
articulos. El formato de cada registro sera:
CODIGO;DESCRIPCION;RUBRO;PRECIO finalizando con un enter o \n

1- Generar el archivo de muestra con 10 registros aproximadamente

2 - Leer los datos de los articulos en la estructura que crea mas conveniente, utilice para esto listas, tuplas y/o diccionarios.
'''
def val(cad):
    while True:
        if cad.lower() =='si'or cad.lower() == 'no':
            return cad 
        cad = input(r'si no quire cargar datos ingrese enter: ')
            
def crearArchivo():
    try:
        file = open(r'practicasDeSegundoparcial\articulos.csv', 'w')
    except OSError as msg:
        print('ERROR!!! hubo un error con el archivo')
    else:
        try:
            while True:
                try:
                    band = input(r'si no quire cargar datos ingrese enter: ')
                    cad = val(band)
                    if cad.lower() == 'no':
                        break
                    codigo = int(input('ingresar codigo de'))
                    nombre = input('ingresar nombre de producto')
                    rubro = input(f'ingresar rubro de {nombre}')
                    precio = int(input('ingresar precio'))
                    file.write(f'{codigo};{nombre};{rubro};{precio}\n')
                except ValueError:
                    print('valor incorrecto registro no guardado')
                    continue
        finally:
            file.close()
        
def leerAchivo():
    try:
        file  = open(r'practicasDeSegundoparcial\articulos.csv', 'r')
    except OSError as msg:
        print(f'ERROR!!! hubo un error con el archivo\n{msg}')
    else:
        try:
            dic = {}
            for i in file :
                cad = i.strip('\n').split(';')
                tup = cad[1::]
                tup = tuple(tup)
                dic.update({f'{cad[0]}': tup})
        finally:
            file.close()
            return dic
def recaudacionTotal(dic):
    '''
    3 - Ademas se dispone de un archivo ventas.txt que contiene codigo de articulo y cantidad de cada una de las ventas.
    Se debera procesar dicho archivo para obtener la recaudacion total por producto que se guardara en un archivo
    recaudacion.txt (CODIGO;RECAUDACION), tambien se debera informar en pantalla el articulo con la mayor recaudacion y
    el monto total de las ventas de todos los articulos'''
    try: 
        file  = open(r'practicasDeSegundoparcial\ventas.csv','r')
        recau = open(r'practicasDeSegundoparcial\recaudacio..txt','w')
    except FileNotFoundError:
        print('el archivo no exite')
    else:
        try:
            ventas = {}
            for linea in file:
                cod,cant = linea.strip('\n').split(';')
                cant = int(cant)
                if cod in ventas:
                    ventas[cod]=ventas[cod]+cant;
                else:
                    ventas[cod]=cant;
            

            totalRecaudado = 0
            maxRecaudado = 0 
            codMax = ''
            for clave in ventas:
                recaudado = 0 
                cantidad = ventas[clave]
                linea = dic[clave]
                precio = linea[2]
                recaudado = float(precio) * int(cantidad)
                recau.write(f'{clave};{recaudado} \n')
                totalRecaudado += recaudado 
                if recaudado > maxRecaudado:
                    maxRecaudado = recaudado
                    codMax = clave
            print(f'el valor preducto con mayor recaudaciones : {codMax} el valor es {maxRecaudado}')   
        except KeyError:
            print('error con el diccionario')
        finally:
            file.close()
            recau.close()
            
def main():
    #crearArchivo()
    dic = leerAchivo()
    recaudacionTotal(dic)

if __name__ == '__main__':
    main()