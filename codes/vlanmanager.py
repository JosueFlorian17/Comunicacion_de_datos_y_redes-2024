class VLANManager:
    def __init__(self):
        self.vlans = {}

    def crear_vlan(self, vlan_id, nombre):
        if vlan_id in self.vlans:
            print(f"Error: Ya existe una VLAN con el ID {vlan_id}.")
            return False
        self.vlans[vlan_id] = {"Nombre": nombre, "dispositivos": []}
        print(f"VLAN {vlan_id} - '{nombre}' creada exitosamente")
        return True

    def asignar_dispositivo(self, vlan_id, dispositivo):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}")
            return False
        if dispositivo in self.vlans[vlan_id]["dispositivos"]:
            print(f"Error: El dispositivo {dispositivo} ya está configurado a la VLAN {vlan_id}.")
            return False

        self.vlans[vlan_id]["dispositivos"].append(dispositivo)
        print(f"Dispositivo {dispositivo} asignado a VLAN {vlan_id} exitosamente")
        return True

    def listar_vlans(self):
        if not self.vlans:
            print("No hay VLANs registradas")
            return
        for vlan_id, info in self.vlans.items():
            print(f"VLAN ID: {vlan_id}, Nombre: {info['Nombre']}, Dispositivos: {info['dispositivos']}")

    def eliminar_vlan(self, vlan_id):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}")
            return False
        del self.vlans[vlan_id]
        print(f"VLAN {vlan_id} eliminada exitosamente")
        return True

    def modificar_nombre_vlan(self, vlan_id, nuevo_nombre):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}")
            return False
        self.vlans[vlan_id]["Nombre"]=nuevo_nombre
        print(f"Se actualizó el nombre a {nuevo_nombre}")
        return True
    def search_by_MAC(self,mac):
        for vlan_id, info in self.vlans.items():
            if mac in info["dispositivos"]:
                print(f"El dispositivo {mac} está asignado a la VLAN {vlan_id} - '{info['Nombre']}'")
                return True
        print("Este dispositivo no está asignado a ninguna VLAN")
        return False
        
    def importar_configuracion(self, archivo):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    vlan_id = int(partes[0])
                    nombre = partes[1]
                    dispositivos = partes[2:]
                    self.vlans[vlan_id] = {'nombre': nombre, 'dispositivos': dispositivos}
            print(f"Configuración de VLANs importada desde {archivo} exitosamente.")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}.")

    
# Demostración del uso de la clase VLANManager
if __name__ == "__main__":
    manager = VLANManager()
    manager.crear_vlan(1, "Producción")
    manager.crear_vlan(2, "Desarrollo")
    manager.asignar_dispositivo(1, "00:1A:2B:3C:4D:5E")
    manager.asignar_dispositivo(2, "00:1A:2B:3C:4D:5F")
    manager.listar_vlans()
    manager.modificar_nombre_vlan(1, "Producción Actualizada")
    manager.listar_vlans()
    manager.eliminar_vlan(2)
    manager.listar_vlans()
    manager.search_by_MAC("00:1A:2B:3C:4D:5F")
    manager.exportar_configuracion("vlans_config.txt")

    # Eliminar VLAN y listar nuevamente
    manager.eliminar_vlan(2)
    manager.listar_vlans()

    # Importar configuración
    manager.importar_configuracion("vlans_config.txt")
    manager.listar_vlans()

    
