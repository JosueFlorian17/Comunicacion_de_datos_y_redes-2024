class VLANManager:
            def __init__(self):
                self.vlans={}
            def crear_vlan(self,vlan_id,nombre):
                if vlan_id in self.vlans:
                    print(f"Error: Ya existe una VLAN con el ID {vlan_id}")
                    return False
                self.vlans[vlan_id]={"nombre":nombre,"dispositivos":[]}
                print(f"VLAN {vlan_id}-'{nombre}' creada exitosamente")
                return True
            def asignar_dispositivo(self, vlan_id, dispositivo):
                if vlan_id not in self.vlans:
                    print(f"Error_ No se encuentró la VLAN con ID {vlan_id}.")
                    return False
                if dispositivo in self.vlans[vlan_id]["dispositivos"]:
                    print(f"Error: El dispositivo {dispositivo} ya está asignado a la VLAN {vlan_id}")
                    return False

                self.vlans[vlan_id]["dispositivos"].append(dispositivo)
                print(f"Dispositivo {dispositivo} asignado a VLAN {vlan_id} exitosamente")
                return True

            def listar_vlans(self):
                if not self.vlans:
                    print("No hay VLANs registradas")
                    return
                for vlan_id,info in self.vlans.items():
                    print(f"VLAN ID: {vlan_id}, Nombre: {info['nombre']}, Dispositivos: {info['dispositivos']}")

            def eliminar_vlan(self,vlan_id):
                if vlan_id not in self.vlans:
                    print(f"Error: No se encontró la VLAN con ID {vlan_id}")
                    return False
                del self.vlans[vlan_id]
                print(f"VLAN {vlan_id} eliminada exitosamente")
                return True
            def rename(self,vlan_id,new_name):
                if vlan_id in self.vlans:
                    print(f"Se renombrará {vlan_id} a {new_name}")
                    self.vlans[vlan_id]={"nombre":new_name,"dispositivos":[]}
                    return True
                else:
                    print(f"Error: No existe una VLAN con el ID {vlan_id}")
                    return False
            def search_by_mac(self,mac):
                for vlan_id,info in self.vlans.items():
                    for i in range(len(info['dispositivos'])+1):
                        if info['dispositivos'][i]== mac:
                            print(f"La dirección MAC {mac} está asignada a a la VLAN de ID: {vlan_id} y Nombre: {info['nombre']}")
                            return True
                        else:
                            pass
                return f"El dispositivo con MAC {mac} no está asignado a ninguna VLAN"
                    
                    
if __name__ =="__main__":
    manager=VLANManager()
    manager.crear_vlan(1,"Producción")
    manager.crear_vlan(2,"Desarrollo")
    manager.asignar_dispositivo(1,"00:1A:2B:3C:4D:5E")
    manager.asignar_dispositivo(1,"00:1A:2B:3C:4D:5X")
    manager.asignar_dispositivo(2,"00:1A:2B:3C:4D:5F")
    manager.listar_vlans()
    #manager.eliminar_vlan(2)
    manager.listar_vlans()
    manager.rename(4,"Caca")
    manager.search_by_mac("00:1A:2B:3C:4D:5X")
