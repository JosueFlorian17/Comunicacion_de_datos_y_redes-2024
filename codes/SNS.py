import random
import time

# Trabajamos con un servicio de notificación A2P
class NotificationSystem:
    def __init__(self):
        self.topics={}
        self.subscriptions={}

    def crear_topic(self,topic):
        if topic not in self.topics:
            self.topics[topic]=[]  # Utilizamos una lista simple en lugar de una cola de prioridad

    def suscribir(self,topic,suscriptor):
        if topic not in self.subscriptions:
            self.subscriptions[topic]=[]
        self.subscriptions[topic].append(suscriptor)

    def publicar(self,topic,mensaje):
        if topic in self.topics:
            self.topics[topic].append(mensaje)  # Añadimos el mensaje a la lista

    def procesamiento(self,topic,max_intentos=3):
        if topic in self.topics and topic in self.subscriptions:
            while self.topics[topic]:  # Mientras la lista no esté vacía
                mensaje=self.topics[topic].pop(0)  # Sacamos el primer mensaje de la lista
                for suscriptor in self.subscriptions[topic]:
                    exito=self.notificar(suscriptor,mensaje,max_intentos)
                    if not exito:
                        print("Ha fallado el envío del mensaje a",suscriptor,"después de",max_intentos,"intentos")

    def notificar(self,suscriptor,mensaje,max_intentos):
        intentos=0
        while intentos<max_intentos:
            intentos += 1
            if suscriptor.enviar(mensaje):
                print("Mensaje enviado a",suscriptor,"en el intento número",intentos,":","\t",'"',mensaje,'"')
                return True
            time.sleep(1)  # Tiempo de espera para el próximo intento
        return False

class EmailEndpoint:
    def __init__(self,correo):
        self.correo=correo

    def enviar(self,mensaje):
        return random.random()<0.8  # Simulamos la posibilidad de que el envío del mensaje falle

    def __str__(self):
        return f"Email({self.correo})"

class SMSEndpoint:
    def __init__(self,telefono):
        self.telefono=telefono

    def enviar(self,mensaje):
        return random.random()<0.7  # Simulamos la posibilidad de que el envío del mensaje falle

    def __str__(self):
        return f"SMS({self.telefono})"

class WebhookEndpoint:
    def __init__(self,url):
        self.url=url

    def enviar(self,mensaje):
        return random.random()<0.9  # Simulamos la posibilidad de que el envío del mensaje falle

    def __str__(self):
        return f"Webhook({self.url})"

# Ejemplo de uso
notification_system=NotificationSystem()
notification_system.crear_topic("circulares_cayetano")

email_endpoint=EmailEndpoint("test@upch.pe")
sms_endpoint=SMSEndpoint("904376308")
webhook_endpoint=WebhookEndpoint("http://blackboard.com/webhook")

notification_system.suscribir("circulares_cayetano",email_endpoint)
notification_system.suscribir("circulares_cayetano",sms_endpoint)
notification_system.suscribir("circulares_cayetano",webhook_endpoint)

notification_system.publicar("circulares_cayetano","¡Se acaban las circulares!")
notification_system.publicar("circulares_cayetano","Participe de la votación del comité electoral")

notification_system.procesamiento("circulares_cayetano")
