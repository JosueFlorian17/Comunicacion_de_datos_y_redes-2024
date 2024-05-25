# Actividad 3 Identificación de direcciones MAC y direcciones IP

### Objetivos
- Parte 1: Recopilar información de PDU para la comunicación de red local
- Parte 2: Recopilar información de PDU para la comunicación de red remota

### Instrucciones
Recopila información del PDU para la comunicación de red local

### 1. Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 172.16.31.2.
   
a. Haz clic en 172.16.31.5 y abra el Command Prompt.

b. Introduce el comando ping 172.16.31.2.

c. Cambia al modo de simulación y repita el comando ping 172.16.31.2. Aparece una PDU junto a 172.16.31.5.

d. Haz clic en la PDU y observa la siguiente información de las pestañas Modelo OSI l y Capa
de PDU saliente:

- Destination MAC Address: 000C:85CC:1DA7
- Source MAC Address: 00D0:D311:C788
- Source IP Address:172.16.31.5
- Destination IP Address: 172.16.31.2
- At Device: 172.16.31.5

### 2. Reunir información adicional de la PDU de otros ping.
Repite el proceso del paso 1 y reúna información para las siguientes pruebas:
- Ping de 172.16.31.2 a 172.16.31.3
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/a6aef1cf-4fe1-4d28-b875-fcb462df152b)![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/29a5bd21-e8c6-4fc9-a0c8-2223282c3ce5)



- Ping de 172.16.31.4 a 172.16.31.5
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/70f173fe-f84c-47e3-8f42-b9d7fea7a6b4)![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/de4eb729-0f9b-49ad-9ea4-8fe27889f3f9)


  
-Vuelva al modo Realtime.



## Preguntas

**Responde las siguientes preguntas relacionadas con los datos capturados:**

**1.¿Se utilizaron diferentes tipos de cables / medios para conectar dispositivos?**

Sí, tanto conexión directa Ethernet como inalámbrica

**2.¿Los cables cambiaron el manejo de la PDU de alguna manera?**

No

**3.¿El hub perdió parte de la información que recibió?**

No, todos los mensajes fueron enviados y recibidos de manera correcta

**4.¿Qué hace el hub con las direcciones MAC y las direcciones IP?**

Repite los datos y los reparte a los dispositivos conectados

**5.¿El punto de acceso inalámbrico hizo algo con la información que se le entregó?**

Sí, la envió inalámbricamente a la computadora con ip 10.10.10.2

**6.¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica?**

No

**7.¿Cuál fue la capa OSI más alta que utilizaron el hub y el punto de acceso?**

La Capa 1

**8.¿El hub o el punto de acceso reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?**

Sí

**9.Al examinar la ficha PDU Details (Detalles de PDU), ¿qué dirección MAC aparecía primero, la de origen o la de destino?**

La de destino

**10.¿Por qué las direcciones MAC aparecen en este orden?**

Al conocer primero la dirección del destino, el disposito lo envía más rápida y facilmente.

**11.¿Había un patrón para el direccionamiento MAC en la simulación?**

No

**12.¿Los switches reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?**

No, solo las computadoras

**13.Cada vez que se enviaba la PDU entre las redes 10 y 172, había un punto donde las direcciones MAC cambiaban repentinamente. ¿Dónde ocurrió eso?**

En el router.

**14.¿Qué dispositivo usa direcciones MAC que comienzan con 00D0: BA?**

El router

**15.¿A qué dispositivos pertenecían las otras direcciones MAC?**

A las PC’s

**16.¿Las direcciones IPv4 de envío y recepción cambiaron los campos en alguna de las PDU?**

No cambiaron

**17.Cuando sigue la respuesta a un ping, a veces llamado pong, ¿ve el cambio de envío y recepción de direcciones IPv4?**

Sí se puede ver como cambian

**18.¿Cuál es el patrón para el direccionamiento IPv4 utilizado en esta simulación?**

Se deben enviar a cada puerto direcciones IP que no sean iguales

**19.¿Por qué es necesario asignar diferentes redes IP a los diferentes puertos de un router?**

Para poder conectar diferentes equipos y hacer que interaccionen

**20.Si esta simulación se configura con IPv6 en lugar de IPv4, ¿cuál sería la diferencia?**

habría que llenar los campos de IPv6 en lugar de IPv4


