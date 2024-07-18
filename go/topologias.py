class Estrella:
    def __init__(self,nodos):
        self.nodos=nodos
        self.principal=None
        self.principal_conectados={}
    def conectar(self,principal):
        self.principal = principal
        self.principal_conectados={self.principal:[]}
        for i in self.nodos:
            if i!=self.principal:
                print("nodo",i,"conectado a",self.principal)
                self.principal_conectados[self.principal].append(i)

        print(self.principal_conectados)
    def enviar_mensaje(self,mensaje):
        for x in self.principal_conectados[self.principal]:
            print(x,"recibió el mensaje",mensaje)
        



class Malla:
    def __init__(self,nodos):
        self.nodos=nodos
        self.conectados={nodo: [] for nodo in nodos}

    def conectar(self):
        for i in self.nodos:
            for j in self.nodos:
                if i != j:
                    self.conectados[i].append(j)
        print(self.conectados)

    def enviar_mensaje(self,mensaje):
        for nodo in self.nodos:
            for x in self.conectados[nodo]:
                print(x,"recibió el mensaje",mensaje)

            

class Bus:
    def __init__(self,linea,nodos):
        self.linea=linea
        self.nodos=nodos
        self.conectados={linea:[]}

    def conectar(self):
        for i in self.nodos:
            print(f"{i} conectado a linea {self.linea}")
            self.conectados[self.linea].append(i)

        print(self.conectados)

    def enviar_mensaje(self,mensaje):
        for men in self.conectados[self.linea]:
            print(f"{men} recibió el mensaje {mensaje}")




class Anillo:
    def __init__(self, nodos):
        self.nodos = nodos
        self.conectados = {nodo: [] for nodo in nodos}
        self.nodo_inicial = None

    def conectar(self, nodo_inicial):
        self.nodo_inicial = nodo_inicial
        num_nodos = len(self.nodos)
        for i in range(num_nodos):
            nodo_actual = self.nodos[i]
            nodo_siguiente = self.nodos[(i + 1) % num_nodos]
            self.conectados[nodo_actual].append(nodo_siguiente)
        print(self.conectados)

    def enviar_mensaje(self, mensaje):
        for nodo in self.nodos:
            for conectado in self.conectados[nodo]:
                print(f"Nodo {conectado} recibió el mensaje: {mensaje}")




print("Ingrese la topología que desea crear\n1 = Estrella\n2 = Malla\n3 = Bus\n4 = Anillo\nquit = salir\n")
while True:
    answer=input()
    if answer==str(1):

        topo=Estrella([1,2,3,4,5,6,7,8])
        topo.conectar(input(f"Ingrese el nodo central ({topo.nodos}): "))
        topo.enviar_mensaje(input("Escriba el mensaje: "))
        break
    if answer==str(2):
        topo=Malla([1,2,3,4,5,6,7,8])
        topo.conectar()    
        topo.enviar_mensaje(input("Escriba el mensaje: "))
        break
    if answer==str(3):
        topo=Bus(input("Ingrese el nombre de la linea: "),[1,2,3,4,5,6,7,8])
        topo.conectar()
        topo.enviar_mensaje(input("Escriba el mensaje: "))
        break
    if answer==str(4):
        topo = Anillo([1, 2, 3, 4, 5, 6, 7, 8])
        topo.conectar(1)
        topo.enviar_mensaje(input("Escriba el mensaje: "))
        break
    if answer=="quit":
        print("Saliendo...")
        break
    else:
        print("Comando incorrecto, por favor, ingrese el comando adecuado")
        
    
