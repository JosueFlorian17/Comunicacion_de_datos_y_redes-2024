Actividad 8

**AWS Shield:** Servicio de protección contra DDoS administrado que protege las aplicaciones que se ejecutan en Amazon Web Services (AWS).

**AWS WAF:** Servicio que le da control sobre qué tráfico permitir o bloquear en sus aplicaciones web mediante la definición de reglas de seguridad web personalizables.

**Denegación de servicio distribuido (DDoS):** Intento malicioso de hacer que un sistema dirigido, como un sitio web o una aplicación, no esté disponible para los usuarios finales. Para lograrlo, los atacantes utilizan una variedad de técnicas que consumen recursos de red o de otros tipos, lo que interrumpe el acceso de los usuarios finales legítimos.

**Amazon Inspector:** Un servicio de evaluación de seguridad automatizada. Le ayuda a probar la accesibilidad a la red de sus instancias de Amazon Elastic Compute Cloud (Amazon EC2) y el estado de seguridad de las aplicaciones que se ejecutan en las instancias.

**AWS Artifact:** Un recurso crucial para la información relacionada con la conformidad. Proporciona acceso bajo demanda a los informes de seguridad y conformidad de AWS y a determinados acuerdos en línea.


## Preguntas

**¿Qué podría motivar a alguien a iniciar un ciberataque contra una empresa? ¿Qué podrían ganar los atacantes? Incluye un ejemplo de una empresa o de un tipo de empresa y un tipo de ciberataque del que podría ser víctima.**

Motivos personales en contra de la organización host del servidor o por competencia entre empresas. Al hacer que el servicio atacado esté de baja, podrían aprovechar en tachar el servicio de poco fiable y robar usuarios.
Por ejemplo, si Wish logra hacer que los servidores de Mercado Libre caigan (pese a que usan servicios de Amazon), podrían aprovechar la desconfianza generada en los usuarios para obtener parte del mercado de compra en línea.

**¿Cree que debería haber diferentes estándares de seguridad para la nube según el tipo de datos que se almacena o procesa? ¿Por qué cree eso? Dé un ejemplo. ¿En qué cree que la seguridad difiere entre los datos almacenados en la nube y los datos almacenados en las instalaciones?**

Sí, porque hay servidores más suceptibles debido al peso de sus archivos, un servidor que mueva texto es más rápido de interceptar y tomar información comparador a uno de video de peso elevado. La seguridad en instalaciones no corre el riesgo de ser interceptado por terceros en internet, en cambio, por la misma naturaleza de los datos enviados en la nube, esto mismo genera un problema a tomar en cuenta

**¿Qué rasgos de carácter cree que necesitaría un administrador de seguridad en la nube exitoso? ¿Por qué? ¿Sería este un rol que le interesaría?**
Debe ser una persona calculadora y que pueda pensar en cualquier vulnerabilidad que presente su sistema, porque de no ser así, todo el servidor que depende de sus implementaciones se verá afectado con una falla que haya cometido. Sinceramente, no me veo interesado en cumplir dicho rol.


## Compare Shield y AWS WAF y proporcione al menos una similitud y una diferencia.
Ambos son servicios de seguridad y se encuentran altamente preparados para evitar ataques DDoS, sin embargo, difieren en que AWS WAF es más personalizable en el sentido en que deja a sus usuarios ajustar más los parámetros de seguridad

