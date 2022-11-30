
def valAltura():
    while True:
        altura = int(input('ingresar altura en cm:\n'))
        if altura > 0:
            return altura

def grabar(lista,lista2):
    try:
        file2 = open('ej1/promedio.txt', 'w')
    except OSError as mgs:
        print('error!!!'+ mgs)
    else:
        try:
            for i in range(len(lista)-1):
                file2.write(f'deporte: {lista[i]}')
                file2.write(f'{lista2[i]}\n')
        finally:
            file2.close()
    
def grabarRangoAltura():
    try:
        file = open('ej1/laltura.txt','w')
    except OSError as mgs:
        print('error!!!'+ mgs)
    else:
        try:
            deporteAnterior= ' '
            while True:
                depeorte = input('ingresar deporte o ingresar no para temrinar: \n')
                deporteMin = depeorte.lower()
                if deporteMin == 'no':
                    file.write('Fin')
                    break
                altura = valAltura()
                if deporteAnterior != deporteMin:
                    file.write(deporteMin + '\n')
                    deporteAnterior = deporteMin
                file.write(f'{str(altura)}\n')
        finally:
            file.close()

def grabrPromedio():
    try:
        file = open('ej1/laltura.txt','r')
    except OSError as mgs:
        print('error!!!', mgs)
    else:
        try:
            deportes = []
            promedios =[]
            promedio = 0
            for i in file:
                numI = i.strip('\n')
                if numI.isdigit() != True:                    
                    deportes.append(i)
                    if promedio != 0:
                        promedios.append(promedio)
                    # file.write(f'el deporte es {i} ')
                    nums = 0
                    sum = 0
                    continue
                sum +=int(i)
                nums += 1
                promedio = sum / nums
            grabar(deportes,promedios)
        finally:
            file.close()

def mostrarMasAlto():
    try:
        file2 = open('ej1/promedio.txt', 'r')
    except OSError as mgs:
        print('error!!!', mgs)
    else:
        try:
            suma = 0
            num = 0
            for i in file2:
                numI = i.strip("\n")
                if numI[0].isdigit() == True:
                    print(numI.isdigit())
                    numeroI = float(numI)
                    suma = suma + numeroI
                    num = num + 1
            promedio = suma / num
            print(promedio)
            listaDep = []
            listaProm = []
            file2.close()
            file2 = open('ej1/promedio.txt', 'r')
            for i in file2:
                numI = i.strip("\n")
                if numI.isdecimal() == True:
                    if float(i) > promedio:
                        listaDep.append(depo)
                        listaProm.append(float(i))
                else:
                    depo = i.strip('\n')          
        finally:
            file2.close()
        for x in range(len(listaDep)):
            print(f'{listaDep[x]} el proemdio es mas que el general es de: {listaProm[x]}')
    
def main():
    # grabarRangoAltura()
    grabrPromedio()
    mostrarMasAlto()

if __name__ == '__main__':
    main()