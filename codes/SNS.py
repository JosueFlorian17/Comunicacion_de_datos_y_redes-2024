import random
import time
import queue


# Trabajamos con un servicio de notificación A2P
class NotificationSystem:
    def __init__(self):
      self.topics={}
      self.subscriptions={}

    def crear_topic(self,topic):
      if topic not in self.topics:
        self.topics[topic]=queue.PriorityQueue() # validamos que el tema sea nuevo y lo añadimos con una lista de prioridad

    def suscribir(self,topic,suscriptor):
      if topic not in self.subscriptions:
        self.subscriptions[topic]=[]
      self.subscriptions[topic].append(suscriptor)
      # verificamos que el suscriptor no esté en el tema anteriormente, si es así creamos una lista vacía e introducimos al suscriptor a dicha lista

    def publicar(self, topic,mensaje,prioridad=1):
      if topic in self.topics:
        self.topics[topic].put((prioridad,mensaje)) # añadimos el mensaje a la lista de prioridad


    def procesamiento(self,topic,max_intentos=3):
      if topic in self.topics and topic in self.subscriptions: #verificamos que que el tema exista y tenga suscriptores
        while not self.topics[topic].empty(): #siempre que no esté vacío
          prioridad, mensaje= self.topics[topic].get()
          for suscriptor in self.subscriptions[topic]:#para cada suscriptor del tema
            exito= self.notificar(suscriptor,mensaje,max_intentos) #realizaremos el intento de notificar
            if not exito: #si falla
              print("Ha fallado el envío del mensaje a",suscriptor,"después de",max_intentos,"intentos")

    def notificar(self,suscriptor,mensaje,max_intentos):
      intentos=0
      while intentos<max_intentos: # hasta un máximo de intentos
        intentos+=1
        if suscriptor.enviar(mensaje):
          print("Mensaje enviado a",suscriptor,"en el intento numero",intentos,": ","\t",'"',mensaje,'"')

          return True
          time.sleep(1) #tiempo de espera para envio de un nuevo mensaje
      return False

class EmailEndpoint:
  def __init__(self,correo):
    self.correo=correo

  def enviar(self,mensaje):
    if random.random()<0.8: # simulamos la posibilidad de que el envío del mensaje falle
      return True
    else:
      return False

  def __str__(self):
    return f"Email({self.correo})"

class SMSEndpoint:
  def __init__(self,telefono):
    self.telefono=telefono

  def enviar(self,mensaje):
    if random.random()<0.7:# simulamos la posibilidad de que el envío del mensaje falle
      return True
    else:
      return False

  def __str__(self):
    return f"SMS({self.telefono})"

class WebhookEndpoint:
  def __init__(self,url):
    self.url=url

  def enviar(self,mensaje):
    if random.random()<0.9:# simulamos la posibilidad de que el envío del mensaje falle
      return True
    else:
      return False

  def __str__(self):
    return f"Webhook({self.url})"


notification_system = NotificationSystem()
notification_system.crear_topic("circulares_cayetano")

email_endpoint = EmailEndpoint("test@upch.pe")
sms_endpoint = SMSEndpoint("904376308")
webhook_endpoint = WebhookEndpoint("http://blackboard.com/webhook")

notification_system.suscribir("circulares_cayetano", email_endpoint)
notification_system.suscribir("circulares_cayetano", sms_endpoint)
notification_system.suscribir("circulares_cayetano", webhook_endpoint)

notification_system.publicar("circulares_cayetano", "Se acaban circulares_cayetano!", prioridad=2)
notification_system.publicar("circulares_cayetano", "Participe de la votación del comité electoral", prioridad=4)

notification_system.procesamiento("circulares_cayetano")
