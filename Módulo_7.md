Actividad 7

# Laboratorio de exploración de usuarios y grupos
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/8f329542-c326-458c-97c6-55be18134be1)

En la ventana de usuarios del apartado IAM, elegimos al usuario 1 y verificamos que no pertenece a ningun grupo ni tiene permiso alguno.

Pasamos al apartado de grupos de usuarios

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/113f663e-9783-4b6e-ada4-5dc119c774c4)

Revisamos los 3 grupos y sus funciones y agragamos a los usuarios a estos grupos

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/ffc3ef33-bca8-45d3-af5d-bee4143eae06)



Ya que asignamos al usuario 1 al rol de soporte de S3, podemos observar como tiene acceso a los buckets S3, mas no a una instancia EC2

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/79a96ef2-54a0-4a9a-8a40-074d5bd6d16c)

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/185819e9-586f-4937-a3f7-24eaccc85060)


### Como el usuario 2:
Tenemos acceso a una instancia EC2 gracias al rol que se nos asignó al "ser contratados"
![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/1920ac3d-ec3f-459e-8f7f-b2c3753962b7)

sin embargo, si intentamos detener la instancia, no podremos, ya que no contamos con esos permisos con nuestro rol

![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/c1feedbc-e33e-421f-be95-67a7aa143349)

### Como el usuario 3:

Podemos detener la instancia gracias a nuestro rol de EC2-Admin


![image](https://github.com/JosueFlorian17/Comunicacion_de_datos_y_redes-2024/assets/150297452/aa65a508-df9e-4c43-b6f9-baac3944249d)

