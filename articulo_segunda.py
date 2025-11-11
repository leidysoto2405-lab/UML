class Articulo_de_segundaMano:
    def __init__(self,clasificacion,tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

    def mostrar_articulo_segundamano(self):
        return"Se a vendido a {} el siguiente articulo de segunda mano: {} - {}".format(self.vendedor, self.tema, self.clasificacion)
    