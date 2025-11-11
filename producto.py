
class Producto:
    def __init__(self, precio, titulo, autor, eeditorial, año_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = eeditorial
        self.año_edicion = año_edicion
        self.preferencias = preferencias

    def vender(self):
        print(f"Producto {self.titulo} vendido por {self.precio}")
    
    def comprar(self):
        print(f"Comprar {self.titulo} - Precio {self.precio}")
    
    def ver_catalogo(self):
        return "{} - {} = {}".format(self.titulo,self.autor,self.precio)
    