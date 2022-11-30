

a = int(input('ingresar numero (desde)'))
b = int(input('ingresar segundo numero (hasta)'))
if a>b:
    while(a>b):
        a = int(input('ingresar numero (desde) '))
        b = int(input('ingresar segundo numero (hasta) '))
lista = [x for x in range(a,b) if x % 7 == 0 and x % 5 !=0]
print(lista)