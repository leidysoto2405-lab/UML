
class Editorial:
    def __init__(self,nombre,direccion,telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        return "Se a vendido un producto de la editorial: {} // direccion: {} // Tel: {} ".format(self.nombre, self.direccion, self.telefono)
    