class Firewall:
    def __init__(self, reglas, puertos, ip):
        self.reglas = reglas
        self.puertos = puertos
        self.ip = ip
        self.logs = []  # Lista de logs de acceso

    def adjuntar_regla(self, regla):
        if regla not in self.reglas:
            self.reglas.append(regla)
            print(f"Regla añadida: {regla}")
        else:
            print("Esta regla ya está en el conjunto de reglas del firewall")

    def comprobar_paquete(self, ip, puerto):
        """
        Comprueba un paquete contra las reglas del firewall.
        :param ip: Dirección IP del paquete
        :param puerto: Puerto del paquete
        :return: "permitir" o "bloquear"
        """
        for regla in self.reglas:
            if regla['ip'] == ip and regla['puerto'] == puerto:
                self.logs.append({'ip': ip, 'puerto': puerto, 'accion': regla['accion']})
                return regla['accion']
        self.logs.append({'ip': ip, 'puerto': puerto, 'accion': 'permitir'})
        return 'permitir'  # Si no hay regla específica, permitir el tráfico

    def imprimir_logs(self):
        """
        Imprime los logs de acceso.
        """
        for log in self.logs:
            print(f"IP: {log['ip']}, Puerto: {log['puerto']}, Acción: {log['accion']}")

# Ejemplo de uso
firewall = Firewall(
    reglas=[
        {'accion': 'permitir', 'ip': '192.168.1.1', 'puerto': '80'},
        {'accion': 'bloquear', 'ip': '192.168.1.2', 'puerto': '22'}
    ],
    puertos=['80', '22'],
    ip=['192.168.1.1', '192.168.1.2']
)

firewall.adjuntar_regla({'accion': 'bloquear', 'ip': '10.0.0.1', 'puerto': '443'})
print(firewall.reglas)

# Comprobando paquetes
print(firewall.comprobar_paquete('192.168.1.1', '80'))  # debería permitir
print(firewall.comprobar_paquete('192.168.1.2', '22'))  # debería bloquear
print(firewall.comprobar_paquete('10.0.0.1', '443'))    # debería bloquear
print(firewall.comprobar_paquete('10.0.0.2', '80'))     # debería permitir (no hay regla específica)

# Imprimiendo logs
firewall.imprimir_logs()
