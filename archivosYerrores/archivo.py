import os

#manejo de archivo
file = open("hi.txt", "r")
print(file.read()) #imprime el contenido 

print(file.read(5)) #imprime la cantida de de carracterres quese le indique 

print(file.readline())#devulve una linea

for x in file: #imprime line a linea con un loop
    print(x)

file.close() #cerramos el archivo

file = open("hi.txt","a") #se abre el archivo para modificar 
file.write("hi, the writing is modifica") #escribis el archivo
file.close()#cerras el archivos

f = open("hi.txt", "r")#se abre para leer
print(f.read()) #imprimis el archivos

#sobre escribe el archivo
print('hola')
f = open("demofile3.txt", "w") 
f.write("Woops! I have deleted the content!")
f.close()

#imprimis el contenido
f = open("demofile3.txt", "r")
print(f.read())


# crear archivo
f = open("myfile.txt", "x") #se crea un archivo vacio
file = open("hola.txt", "w") #se crea un archivo vacio


#eliminar archivos

if os.path.exists("demonfile.txt"):
  os.remove("demonfile.txt") #esta funcion elimina el archivo del sistema
  os.rmdir("myfolder") #eliminar la carpeta 
  print('ya estan eliminados')
else:
  print("The file does not exist")