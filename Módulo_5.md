Módulo 5: Entrega de Contenido
- Aprenderemos de las CDN (Content Delivery Network) como Amazon Cloudfront.
- Importancia de las ubicaciones de borde


Amazon CloudFront: Un servicio de red de entrega de contenido (CDN) rápida que entrega datos, videos, aplicaciones e interfaces de programación de aplicaciones (API) de forma segura a clientes de todo el mundo con baja latencia y altas velocidades de transferencia, todo ello dentro de un entorno favorable para los desarrolladores.

AWS Direct Connect: Direct Connect es una solución de servicio de nube que proporciona la capacidad de establecer una conexión de red dedicada desde su entorno en las instalaciones a AWS. Con Direct Connect, puede establecer una conectividad privada entre AWS y su centro de datos, oficina o entorno de coubicación, lo que en muchos casos puede reducir los costos de red, aumentar el rendimiento del ancho de banda y ofrecer una experiencia de red más uniforme que las conexiones basadas en Internet.

Almacenamiento en Caché: Almacena los datos solicitados con frecuencia en ubicaciones de borde para que se pueda acceder a ellos con mayor rapidez.

CDN: Sistema de servidores distribuidos (red) que entrega páginas y otro contenido web a un usuario, en función de las ubicaciones geográficas del usuario, el origen de la página web y el servidor de entrega de contenido.

Distribución:  Indica a CloudFront dónde obtener la información que está almacenando en caché en las ubicaciones de borde y cómo realizar un seguimiento y administrar la entrega de contenido.

Ubicación de borde: Sitio en el que se pueden almacenar los datos para reducir la latencia. A menudo, las ubicaciones de borde estarán cerca de las zonas de gran población que generarán grandes volúmenes de tráfico.

Origen: Tipo complejo que describe el bucket de Amazon S3, el servidor de Protocolo de transferencia de hipertexto (HTTP) (por ejemplo, un servidor web) u otro servidor del que CloudFront obtiene sus archivos.


## Preguntas

**1. ¿Alguna vez ha intentado acceder a una página web, transmitir un video o descargar un archivo, y no funcionó o ha funcionado demasiado lento? ¿Qué contenido era? ¿Cómo lo hizo sentir esto? ¿Por qué cree que pasa esto?**

Intenté entrar a una página aparentemente rusa para poder descargar un archivo, pero tardaba en cargar, imagino que al ser una página poco conocida y lejana geográficamente, se estableció una conexión casi desde cero, teniendo que esperar el tiempo completo

**2. ¿Qué significa el término neutralidad de la red? ¿Cómo se relaciona este término con una CDN y CloudFront?**

Que todos los archivos deben de tratarse de igual manera, se relaciona por medio del envío de la información de CDN y Cloudfront, porque cada "pedazo" de la información debe ser enviado al ser igual de relevante

**3. ¿El acceso a Internet debería ser un derecho humano? ¿Por qué sí o por qué no? ¿Debería permitirse al gobierno restringir determinadas páginas web o contenido en línea? ¿Por qué sí o por qué no?**

Sí, porque al igual que el acceso a cualquier otro recurso, puede ayudar a cambiar la vida de una persona tanto para bien como para mal, recae en la moral del individuo y su entorno el uso que se le dé, por lo que no sería necesaria la intervención del gobierno.


**4. ¿Qué ventajas ofrece el acceso a Internet a un estudiante con respecto a un estudiante sin acceso a Internet? ¿Existe alguna ventaja de no tener acceso a Internet?**

La principal ventaja de aquel estudiante con acceso a internet se encuentra en la mayor disponibilidad a la información y contraste de ideas en línea, podiendo obtener el testimonio de diferentes usuarios sobre un mismo tema, para tener una visió más amplia e informada. La principal ventaja de no tener acceso a internet reside en el mayor desarrollo de aptitudes como la creatividad, ya que al no contar con las respuestas inmediatas, el estudiante requiere de pensar más en una posible respuesta o solución.



# Laboratorio de creación de un CloudFront como CDN

En la opción de Cloushell:
- ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/b0f6f9a1-be2b-43fe-ada8-45e2b1dc24a0)
- creamos un bucket
- ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/fdbc60cd-b3f9-4325-9e8e-97dcb1cd1a79)
- quitamos el bloque a acceso público
- ![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/0934be68-fd9b-49ca-83e7-814709de3acf)
- subimos el index.html
- una vez está listo nuestro S3 y vemos que funciona, crearemos el CloudFront para envio de datos
- Subimos una imagen de elección y copiamos el nombre del dominio de nuestra DNS
- obtenemos el siguiente resultado al poner el código proporcionado

- ![g1](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/92a9c5f2-7984-4946-8617-bfd1ad26d323)



