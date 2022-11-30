from random import randint


def ingresarDatos(minimo,maximo,texto):
    while True:
        # num = int(input(f'ingresar {texto} del alumno'))

        num =randint(minimo,maximo)
        if num >= minimo and num <= maximo:
            return num 
        print('el valor es incorrecto')
def cargaDeAlumnos():
    dnis = []
    notasParcial1 = []
    notasParcial2  = []
    porcentajeAsis = []
    print('----------------- carga de datos de los alumnos -----------------')
    while True:
        # ingreso de datos
        dni =  int(input('ingresar dni'))
        # dni = ingresarDatos(0,99999999,'DNI')
        if dni == 0:
            print('carga realizada con exito!!!!')
            return dnis,notasParcial1,notasParcial2,porcentajeAsis
        nota1 = ingresarDatos(0,10,'nota de parcial 1')
        nota2 = ingresarDatos(0,10,'nota de parcial 2')
        porcentaje = ingresarDatos(0,100, 'porcentaje de asistencia')
        print('fin de carga de alumno')
        
        # guardado de datos en listas 
        dnis.append(dni)
        notasParcial1.append(nota1)
        notasParcial2.append(nota2)
        porcentajeAsis.append(porcentaje)
    
def examenPerfecto(dnis,notas2):
    print('----------------- examenees con 10 -----------------')
    for i in range(len(dnis)):
        if notas2[i] == 10:
            print(f'el alumno  con el DNI {dnis[i]} ha sacado 10 en el segundo parcial')


            
            
    

def condicionAlumno(dnis,notas1,notas2):
    print("----------------- condicion de los alunos en la materia -----------------")
    for i in range(len(dnis)):
        if notas1[i] >= 7 and notas2[i] >= 7:
            print(f'el alumno  con el DNI {dnis[i]} ha promocionado')
        elif(notas1[i] >= 4 and notas2[i] >= 4):
            print(f'el alumno  con el DNI {dnis[i]} ha aprobado')
        elif notas1[i] >= 1 and notas2[i] >= 1:
            print(f'el alumno  con el DNI {dnis[i]} ha desaprobado')
        else:
            print(f'el alumno  con el DNI {dnis[i]} ha desaprobado por estar asute a uno o ambos parciales')

def asistencia(dnis,porcentajes):
    print('----------------- cumplimiento de la asistencia -----------------')
    for i in range(len(dnis)):
        if porcentajes[i] > 75:
            print(f'el alumno con DNI {dnis[i]} no cumple con la asistencia')

def main():
    dnis,notasParci1,notasParci2,porcentajes = cargaDeAlumnos()
    condicionAlumno( dnis,notasParci1,notasParci2)
    asistencia(dnis,porcentajes)
    examenPerfecto(dnis,notasParci2)
    print(porcentajes)
    print(min(porcentajes))




if __name__ =='__main__':
    main()