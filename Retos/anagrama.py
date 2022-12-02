'''
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
'''

def anagrama(str1,str2):
    return True if str1 == str2[::-1] else False 
resultado = anagrama('hola','aloh')
print(resultado)
