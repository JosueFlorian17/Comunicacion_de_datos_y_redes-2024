Actividad 4

Elegimos start lab y esperamos a que nuestro indicador de AWS se ponga en verde

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/d9bb0488-2f08-4061-b73f-47b65fb613e1)

elegimos EC2

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e8ee052b-bc2c-435d-9808-fc513529b9c9)

Lanzamos la instancia

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/5faabba3-32b0-44a9-a588-9b865a7dd4cb)


Le damos el nombre "Web server 1"

elegimos el AMI por defecto de Amazon/Linux

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/901d339a-06d4-415d-9c4c-b0a02625f89e)


Mantenemos el Tipo de Instancia como t2.micro


Cambiamos el par de claves de inicio de sesión a vockey, que usa el algoritmo de crifrado RSA

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/61e72bba-73fb-42a4-adaa-b1ceda8d1163)


Establecemos una configuración de red

- Dejamos por defecto el VPC, la asignación de IP pública
- Cambiamos el nombre del firewall a Web server
- Cambiamos la descripción del firewall a "Security group for my web server"
- Eliminamos el SSH por defecto, para configurar luego un nuevo método de generar sesiones


![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/f9e6b9cc-feb3-4f92-adb6-81c52d38cba2)



Configuramos almacenamiento:
Mantenemos las opciones por defecto

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/5185005b-47b1-4018-8cf7-ba905ec332b1)


Detalles avanzados
Introducimos el código proporcionado en AWS


``` 
#!/bin/bash
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello World!</h1></html>' > /var/www/html/index.html
``` 

Este código se encarga de:
- Actualizar el servidor
- Instalar Apache Web Server
- Configuar el servidor para iniciarse con el encendido de la computadora
- Activa el servidor web
- Crea una página web simple

Lanzamos la página:
Damos click a lanzar página y observamos el mensaje 

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/cfbf83c4-fffb-4f65-a1ca-aeb717b30480)


Seleccionamos nuestra instancia recién creada (Web Server 1) y observamos la información mostrada. Obteniendo la IPv4 que le fue asignada, podemos alcanzar nuestra instancia a través del internet



![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/582aa5be-e0d4-44ff-90d5-f3d4a3d8a731)



Accediendo a nuestra instancia EC2
Por ahora, si queremos acceder a nuestra instancia, debemos pegar nuestra dirección IP pública en el navegador. Sin embargo, veremos que esto es imposible por el momento, moetrando el siguiente mensaje

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/272c9da5-6860-43ba-b2cc-910f913e9dee)

para poder acceder, tenemos que pasar a 

Actualizar el grupo de seguridad

Debido a que nuestra instancia no permite conexiones desde el puerto 80 (puerto usado para los comandos de HTTP)

entonces, volvemos a la configuración de nuestro web server, específicamente al apartado de Entradas

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/908bab3c-86de-4752-afb2-e1d585d84cce)

Una vez realizados estos cambios

podemos ver que nuestro servidor ¡FUNCIONA!

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/d5a43d41-d63f-4611-b9f2-807b8aa905e7)
