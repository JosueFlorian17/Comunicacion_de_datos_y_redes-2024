import networkx as nx
import matplotlib.pyplot as plt
from ipaddress import ip_network

# Ejercicio 1: Introducción a las Redes On-Premises y Corporativas Básicas
def visualize_network():
    G = nx.Graph()

    # Añadir nodos (dispositivos)
    G.add_node("Router")
    G.add_node("Switch 1")
    G.add_node("Switch 2")
    G.add_node("PC 1")
    G.add_node("PC 2")
    G.add_node("PC 3")
    G.add_node("PC 4")

    # Añadir enlaces (conexiones)
    G.add_edges_from([("Router", "Switch 1"), ("Router", "Switch 2"),
                      ("Switch 1", "PC 1"), ("Switch 1", "PC 2"),
                      ("Switch 2", "PC 3"), ("Switch 2", "PC 4")])

    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', font_size=10,
            font_color='black')
    plt.show()

# Ejercicio 2: Direccionamiento IP y CIDR
def calculate_ip_range(cidr):
    network = ip_network(cidr)
    print(f"Rango de direcciones IP para {cidr}:")
    for ip in network.hosts():
        print(ip)

# Ejercicio 3: Redes privadas virtuales (VPCs) y subredes
class VPC:
    def __init__(self, cidr):
        self.cidr = cidr
        self.subnets = []

    def add_subnet(self, cidr):
        subnet = Subnet(cidr)
        self.subnets.append(subnet)

class Subnet:
    def __init__(self, cidr):
        self.cidr = cidr

def create_vpc_and_subnets():
    vpc = VPC('10.0.0.0/16')
    vpc.add_subnet('10.0.1.0/24')
    vpc.add_subnet('10.0.2.0/24')

    print(f"VPC CIDR: {vpc.cidr}")
    for subnet in vpc.subnets:
        print(f"Subred CIDR: {subnet.cidr}")

# Ejecución de los ejercicios
if __name__ == "__main__":
    # Ejecutar Ejercicio 1
    visualize_network()

    # Ejecutar Ejercicio 2
    print("Ejercicio 2: CIDR 192.168.1.0/24")
    calculate_ip_range('192.168.1.0/24')
    print("\nEjercicio 2: CIDR 192.168.1.0/26")
    calculate_ip_range('192.168.1.0/26')

    # Ejecutar Ejercicio 3
    create_vpc_and_subnets()


# EJERCICIO 4 Simulación de un DNS con registros A y CNAME
dns_records = {
  'example.com': '192.168.1.10',
  'www.example.com': 'example.com',
}
def resolve_dns(name):
  if name in dns_records:
    value = dns_records[name]
# Resolver CNAME
    if value in dns_records:
      value = dns_records[value]
    return value

  return None
# Probar la resolución de DNS
print(f"IP de example.com: {resolve_dns('example.com')}")
print(f"IP de www.example.com: {resolve_dns('www.example.com')}")




# EJERCICIO 5
import time
class CDN:
  def __init__(self):
    self.cache = {}
  def get_content(self, url):
    if url in self.cache:
      print("Content served from cache")
      return self.cache[url]
    else:
      content = self.fetch_from_origin(url)
      self.cache[url] = content
      return content
  def fetch_from_origin(self, url):
      print("Fetching content from origin server...")
      time.sleep(2) # Simular tiempo de respuesta del servidor de origen
      return f"Content of {url}"
# Crear una instancia de CDN
cdn = CDN()
# Solicitar contenido
print(cdn.get_content("https://example.com/image.png"))
print(cdn.get_content("https://example.com/image.png"))
