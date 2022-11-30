"""Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). 
En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). 
Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.""" 

#imports 

#function
def ingresar():#args
    lista = []
    for i in range(3): #encontre una mehorar par l aescalabilidad del progrtma ya que podemos cambiar el argumento para que se ingrese la cantida de valores que el usuario quiera 
        num = int(input('ingresar un numero '))
        while num < 0:
            num = int(input('ingresar un numero,recuerde que tiene que ser positivo '))
        lista.append(num)
    return lista

def mayorEstricto(lista):
    maximo = max(lista)
    anterior = 0
    for x in lista:
        if x == anterior:
            return -1
        if x > anterior:
            anterior = x
    return maximo
    
        
def main():
    lista = ingresar()
    valor = mayorEstricto(lista)
    if (valor == -1):
        print('el mayor estricto no existe')
    print(valor)
#main program
main()