
class Libro:
    def __init__(self, genero):
        self.genero = genero

    def mostrar_genero(self):
        return "El libro pertenece al género {}.".format( self.genero)
