import random

tabla_arp={"MAC1":"192.168.1.1","MAC2":"192.168.1.2","MAC3":"192.168.1.3"}


def traducir(ip_name):
    for mac,ip in tabla_arp.items():
        if ip==ip_name:
            return f"{ip_name} está en la tabla y su dirección MAC asociada es {mac}"
        else:
            print(f"{ip_name} no está en la tabla")
def add(ip_name):
    if ip_name not in tabla_arp.values():
        print(f"Se añadirá el valor {ip_name} a la tabla ARP con una dirección MAC automática")
        tabla_arp[f"MAC{len(tabla_arp)+1}"]=ip_name
        return tabla_arp
    else:
        return("Ya está en la tabla")

def delete(ip_name):
    for mac,ip in tabla_arp.items():
        if ip==ip_name:
            print("Se eliminará la dirección {ip_name}")
            del tabla_arp[mac]
            return tabla_arp
        else:
            return(f"{ip_name} no está en la tabla")
def age():
    for mac,ip in tabla_arp.items():
        stop=random.choice([True,False])
        if stop==True:
            print("Se eliminará la dirección {ip_name} porque no se usa hace mucho tiempo")
            del tabla_arp[mac]
            return tabla_arp
        else:
            pass

print(traducir("192.168.1.1"))
print(add("192.168.1.1"))
print(delete("192.168.1.12"))
print(age())
