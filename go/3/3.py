import random
class VirtualMachine:
    def __init__(self,recursos):
        self.estado="Apagado"
        self.recursos=recursos


class HyperVisor:
    def __init__(self,vm):
        self.vm=vm

    def iniciar(self):
        if self.vm.estado!="Iniciado":
            self.vm.estado="Iniciado"
            return "Se ha iniciado la máquina virtual"
        else:
            return "La máquina virtual ya está iniciada"

    def detener(self):
        if self.vm.estado!="Apagado":
            self.vm.estado="Apagado"
            return "Se ha apagado la máquina virtual"
        else:
            return "La máquina virtual ya está apagada"

    def reiniciar(self):
        if self.vm.estado!="Apagado":
            print("Se reiniciará la máquina virtual")
            self.detener()
            self.iniciar()
            return "Se ha reiniciado la máquina virtual"

    def balancear(self,vm,otra):
        a=len(vm.recursos)
        b=len(otra.recursos)
        
        if a<b:
            menor=vm
            mayor=otra
        if b<a:
            menor=otra
            mayor=vm
        else:
            menor="iguales"
        factor=a-b
        if factor<0:
            factor*=-1
        for i in range(factor//2):
            item=random.choice(mayor.recursos)
            menor.recursos.append(item)
            mayor.recursos.remove(item)
        return vm.recursos, otra.recursos

vm=VirtualMachine([1,2,3,4,5,6,7,8])
vm2=VirtualMachine([1,2,3,4])
visor=HyperVisor(vm)
print(visor.iniciar())
print(visor.detener())
vm.estado="Iniciado"
print(visor.reiniciar())
print(visor.balancear(vm,vm2))
