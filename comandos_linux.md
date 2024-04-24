# Comandos Linux
## Trabajando con "la Shell" para enviar comandos al sistema operativo, se harà a travès de la terminal de Linux, que nos permitirà interactuar con el teclado directamente en la Shell
1.- Escribiendo comandos sin sentido:

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e3c089b4-a7ec-406d-8174-009a01d6e629)

no se reconoce el comando 

## Creando Shellscripts
Conteniendo series de comandos

Debemos seguir los siguientes 3 pasos:
- Escribir el script
- Dar permisos a la Shell para ejecutar el script
- Poner el script en un lugar donde la Shell pueda encontrarlo

### escribiendo nuestro primer script
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/6eaa11c1-3139-48d0-b83c-2afb89237bd3)

creamos el script llamado "hello world" que imprime el mensaje, luego de ubicarlo en la ruta de nuestro terminal, lo llamamos y observamos el resultado esperado

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/fa7d2ccb-379a-4363-a48e-6330afe8d03a)


para una mejor organización, creamos nuestro propio BIN en el que almacenaremos nuestros scripts

## Alias
es una forma de abreviar comandos extensos en menos caracteres, en este caso, acortaremos el comando "ls -l" a, simplemente, "l"
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/b41a5f07-1fa3-4c23-9e77-453c33c14c0b)
![Captura desde 2024-04-24 07-27-15](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/ca8999cb-2961-4f00-9d7e-04c7545df4a5)


## Implementando HTML en los scripts

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/2cffa08e-0967-471a-84fb-145f2ab59497)


## Variables

ya que tenemos un script funcional, pasaremos a hacerle mejoras con el uso de variables para evitar trabajo repetitivo

- title="My System Information"
- $title
con este formato de creación y llamada, junto a las reglas de siempre comenzar con una letra, no contener espacios ni signos de puntuación, podemos crear variables que nos ahorrarán la escritura de código repetitivo

luego de diferentes modificaciones, obtenemos el siguiente resultado al modificar nuestro script


![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/d7b69b9f-26c7-4fae-b36f-09b1197504d9)

## Sustitución de comandos y constantes

Gracias a este código " $(date +"%x %r %Z") ", podemos realizar la sustitución de comandos al insertar los valores de, en este caso, la fecha
La creación de constantes no es diferente a la que se tiene en la programación, son valores que, una vez inicializados, no cambiarán.
Una vez aplicados estos conceptos, nuestro script se ve así
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/f01650e0-09d5-4a4d-855f-ee090b189be4)

## Funciones Shell

Idea similar a la encontrada en lenguajes de programación como Python, poder realizar pequeñas tareas que complenten una más grande. En el caso de este ejercicio, lo haremos con un ejemplo de ir a hacer las compras
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/11ff5c17-85a4-49e5-85e4-ef48556e8568)


## Aplicando una Funcion Más Útil

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/99f44106-8366-43ff-8cfb-0848eee2d0b9)

crearemos funciones útiles para el monitoreo de espacio
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/b6366c93-fe98-459c-b151-5c8d92fa5c96)

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/4ba990c2-b704-44d8-8df8-fb6df5d6ec11)


![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/b3c1ef62-1936-485d-b0f1-445109678a6a)


## Control de flujo
### if y elif
tienen el funcionamiento básico de todo lenguaje de programación como condicionales
### exit estatus
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e7df17d2-cd02-4330-a9f8-ef68e9a0eaa2)
vemos como, después de un error, el exit estatus cambia a 2, indicando que un error ocurrió en su ejecutación
True y False dan como exit status 0, por lo que podemos combinarlo con condicionales para tener scripts que validen la verdad o falsedad de una afirmación
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/4e2d0dbc-62d8-469a-af7a-f0a8d95df7d2)

### test
Realizamos el uso de test, si el exit estatus es 0, significa que, internamente, la expresión es verdadera
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/f3dc54fc-d3d7-4882-bbae-2afdb9535a28)


## Para mantenernos fuera de problemas
### debemos evitar
### - Variables vacías
### - Falta de comillas
### podemos probar
### - aislar problemas y resolverlos individualmente
