'''
1 ingresar una frase 
2 imprimir un listado ordenado
3 eliminar las repetidas 
4 sumar cantidad des veces
'''

def crearDic():
    frase = input('ingresar frase')
    palabras = frase.split()
    dic  = {}
    for palabra in palabras:
        if palabra not in dic:
            dic[palabra] = 1
        else:
            dic[palabra] += 1
    print(dic)
    claves = list(dic)
    print(claves)
    claves.sort()
    for clave in claves:
        print(clave ,'aparece :',dic[clave],' veces')

def main():
    crearDic()


if __name__ == '__main__':
    main()