
class Novedades:
    def __init__(self,clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self):
        return"La clasificacion a sido cambiada: Clasificacion anterio: {} - nueva clasificacion: {} ".format(self.tema,self.clasificacion)
        
