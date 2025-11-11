#----------------Zona de clase --------------------
print("--------------------------------------------------")
class Usuario:
    def __init__(self, nombre, apellido, N_cuenta, direccion, login, password):
        
        self.nombre = nombre
        self.apellido = apellido
        self.N_cuenta = N_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self,texto):
        print(f"sugerencia enviada por {self.login}: {texto}")

    def leer(self ):
        print(f"{self.nombre} Esta leyendo...")
    
    def comprar(self):
        print(f"{self.login} realizo una compra...")

    def vender(self):
        print(f"{self.login} puso en venta un producto....")
    
    def realizar_reclamacion(self):
        print(f"Reclamacion de {self.login} sobre el producto: ")
    



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
        return "{} - {}  {}".format(self.titulo,self.autor,self.precio)
    

class Libro:
    def __init__(self, genero):
        self.genero = genero

    def mostrar_genero(self):
        return "El libro pertenece al género {}.".format(self.genero)

class Revista:
    def __init__(self,categoria):
        self.categoria = categoria
    
    def mostrar_categoria(self):
        return "El libro pertenece a la categoria {}.".format(self.categoria)
    
class Articulo_de_segundaMano:
    def __init__(self,clasificacion,tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

    def mostrar_articulo_segundamano(self):
        return"Se a vendido a {} el siguiente articulo de segunda mano: {} - {}".format(self.vendedor, self.tema, self.clasificacion)
    
class Novedades:
    def __init__(self,clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self):
        return"La clasificacion a sido cambiada: Clasificacion anterio {} - nueva clasificacion {} ".format(self.tema,self.clasificacion)
        

class Articulo_online:
    def __init__(self,tema):
        self.tema = tema 

    def publicar(self):
        return"Se a publicado el libro de {} ".format(self.tema)

    

class Servidor:
    def muestra_pagina(self):
        print("Mostrar pagina ")

    def envia_sugerencia(self):
        print ("mostrar sugerencia:")
    
    def  dato_compra(self):
        print("Mostrar datos compra")

    def enviar_datos_venta(self):
        print("Mostrar datos de venta")




    
class Procesador:
    def mandar_datos_de_venta(self):
        print("mandar datos de venta del producto")

    def mandar_artticulo(self):
        print("mandar articulo ")

    def realizar_pago(self):
        print("procesar pago")

    def realizar_cobro(self):
        print("realizar cobro")

    def enviar_datos_de_compra(self):
        print("enviar datos de compra")

    def realizar_busqueda(self):
        print("realizar busqueda")


class Indexador:
    def actualizar_almacen(self):
        print("Se an actualizado los almacenes.....")

    def enviar_resultado_busqueda(self):
        print("Se a enviado el resultado de la busqueda....")



class Hilo:
    def buscar_novedades(self):
        print("Se estan buscando las mas recientes novedades")


class Recolector:
    def enviar_novedades(self):
        print("Se an enviado las mas recientes novedades")


class Editorial:
    def __init__(self,nombre,direccion,telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        return "Se a vendido un producto de la editorial: {} // direccion: {} // Tel: {} ".format(self.nombre, self.direccion, self.telefono)
    
        






#-------------zona de codigo principal----------------------

print("............................................................................")

obj_usuario = Usuario( "Leidy" , "Soto",   89848 ,  " calle 6 ", "Leidydy", "PMt45" )

a = obj_usuario.enviar_sugerencia("Podrian mejorar la entrada de libros...")
b = obj_usuario.leer()
c = obj_usuario.vender()
d = obj_usuario.realizar_reclamacion()
e = obj_usuario.comprar()

print("..............................................................................")

obj_producto = Producto("26.000", "Puente hacia el infinito", "Richard bach", "FlorSalvadory", 1892, "Romance_Aventura")

a = obj_producto.vender()
b = obj_producto.comprar()
c = obj_producto.ver_catalogo()
print(obj_producto.ver_catalogo())
print("..............................................................................")

obj_libro = Libro("Romance_aventura")
print(obj_libro.mostrar_genero())

obj_revista = Revista("Para mayores de 15 años")
print(obj_revista.mostrar_categoria())

obj_segundaMano = Articulo_de_segundaMano("Libro", "Terror_romance", "Alexis")
print(obj_segundaMano.mostrar_articulo_segundamano())

obj_novedades = Novedades("Romance", "Romance_tragico")
print(obj_novedades.cambiar_clasificacion())

obj_articulo_online = Articulo_online("filosofia e historia")
print(obj_articulo_online.publicar())

print("..............................................................................")

obj_servidor = Servidor()

a = obj_servidor.muestra_pagina()
b = obj_servidor.envia_sugerencia()
c = obj_servidor.dato_compra()
d = obj_servidor.enviar_datos_venta()


print("..............................................................................")

obj_procesador = Procesador()

a = obj_procesador.mandar_datos_de_venta()
b = obj_procesador.mandar_artticulo()
c = obj_procesador.realizar_pago()
d = obj_procesador.realizar_cobro()
e = obj_procesador.enviar_datos_de_compra()
f = obj_procesador.realizar_busqueda()
print("..............................................................................")

obj_indexador = Indexador()

a = obj_indexador.actualizar_almacen()
b = obj_indexador.enviar_resultado_busqueda()

print("..............................................................................")

obj_hilo = Hilo()
a = obj_hilo.buscar_novedades()

obj_recolector = Recolector()
a = obj_recolector.enviar_novedades()

obj_editorial = Editorial("FlorSalvatory", "calle 16", "310 6473674")
print(obj_editorial.vender())

print("........................................................................")

    