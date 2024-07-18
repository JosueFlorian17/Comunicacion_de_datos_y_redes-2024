import random
class Cliente:
    def __init__(self):
        self.estado="Nada"
        self.servidor=None

    def enviar_SYN(self):
        print("Enviando SYN al servidor")
        self.estado="SYN sent"
        self.servidor.recibir_SYN()
        
    def recibir_SYN_ACK(self):
        if self.servidor.estado=="SYN-ACK sent":
            print("Se ha recibido el SYN-ACK desde el servidor")
            self.estado="SYN-ACK received"
            self.enviar_ACK()
        else:
            print("No se ha enviado")

    def enviar_ACK(self):
        print("Enviando ACK")
        self.estado="ACK sent"
        self.servidor.recibir_ACK()

class Server:
    def __init_(self):
        self.estado="Nada"
        self.cliente=None

    def recibir_SYN(self):
        while True:
            exito=random.choice([True,False])
            if exito==True:
                self.estado="SYN received"
                print("Se ha recibido el SYN")
                self.enviar_SYN_ACK()
                break
            else:
                print("no se ha recibido el SYN, reintentando")
            
    def enviar_SYN_ACK(self):
        while True:
            exito=random.choice([True,False])
            if exito==True:
                print("Enviando SYN-ACK")
                self.estado="SYN-ACK sent"
                self.cliente.recibir_SYN_ACK()
                break
            else:
                print("No se ha enviado el SYN-ACK, reintentando")
    def recibir_ACK(self):
        while True:
            exito=random.choice([True,False])
            if exito==True:
                print("ACK recibido, conexión establecida")
                self.estado="Connection established"
                return self.estado
                break
            else:
                print("No se ha recibido el ACK, reintentando")


cliente=Cliente()
server=Server()
cliente.servidor=server
server.cliente=cliente
cliente.enviar_SYN()
