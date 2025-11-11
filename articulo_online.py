
class Articulo_online:
    def __init__(self,tema):
        self.tema = tema 

    def publicar(self):
        return"Se a publicado el libro de {} ".format(self.tema)

    