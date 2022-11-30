#con methodo

class Argentina:
    def capital(self):
        print('buenos aires')
    def idioma(self):
        print('español argentina')

class Colombia:
    def capital(self):
        print('bogotas')
    def idioma(self):
        print('español')

class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('frances')

colombiano = Colombia()
argentino = Argentina()
frances = Francia()

for pais in (argentino,colombiano,frances):
    pais.capital()
    pais.idioma()