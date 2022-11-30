#herencia multiple

class Telefono:
    def __init__(self) :
        pass
    def llamar(self):
        print('esta llamando')
    def cortar(self):
        print('se finalizo la llamada')

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('tomando la foto')
    def video(self):
        print('esta grando un video')

class Reproduccion:
    def __init__(self):
        pass
    def reproduccionDeVideo(self):
        print(' esta reproducciendo un video')
    def reproducAudio(self):
        print('reproducciendo un audio')

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        pass
        

movil = Smartphone()
movil.llamar()
movil.fotografia()