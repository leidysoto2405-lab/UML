
class Revista:
    def __init__(self,categoria):
        self.categoria = categoria
    
    def mostrar_categoria(self):
        return "El libro pertenece a la categoria {}.".format(self.categoria)
    
