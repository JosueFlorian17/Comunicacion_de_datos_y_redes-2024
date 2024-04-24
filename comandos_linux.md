# Comandos Linux
## Trabajando con "la Shell" para enviar comandos al sistema operativo, se harà a travès de la terminal de Linux, que nos permitirà interactuar con el teclado directamente en la Shell
1.- Escribiendo comandos sin sentido:

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e3c089b4-a7ec-406d-8174-009a01d6e629)

no se reconoce el comando 
## Comando pwd para mostrar el directorio en donde estamos
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/06168478-f1e3-449f-94d0-54ec9803809f)

## Comando ls para ver la lista de archivos en el directorio
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/60961d5b-ace3-493d-b7f0-fc228e0bc182)

## Comando cd para cambiar el directorio
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e0345673-da97-4f15-b030-b7c79ae1e37c)

## Comandos para manipular archivos
### cp para hacer copias
### mv para renombrar archivos
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/1d290971-0c43-4689-80f3-0148102e147c)
### rm para eliminar archivos
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/c9c408d1-d3fb-492a-af16-7fe94242dc6e)
### mkdir para crear directorios 
en este caso, creamos el directorio redes y trabajamos con él

## Trabajando con comandos
### type
nos ayuda a indetificar el tipo de comando que se correrá
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/145f791b-d74a-4dbb-94fe-f045f70b49ce)
## help
nos muestra los posibles comandos a usar

## Redirección de Inputs/Outputs
con el comando >, podemos guardar los datos en un archivo en lugar de representarlos en la terminal, mientras que con >> podemos añadir en lugar de sobreescribir
![Captura desde 2024-04-24 08-54-34](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/26fae6e4-bbae-4317-89a0-8284cd90f500)


Y para recibir inputs desde un archivo en lugar de escribirlos con el teclado, usamos <, así como una combinación entre input y output
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/258e65f7-93b5-482a-90f3-1e0d59986ddb)

## Permisos
En linux, cada uno de los directorios tiene diferentes accesos, por lo que se necesitará de diferentes permisos para poder trabajar
# Comandos Linux
## Trabajando con "la Shell" para enviar comandos al sistema operativo, se harà a travès de la terminal de Linux, que nos permitirà interactuar con el teclado directamente en la Shell
1.- Escribiendo comandos sin sentido:

![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e3c089b4-a7ec-406d-8174-009a01d6e629)

no se reconoce el comando 
## Comando pwd para mostrar el directorio en donde estamos
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/06168478-f1e3-449f-94d0-54ec9803809f)

## Comando ls para ver la lista de archivos en el directorio
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/60961d5b-ace3-493d-b7f0-fc228e0bc182)

## Comando cd para cambiar el directorio
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/e0345673-da97-4f15-b030-b7c79ae1e37c)

## Comandos para manipular archivos
### cp para hacer copias
### mv para renombrar archivos
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/1d290971-0c43-4689-80f3-0148102e147c)
### rm para eliminar archivos
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/c9c408d1-d3fb-492a-af16-7fe94242dc6e)
### mkdir para crear directorios 
en este caso, creamos el directorio redes y trabajamos con él

## Trabajando con comandos
### type
nos ayuda a indetificar el tipo de comando que se correrá
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/145f791b-d74a-4dbb-94fe-f045f70b49ce)
## help
nos muestra los posibles comandos a usar

## Redirección de Inputs/Outputs
con el comando >, podemos guardar los datos en un archivo en lugar de representarlos en la terminal, mientras que con >> podemos añadir en lugar de sobreescribir
![Captura desde 2024-04-24 08-54-34](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/26fae6e4-bbae-4317-89a0-8284cd90f500)


Y para recibir inputs desde un archivo en lugar de escribirlos con el teclado, usamos <, así como una combinación entre input y output
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/258e65f7-93b5-482a-90f3-1e0d59986ddb)

## Permisos
En linux, cada uno de los directorios tiene diferentes accesos, por lo que se necesitará de diferentes permisos para poder trabajar
  
![Captura desde 2024-04-24 09-01-06](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/f5648e69-9cf0-4d10-aa4b-747f9ef1e472)


el archivo /bin/bash pertenece al usuario "root"
Con **chmod** podemos cambiar los permisos de un archivo
el **superuser** o **su** es necesario para realizar tareas importantes del sistema
mientras que con **sudo** tenemos temporalmente los derechos de superusuario


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

## Inputs de teclado y aritmética
Usamos la función READ para introducir mensajes al terminal
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/db70b4e2-4370-4489-b163-0e19e65bb7a5)

Para ecuaciones aritméticas, es importante **Usar siempre doble paréntesis**


Combinando inputs y diversas operaciones: 

![Captura desde 2024-04-24 08-28-27](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/0086a90f-2de1-4b38-8e6a-c35e132d931d)

## Control de flujo 2:


el archivo /bin/bash pertenece al usuario "root"
Con **chmod** podemos cambiar los permisos de un archivo
el **superuser** o **su** es necesario para realizar tareas importantes del sistema
mientras que con **sudo** tenemos temporalmente los derechos de superusuario

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

## Inputs de teclado y aritmética
Usamos la función READ para introducir mensajes al terminal
![imagen](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/db70b4e2-4370-4489-b163-0e19e65bb7a5)

Para ecuaciones aritméticas, es importante **Usar siempre doble paréntesis**


Combinando inputs y diversas operaciones: 

![Captura desde 2024-04-24 08-28-27](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/0086a90f-2de1-4b38-8e6a-c35e132d931d)

## Control de flujo 2:
