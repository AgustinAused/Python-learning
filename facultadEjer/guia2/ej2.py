from random import randint

def crearLista():
    lista  = []
    for i in range(1,50):
        num = randint(1,100)
        lista.append(num)
    return lista

def repetido(lista):
    for i in lista:
        for j in range(i+1, len(lista)):
            if (i == lista[j]):
                return True
    return False

def unicos(lista):
    list2 =[]
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if (lista[i] == lista[j]): 
                list2.append(lista[i])
    for x in list2:
        lista.remove(x)

def main():
    lista = crearLista()
    print(lista)
    valor = repetido(lista)
    print(valor)
    unicos(lista)
    print(lista)

main()