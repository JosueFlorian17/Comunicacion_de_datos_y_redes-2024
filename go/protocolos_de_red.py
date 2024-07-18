import random
class UDP:
    def __init__(self,paquetes):
        self.paquetes=paquetes

    def enviar(self):
        recibidos=[]
        for i in self.paquetes:
            exito=random.choice([True,False])
            envio=exito
            if envio==True:
                print("se envió el paquete")
                recibidos.append(i)
            else:
                print("no se envió el paquete")

        return recibidos
        
    def recibir(self,recibidos):
        print(f"Los mensajes recibidos fueron {recibidos}")


class TCP:
    def __init__(self,paquetes):
        self.paquetes=paquetes

    def enviar(self):
        recibidos = []
        max_reintentos = 3

        for paquete in self.paquetes:
            intentos = 0
            enviado = False
            print(f"Estableciendo conexión para el paquete {paquete}...")

            while intentos < max_reintentos and not enviado:
                exito = random.choice([True, False])
                if exito:
                    print(f"Paquete {paquete} enviado exitosamente.")
                    recibidos.append(paquete)
                    enviado = True
                else:
                    intentos += 1
                    print(f"Fallo al enviar el paquete {paquete}. Reintento {intentos} de {max_reintentos}...")

            if not enviado:
                print(f"No se pudo enviar el paquete {paquete} después de {max_reintentos} reintentos.")

        return recibidos
        
    def recibir(self,recibidos):
        print(f"Los mensajes recibidos fueron {recibidos}")

        
#udp=UDP([1,2,3,4,5,6,7])

#x=udp.enviar()

#udp.recibir(x)

tcp = TCP([1, 2, 3, 4, 5, 6, 7])

tcp.recibir(tcp.enviar())
