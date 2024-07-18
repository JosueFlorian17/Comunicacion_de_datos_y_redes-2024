class OSI:
    def __init__(self,mensaje):
        self.mensaje=mensaje

    def fisica(self,mensaje):
        print("se procesó el mensaje en la capa física")
        self.mensaje="phisic_layer["+mensaje+"]"
        print(self.mensaje)
    def datalink(self,mensaje):
        print("se procesó el mensaje en la capa de enlace de datos")
        self.mensaje="data_link_layer["+mensaje+"]"
        self.fisica(self.mensaje)
    def red(self,mensaje):
        print("se procesó el mensaje en la capa de red")
        self.mensaje="network_layer["+mensaje+"]"
        self.datalink(self.mensaje)
    def transporte(self,mensaje):
        print("se procesó el mensaje en la capa de transporte")
        self.mensaje="transport_layer["+mensaje+"]"
        self.red(self.mensaje)
    def sesion(self,mensaje):
        print("se procesó el mensaje en la capa de sesion")
        self.mensaje="session_layer["+mensaje+"]"
        self.transporte(self.mensaje)
    def presentacion(self,mensaje):
        print("se procesó el mensaje en la capa de presentacion")
        self.mensaje="presentation_layer["+mensaje+"]"
        self.sesion(self.mensaje)
    def aplicacion(self,mensaje):
        print("se procesó el mensaje en la capa de aplicación")
        self.mensaje="aplication_layer["+mensaje+"]"
        self.presentacion(self.mensaje)

osi=OSI("mensaje inicial")
osi.aplicacion("mensaje")
