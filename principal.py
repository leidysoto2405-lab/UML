
from usuario import Usuario
from producto import Producto
from libro import Libro
from revista import Revista
from articulo_segunda import Articulo_de_segundaMano
from novedades import Novedades
from articulo_online import Articulo_online
from servidor import Servidor
from procesador import Procesador
from indexador import Indexador
from hilo import Hilo
from recolector import Recolector 
from editorial import Editorial


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

print("..............................................................................")

obj_revista = Revista("Para mayores de 15 años")
print(obj_revista.mostrar_categoria())

print("..............................................................................")


obj_segundaMano = Articulo_de_segundaMano("Libro", "Terror_romance", "Alexis")
print(obj_segundaMano.mostrar_articulo_segundamano())

print("..............................................................................")

obj_novedades = Novedades("Romance", "Romance_tragico")
print(obj_novedades.cambiar_clasificacion())

print("..............................................................................")

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

print("..............................................................................")

obj_recolector = Recolector()
a = obj_recolector.enviar_novedades()

print("..............................................................................")

obj_editorial = Editorial("FlorSalvatory", "calle 16", "310 6473674")
print(obj_editorial.vender())

print("........................................................................")

    
