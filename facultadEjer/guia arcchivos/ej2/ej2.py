def grabarArm(nombre,file):
    try:
        file.write(f'el nombre es: {nombre}\n')
    except OSError as msg:
        print('error!!'+msg)
        
        


def fun():
    try:
        file = open(r'ej2/nombres.txt','r')
        arm = open(r'ej2/armenia.txt','w')
        esp = open(r'ej2/españa.txt','w')
        ita = open(r'ej2/italia.txt','w')
    except OSError as mgs:
        print('error!!!', mgs)
    else:
        try:
            for i in file:
                cad,cad2= i.split()
                cad=cad.replace(",","")
                if cad[len(cad)-3:len(cad)].upper()=='IAN':
                    grabarArm(cad2,arm)
                else:
                    if cad[len(cad)-3:len(cad)].upper()=='INI':
                        grabarArm(cad2,ita)
                    else:
                        if cad[len(cad)-2:len(cad)].upper()=='EZ':
                            grabarArm(cad2,esp)
        finally:
            file.close()
            arm.close()
            ita.close()
            esp.close()

def main():
    fun()


if __name__ == '__main__':
    main()