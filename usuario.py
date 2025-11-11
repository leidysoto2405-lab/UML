#------------------zona de clase-----------------
class Usuario:
    def __init__(self, nombre, apellido, N_cuenta, direccion, login, password):
        
        self.nombre = nombre
        self.apellido = apellido
        self.N_cuenta = N_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self,texto):
        print(f"sugerencia enviada por {self.login}: _ {texto} _")

    def leer(self ):
        print(f"{self.nombre} Esta leyendo...")
    
    def comprar(self):
        print(f"{self.login} realizo una compra...")

    def vender(self):
        print(f"{self.login} puso en venta un producto....")
    
    def realizar_reclamacion(self):
        print(f"Reclamacion de {self.login} sobre el producto: ")
    
