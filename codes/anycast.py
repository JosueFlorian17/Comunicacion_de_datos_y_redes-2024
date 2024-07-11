import random
class AnycastService:
  def __init__(self):
     self.servers = ['192.168.1.1', '192.168.2.1', '192.168.3.1']
  def dijkstra(self,Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev
grafo = {
    '192.168.1.1': {'or': 4},
    '192.168.2.1': {'or': 5},
    '192.168.3.1': {'or': 2},
    'or':   {'192.168.1.1':4,'192.168.2.1':5,'192.168.3.1':2}
    }    
anycast = AnycastService()
s, distancia, previos = anycast.dijkstra(grafo,"or")
print(f"Nearest server for user is {s[1]}")
