import random

tabla_arp={
    '192.168.1.1': '00:1A:2B:3C:4D:5E',
    '192.168.1.2': '00:1A:2B:3C:4D:5F',
    '192.168.1.3': '00:1A:2B:3C:4D:60',
    }


def mostrar_tabla(tabla_arp):
    print("Mostrando tabla")
    for i in tabla_arp.items():
        print(i)

        
def request(tabla,r):
    for i in tabla_arp.keys():
        if r==i:
            print(f"Dirección MAC asociada: {tabla_arp[r]}")
            break

        else:
            print("se añadirá",r,"a la tabla arp")
            add(tabla_arp,r)
            break

def add(tabla,addittion):
    tabla[addittion]="00:1A:2B:3C:4D:61"
    mostrar_tabla(tabla)


def remove(tabla,deletion):
    print("se eliminará el elemento de la tabla arp")
    tabla.pop(deletion)
    mostrar_tabla(tabla)

def aged(tabla):
    #simulamos que se dejo de usar un elemento aleatorio
    x=random.choice(list(tabla_arp.keys()))
    print(f"El elemento {x} dejó de usarse por mucho tiempo y se eliminará")
    remove(tabla,x)


#request(tabla_arp,r="192.168.1.1")
#request(tabla_arp,r="192.168.1.5")
#remove(tabla_arp,"192.168.1.3")
#aged(tabla_arp)
#mostrar_tabla(tabla_arp)

