import random

class VirtualMachine:
    def __init__(self,procesos):
        self.estado="Apagado"
        self.procesos=procesos


class Hypervisor:

    def iniciar(vm):
        vm.estado = "Encendido"
        print(f"VM iniciado")

    def detener(vm):
        vm.estado = "Apagado"
        print(f"VM detenido")


    def reiniciar(vm):
        vm.estado = "Reiniciando"
        print(f"VM reiniciando")
        Hypervisor.detener(vm)
        Hypervisor.iniciar(vm)
    

    def balanceo(vm,otra):
        if len(vm.procesos)>4:
            x=random.choice(vm.procesos)
            y=random.choice(vm.procesos)

            vm.procesos.remove(x)
            vm.procesos.remove(y)

            otra.procesos.append(x)
            otra.procesos.append(y)

        print(vm.procesos)
        print(otra.procesos)

virtual=VirtualMachine([1,2,3,4,5,6,7,8,9])
machine=VirtualMachine(["a","b","c","d","e"])
visor=Hypervisor
visor.balanceo(virtual,machine)
visor.detener(virtual)
