Actividad 6: Almacenamiento virtual


Amazon Elastic Block Store (Amazon EBS): Almacenamiento para instancias específicas de Amazon Elastic Compute Cloud (Amazon EC2). Considérelo como la unidad de almacenamiento de la instancia EC2.

Amazon Elastic Compute Cloud (Amazon EC2): Servicio web que ofrece capacidad informática escalable en la nube. Considérelo como alquilar una computadora en la nube.

Unidad de disco duro (HDD): Almacenamiento más lento que utiliza un disco giratorio para almacenar datos.

Operaciones de entrada y salida por segundo (IOPS): Medida de rendimiento frecuente que se utiliza para comparar dispositivos de almacenamiento informático como las unidades de disco duro (HDD) y las unidades de estado sólido (SSD).

Unidad de estado sólido (SSD): Almacenamiento muy rápido que utiliza memoria flash en lugar de un disco giratorio.

A continuación, se presentan otras diferencias clave entre el almacenamiento de datos de Amazon S3 y Amazon EBS:

Amazon EBS solo se puede utilizar cuando se adjunta a una instancia EC2. En cambio, se puede acceder a Amazon S3 de manera independiente mediante los protocolos del Protocolo de transferencia de hipertexto (HTTP).
- Amazon EBS no puede contener tantos datos como Amazon S3.
- Amazon EBS solo puede adjuntarse a una instancia EC2, mientras que varias instancias EC2 pueden acceder a los datos de un bucket de S3.
- Amazon S3 presenta más demoras que Amazon EBS a la hora de escribir datos.
- El modelo de datos de consistencia final se implementa de forma diferente entre Amazon EBS y Amazon S3. La consistencia final significa que, si se realiza una escritura seguida de una lectura, los datos leídos acabarán siendo los mismos que los escritos. Con Amazon EBS, la demora para lograr esta consistencia es casi nula, mientras que podría ser considerablemente mayor con Amazon S3.
Los volúmenes de EBS se cifran en su totalidad, mientras que los objetos de Amazon S3 se cifran de forma individual mediante el cifrado del lado del servidor (SSE).
Amazon EBS incluye tres tipos de volúmenes, mientras que Amazon S3 incluye más tipos:
  - S3 Standard
  - S3 Standard-Infrequent Access (S3 Standard-IA)
  - S3 One Zone-Infrequent Access (S3 One Zone-IA)
  - S3 Intelligent-Tiering
  - S3 Glacier
  - S3 Glacier Deep Archive
 


## Reflexione

Una vez que complete la actividad, prepárese para responder y analizar estas preguntas.

**¿Por qué piensa que AWS ofrece cuatro opciones diferentes para los volúmenes de EBS?**
- La principal característica distintiva en estos diferentes tipos de volúmenes es el caso de uso que se le dará, puesto que, por ejemplo, para datos ligeros y que necesiten accederse de manera veloz, se entiende que un HDD no será la opción más eficiente, puesto que sirve la función de almacenar información pesada de manera resitente y eficaz, pero no tan rápida.

**Describa qué hace que cada uno de los cuatro beneficios de Amazon EBS sea tan importante.**
- La amplia disponibilidadde datos ayuda a que frente a problemas de hardware, no se pierda la información
- La persistencia influye en que, frente a algún problema de nuestra instancia, la información se mantenga
- El cifrado aporta una capa extra de seguridad frente a posibles terceros interceptando la información
- La instantaneidad permite mantener pequeñas copias que se accedan de manera todavía más rápida


## Labnoratorio de EBS
- Creamos una instancia EC2 como se aprendió anteriormente y nos aseguramos que esté disponible de manera pública con la IPv4
- ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/00ddcb73-e6c1-4b87-8020-d12b6d1e4cfa)
- Luego, pasamos a crear un volumen
- Y, finalmente, lo asociamos a nuestra instancia usando la misma zona de disponibilidad (us-east-1b)
- ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/2efe8964-cadd-49d2-99c1-0206a4e408ea)


