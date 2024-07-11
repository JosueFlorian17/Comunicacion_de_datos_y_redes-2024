#crear clase server
class Server:
  #inicializa las variables
  def __init__(self,cpu_capacity,memory_capacity):
    self.cpu_capacity =cpu_capacity
    self.memory_capacity=memory_capacity
    self.current_load_cpu=0
    self.current_load_memory=0
   
   
  #creo funcion para escalamiento vertical
  def scale_up(self,cpu_ad,mem_ad):
     print("Se está cerrando la instancia...")
     self.cpu_capacity += cpu_ad
     self.memory_capacity += mem_ad
   
   
   
  #Simulo como el servidor maneja las solicitudes en caso de tener recursos disponibles y en caso que no  
  def handle_request(self,cpu_s,memoria_s):
    if self.current_load_cpu + cpu_s <=self.cpu_capacity and self.current_load_memory + memoria_s <= self.memory_capacity :
      self.current_load_cpu += cpu_s  #en caso de tener recursos disponibles para la solicitud se agrega a la memoria y al cpu
      self.current_load_memory += memoria_s
      return True
    else:
      x=50 #capacidades a aumentar a nuestro CPU y MEMORIA
      y=50
      if self.current_load_cpu+x>= cpu_s and self.current_load_memory+y>= memoria_s:
          if self.cpu_capacity + x <=140 and self.memory_capacity+y<=140: #SI NO SUPERAMOS UN LÍMITE DE CAPACIDAD, AÚN ES EFICIENTE USAR UN SOLO EC2, POR LO QUE AUMENTAMOS SU CAPACIDAD
            self.scale_up(x,y) #AUMENTAMOS LA CAPACIDAD
            handle_request(cpu_s,memoria_s)
            return True
          else: # SI LA MEMORIA A AÑADIR ES DEMASIADA, ENTONCES PASAMOS A ESCALADO HORIZONTAL
              return False
      return False  
     
     
  #metodo para definir una representacion de la clase  cuando se usa el print()  
  def __str__(self):
        return f"Server(CPU: {self.cpu_capacity}, Memory: {self.memory_capacity}, Current CPU Load: {self.current_load_cpu}, Current Memory Load: {self.current_load_memory})"  


#clase servercluster donde se almacenas los servidores
class ServerCluster:
  def __init__(self):
    #inicializar la lista de servers
    self.servers=[]
   
  #funcion para agregar servers
  def add_server(self,server):
    self.servers.append(server)
 
  #funcion para eliminar un servidor
  def eliminar_server(self,server):
    self.servers.remove(server)
   
   
  #funcion para distribuir las cargas    
  def distribuir_carga(self,cpu_s,memoria_s):
    for server in self.servers: #verifica los servidores hasta encontrar uno que cumpla con el espacio requerido
      if server.handle_request(cpu_s,memoria_s):
        return server
    return None
   
   
  #genera una cadena cuando se usa print() en una clase de este tipo
  def __str__(self):
        return "\n".join(str(server) for server in self.servers)


#clase de sutoescaler para escalar  cuandos se necesite
class AutoScaler:
  def __init__(self,cluster):
    self.cluster=cluster
   
  #funcion para escalar horizontalmente
  def scale_horizon(self):
    nuevo=Server(100,100)  
    self.cluster.add_server(nuevo)
   
  # funcion para desescalar horizontalmente
  def scale_down(self):
    s_r=self.cluster.servers[-1]
    self.cluster.eliminar_server(s_r)
   
   
  def ajustar(self):
    #genera un promedio  en las capacidades usadas y totales en cpu y memoria
    av_cpu=sum(server.current_load_cpu for server in self.cluster.servers)/sum(server.cpu_capacity for server in self.cluster.servers)
    av_mem=sum(server.current_load_memory for server in self.cluster.servers)/sum(server.memory_capacity for server in self.cluster.servers)
    if av_cpu >0.8 or av_mem >0.8:# si el valor de la diviion es mayor a 0.8 usa el escalado horizontal
      self.scale_horizon()
    elif av_cpu <0.3 or av_mem <0.3:# si el valor de la division es menor a 0.25 se usa el desescalado horizontal
      self.scale_down()

s=Server(100,100) #creamos un server con 100 de capacidad en cpu y ram
print(s)
s.scale_up(40,30) #escalamos verticalmente aumentando la capacidad
print(s)
print("--------------------------------------------------------------------------")
cluster=ServerCluster()
servidor1=Server(140,140)
print(servidor1.current_load_cpu)
servidor2=Server(100,100)
servidor3=Server(100,100)
cluster.add_server(servidor1)
cluster.add_server(servidor2)
cluster.add_server(servidor3)
print(cluster)
print("<---->")
cluster.distribuir_carga(60,60)
cluster.distribuir_carga(60,60)
cluster.distribuir_carga(60,60)
cluster.distribuir_carga(60,60)
print(cluster)
print("<---->")


print("--------------------------------------------------------------------------")

cluster = ServerCluster()
servidor1 = Server(cpu_capacity=100, memory_capacity=100)
cluster.add_server(servidor1)
auto_scaler = AutoScaler(cluster)
requests = [(30, 30), (40, 40), (50, 50), (10, 10)]
for cpu_request, memory_request in requests:
    server = cluster.distribuir_carga(cpu_request, memory_request)
    if server:
        print(f"Carga tomada por {server}")
    else:
        print("Escalando...")
        auto_scaler.scale_horizon()
        cluster.distribuir_carga(cpu_request, memory_request)

    auto_scaler.ajustar()
    print(cluster)
