"""Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año).
Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función"""



def ingresarFecha():
    dia = int(input('ingresar dia'))
    mes = int(input('ingresar mes'))
    anio = int(input('ingresar año'))
    return dia, mes, anio

def varifica(num,cant):
    if num > 0 and num <= cant:
        return True
    else:
        return False



def main():
    dia,mes,anio = ingresarFecha()
    print(varifica(dia,31))
    print(varifica(mes,12))
    print(varifica(anio,2022))
    



#main program
main()