
def crearAlumnos():
    try:
        file = open('alumnos.txt','wt')
    except OSError:
        print('hubo problemas con el archivo')
    else:
        try:
            while True:
                legajos = int(input('ingresar numero de legajo'))
                if legajos < 0:
                    break
                nombre = input('ingresar nombre')
                ape = input('ingresar apellido')
                faltas = int(input('ingrear faltas'))
                notaF = int(input('ingresar nota final'))
                file.write(f'{legajos};{nombre} {ape};{faltas};{notaF}\n')
        except ValueError:
            print('ERROR!! el valor no es correcto')            
        finally:
            file.close()

def proceesar():
    try:
        libres = open('ej1\libres.txt','w')
        file = open('alumnos.txt','r')
    except OSError:
        print('hubo problemas con el archivo')
    else:
        try:
            for i in file:
                i = i.strip('\n')
                leg,nom,faltas,notas = i.split(';')
                if faltas > 4:
                    libres.write(f'{leg};{nom};{faltas};{notas} \n')
        finally:
            file.close()
            libres.close()
        



def main():
    crearAlumnos()
    proceesar()