class Ruta:
    def __init__(self,destino,metrica):
        self.destino=destino
        self.metrica=metrica

class TablaDeEnrutamiento:
    def __init__(self):
        self.rutas=[]

    def agregar_ruta(self,destino,metrica):
        nueva_ruta=Ruta(destino,metrica)
        self.rutas.append(nueva_ruta)

    def encontrar_mejor_ruta(self,destino):
        mejor_ruta=None
        for ruta in self.rutas:
            if ruta.destino==destino:
                if mejor_ruta is None or ruta.metrica<mejor_ruta.metrica:
                    mejor_ruta=ruta
        return mejor_ruta

def main():
    tabla=TablaDeEnrutamiento()
    while True:
        print("1.- Agregar ruta")
        print("2.- Encontrar mejor ruta")
        print("3.- Salir")
        opcion=int(input("Elige una opción: "))
        if opcion == 1:
            destino = input("Introduce la dirección de red de destino: ")
            metrica = int(input("Introduce la métrica: "))
            tabla.agregar_ruta(destino, metrica)
        elif opcion == 2:
            destino = input("Introduce la dirección de red de destino: ")
            mejor_ruta = tabla.encontrar_mejor_ruta(destino)
            if mejor_ruta:
                print(f"La mejor ruta hacia {destino} tiene una métrica de {mejor_ruta.metrica}")
            else:
                print(f"No se encontró una ruta hacia {destino}")
        elif opcion == 3:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
