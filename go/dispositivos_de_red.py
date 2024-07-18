class Switch:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conectados = []

    def conectar(self, dispositivo):
        if dispositivo not in self.conectados:
            self.conectados.append(dispositivo)
            dispositivo.conectados.append(self)
            print(f"Dispositivo {dispositivo.nombre} conectado a {self.nombre}")
        else:
            print(f"Dispositivo {dispositivo.nombre} ya está conectado a {self.nombre}")

    def enviar_mensaje(self, origen, destino, mensaje):
        if destino in [d.nombre for d in self.conectados]:
            print(f"Se envió el mensaje '{mensaje}' desde {origen} a {destino} a través del {self.nombre}")
        else:
            print("El destino no está conectado al switch")

class Hub:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conectados = []

    def conectar(self, dispositivo):
        if dispositivo not in self.conectados:
            self.conectados.append(dispositivo)
            dispositivo.conectados.append(self)
            print(f"Dispositivo {dispositivo.nombre} conectado a {self.nombre}")
        else:
            print(f"Dispositivo {dispositivo.nombre} ya está conectado a {self.nombre}")

    def enviar_mensaje(self, origen, destino, mensaje):
        print(f"{self.nombre} enviando mensaje '{mensaje}' desde {origen} a todos los dispositivos conectados")
        for dispositivo in self.conectados:
            if dispositivo.nombre == destino:
                dispositivo.recibir_mensaje(mensaje, origen)
                return
        print(f"El destino {destino} no está conectado al hub")

class Router:
    def __init__(self, nombre, tabla):
        self.nombre = nombre
        self.tabla = tabla  # {destino_ip: dispositivo_de_red}
        self.conectados = []

    def conectar(self, dispositivo):
        if dispositivo not in self.conectados:
            self.conectados.append(dispositivo)
            dispositivo.conectados.append(self)
            print(f"Dispositivo {dispositivo.nombre} conectado a {self.nombre}")
        else:
            print(f"Dispositivo {dispositivo.nombre} ya está conectado a {self.nombre}")

    def enviar(self, origen_ip, destino_ip, mensaje):
        if destino_ip in self.tabla:
            siguiente_salto = self.tabla[destino_ip]
            print(f"{self.nombre} enviando mensaje '{mensaje}' desde {origen_ip} a {destino_ip} a través de {siguiente_salto.nombre}")
            siguiente_salto.enviar_mensaje(origen_ip, destino_ip, mensaje)
        else:
            print(f"{self.nombre} no tiene una ruta a {destino_ip}")

class Dispositivo:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
        self.conectados = []

    def conectar(self, dispositivo_de_red):
        if self not in dispositivo_de_red.conectados:
            dispositivo_de_red.conectar(self)
        else:
            print(f"Dispositivo {self.nombre} ya está conectado a {dispositivo_de_red.nombre}")

    def recibir_mensaje(self, mensaje, origen):
        print(f"Dispositivo {self.nombre} ha recibido el mensaje '{mensaje}' de {origen}")

# Crear dispositivos de red
hub = Hub("Hub1")
switch = Switch("Switch1")
router = Router("Router1", {})

# Crear dispositivos
pc = Dispositivo("PC", "192.168.1.1")
cel = Dispositivo("Cel", "192.168.1.2")

# Conectar dispositivos al switch
pc.conectar(switch)
cel.conectar(switch)

# Conectar dispositivos al hub
pc.conectar(hub)
cel.conectar(hub)

# Añadir rutas al router
router.tabla = {
    "192.168.1.1": switch,
    "192.168.1.2": hub
}

# Enviar mensajes a través del switch y el hub
switch.enviar_mensaje(pc.nombre, cel.nombre, "Hola desde el Switch")
hub.enviar_mensaje(pc.nombre, cel.nombre, "Hola desde el Hub")

# Enviar mensaje a través del router
router.enviar(pc.ip, cel.ip, "Hola desde el Router")

# Enviar mensaje desde el PC al Cel a través de la red
pc.conectar(router)
router.enviar(pc.ip, cel.ip, "Mensaje de PC a Cel a través del Router")
