#imports


#funciones
import os


def encriptar(a):
    textoFinal = ''
    for letra in texto:
        textoFinal += letra +'x'
    print('el texto fue encriptado')
    return textoFinal
def desEncriptar(a):
    textoFinal = ''
    for letra in texto:
        if letra != 'x':
            textoFinal += letra 
    print('el texto fue desencriptado')
    return textoFinal

if os.path.exists("texto.txt"):

    file = open('texto.txt')
    texto = file.read()
    textoEncriptado = encriptar(texto)
    file.close()

    file = open('texto.txt', 'a')
    file.write(textoEncriptado)
    file.close()


    file = open('texto.txt')
    textoEncriptado = file.read()
    textoDesencriptado = desEncriptar(textoEncriptado)

    file = open('texto.txt', 'a')
    file.write(textoDesencriptado)
    file.close()
else:
    print('no existe')