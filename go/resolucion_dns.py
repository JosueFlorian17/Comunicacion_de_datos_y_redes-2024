tabla_dns={"192.168.1.1":"google","192.168.1.2":"amazon","192.168.1.3":"youtube"}

def agregar(dns_name):
    for ip,dns in tabla_dns.items():
        if dns_name==dns:
            print("sí existe en la tabla y su IP es",ip)
            return tabla_dns
        else:
            pass
    print("Se añadirá a la tabla de resolución")
    tabla_dns["192.168.1.4"]=dns_name

 

def buscar_dns(dns_name):
    for ip,dns in tabla_dns.items():
        if dns_name==dns:
            print("sí existe en la tabla y su IP es",ip)
            return tabla_dns
        else:
            print("No existe en la tabla, ¿desea ingresarla?")
            si=input()
            if si.lower()=="si" or si.lower()=="sí":
                print("ok")
                agregar(dns_name)
                return tabla_dns
            else:
                print("está bien")

def buscar_ip(ip_name):
    for ip,dns in tabla_dns.items():
        if ip==ip_name:
            print("sí existe en la tabla y su DNS es",dns)
            return tabla_dns
        else:
            pass    
    print("no se encuentra")

print("Indique qué operación desea realizar:\n1 = resolver DNS\n2 = resolver IP")

while True:
    ans=input("")
    if ans==str(1):
        buscar_dns(input("Ingrese el nombre del DNS que busca: "))
        break
    if ans==str(2):
        buscar_ip(input("Ingrese el nombre del IP que busca: "))
        
        break
    else:
        print("Opción inválida, elija una dentro de las opciones que se le ofrecen")
        
