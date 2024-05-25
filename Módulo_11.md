Actividad 11

Amazon ElastiCache: Es un servicio web que facilita la implementación, el funcionamiento y el escalado de una caché en memoria en la nube. El servicio mejora el rendimiento de las aplicaciones web, ya que permite la recuperación de la información de cachés en memoria rápidas y administradas, en lugar de depender de bases de datos más lentas basadas en disco.

Caché: nunca
En informática, una caché es una capa de almacenamiento de datos de alta velocidad que almacena un subconjunto de datos, normalmente de naturaleza transitoria, de modo que las solicitudes futuras de esos datos se entregan más rápido de lo que sería posible si se accediera a la ubicación de los datos en el almacenamiento principal.

Almacenamiento de datos en Caché:  El almacenamiento de datos en una caché permite reutilizar de forma eficiente los datos recuperados o calculados previamente. Los datos de una caché generalmente se almacenan en hardware de acceso rápido, como la memoria de acceso aleatorio (RAM) y también se pueden utilizar con un componente de software.

Elastic Load Balancing: Elastic Load Balancing (ELB) distribuye automáticamente el tráfico entrante de las aplicaciones en varios destinos, como las instancias de Amazon Elastic Compute Cloud (Amazon EC2), los contenedores, las direcciones IP y las funciones de AWS Lambda. Si el tráfico a un sitio web aumenta repentinamente, ese tráfico se puede dirigir a otras instancias EC2 (u otros tipos de instancias, como instancias Lambda) que se hayan establecido de antemano para este fin. Este balanceador de carga evita la sobrecarga de un solo servidor debido al aumento del tráfico que se dirige hacia él.

Random Acces Memory: Almacenamiento de memoria volátil y temporal. Estos son los datos que se conservan temporalmente mientras un equipo está en uso; sin embargo, una vez que la máquina se apaga o se completa la tarea, estos datos desaparecen. La memoria virtual se almacena en la memoria de solo lectura (ROM) como complemento de la RAM, cuando no hay suficiente memoria temporal disponible.

## Laboratorio

Creamos una instancia EC2 (Server 1)
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/123a018e-f164-4d02-83c3-2201ce0c7aeb)


Creamos otra instancia EC2 (Server 2) muy parecida a la primera 
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/a5293762-57d5-4360-860d-8e089d285519)
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/8526aa1a-1e6f-4772-808e-598c66a54892)


Están en diferentes zonas de disponibilidad

Ahora creamos un balanceador de carga
  - creamos unos grupos de destino
  - ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/b14fc482-55f5-4050-99ac-5cd5a9bf7789)
- Una vez hay un grupo de destino, se crea el equilibrador de carga
- ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/eba398e3-65dd-4f1d-8f2a-2e1a9c9ae728)

Para comprobar su correcta creación, pondemos el DNS de nuestro balanceador de carga en el navegador y observamos el resultado
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/3dea6412-3962-4cfd-839f-2bd5b592423f)


- Pero podemos observar como, al refrescar la página, cambia entre server 1 y 2, balanceado correctamente la carga entre ambos servidores
