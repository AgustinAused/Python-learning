# palabra1 ='neuquen'
# palabra2 = 'hola'

# def verificar(palabra):
#     palabra = palabra.lower()
#     str=''.join(reversed(palabra))
#     if palabra == str:
#         print('es capicua')

# def centrar(palabra):
#     cad = palabra.center(80,'-')
#     print(cad)

# def clave(palabra):
#     val = palabra.isdigit()

#     while val == False:
#         palabra= input()
#         val=palabra.isdigit()
        
#     clave1 =''
#     clave2= ''
#     for i in palabra:
#         num = palabra.index(i)
#         if num % 2 == 0:
#             clave1 +=i 
#         else:
#             clave2+=i
#     return clave1,clave2




# verificar(palabra1)
# centrar(palabra1)
n = input()
# claves = clave(n)
# print(claves)

lista = [a for a in range(len(n)) if a %2!=0]
print(lista)


