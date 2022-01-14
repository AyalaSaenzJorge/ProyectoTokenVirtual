# Token Virtual

Crear soluciones seguras para los clientes es uno de los objetivos más importantes para la
cualquier empresa, más hoy en día con acecho constante en los fraudes y demás delitos
de tipo electrónico y de suplantamiento de identidad, donde el punto fuerte se encuentra en
la autenticación y validación de datos.
Por fortuna, la tecnología ha avanzado a pasos agigantados en temas de seguridad y
lógicas de autenticación. El Token Virtual es una opción que implementa dichos avances
dentro de las estrategias de protección al usuario.

El Token Virtual, también conocido como token de autenticación, token de seguridad o
token criptográfico, es un servicio tecnológico altamente integrable que genera una clave
de 6 dígitos de forma aleatoria e irreemplazable, dicha clave se actualiza generalmente
cada 60 segundos aproximadamente.

Video Ilustrativo [Segundo 42]: https://youtu.be/3JJRP8MQoYY?t=42

## OBJETIVO

Desarrollar un sistema web orientado a servicios donde se demuestre el funcionamiento de
la implementación del Token Virtual.

## SOLUCIÓN

Se plantea desarrollar una app siguiendo el patrón de arquitectura de Microservicios, de esa
forma se puede manejar cada funcionalidad requerida como componentes individuales, brindando
escalabilidad y facilidad de detectar bugs en caso de que algunos de los microservicios deje
de funcionar.

![Solución propuesta](https://github.com/AyalaSaenzJorge/ProyectoTokenVirtual/blob/main/Soluci%C3%B3n%20de%20Token%20virtual.jpg)

**Token_Control_Service**: permite generar tokens a partir de un nombre de usuario, guardando
en una BD los tokens creados con información de fecha de creación y las veces que el token
se ha usado:
* Para la generación del token, se llama al servicio *Token_Generation_Service*
* Cada vez que se usa un token, éste es primero validado considerando que se solicita su uso
* luego de haber pasado 60 segundos, automáticamente se genera un nuevo token.
* Todas las veces que se usa un token se almacenan en una BD.

**Token_Generation_Service**: genera un número de 6 dígitos que funciona como token virtual.

## REQUERIMIENTOS

* Python 3.8+
* Pip 20.0.2
* Virtualenv 20.0.17 
* NodeJS v14.18.3
* NPM 6.14.15
* MySQL Server 8.0.+

## LEVANTAR BD

Crear base de datos token_control_service_DB e importar el script:

> `mysql -u root -p token_control_service_DB < token_control_service_DB.sql`

## LEVANTAR SERVICIOS

### Servicio de control
* Dirigirse a /ProyectoTokenVirtual/backend/token_control_service:

> /ProyectoTokenVirtual/backend/token_control_service$  `source env/bin/activate`

> /ProyectoTokenVirtual/backend/token_control_service$  `pip install -r requirements.txt`

* Dirigirse a /ProyectoTokenVirtual/backend/token_control_service:

> /ProyectoTokenVirtual/backend/token_control_service/Token_Control$ `python3 manage.py migrate`

> /ProyectoTokenVirtual/backend/token_control_service/Token_Control$ `python3 manage.py runserver`

* El servicio estará levantado, con los siguientes endpoints disponibles (los parámetros son ejemplos):

> http://127.0.0.1:8000/generar_token?cliente=jorge.ayala 

> http://127.0.0.1:8000/validar_token?cliente=jorge.ayala&token=388639 


### Servicio de generación de token

* Dirigirse a /ProyectoTokenVirtual/backend/token_generation_service:

> /ProyectoTokenVirtual/backend/token_generation_service$  `source env/bin/activate`

> /ProyectoTokenVirtual/backend/token_generation_service$  `pip install -r requirements.txt`

* Dirigirse a /ProyectoTokenVirtual/backend/token_generation_service:

> /ProyectoTokenVirtual/backend/token_generation_service/Token_Generation$ `python3 manage.py runserver`

* El servicio estará levantado, con los siguientes endpoints disponibles (los parámetros son ejemplos):

> http://127.0.0.1:8001/crear_token?cliente=jorge.ayala 

## Frontend

* Dirigirse a ProyectoTokenVirtual/frontend:

> /ProyectoTokenVirtual/frontend$ `npm install`

> /ProyectoTokenVirtual/frontend$ `npm start`

La aplicación estará levantada en: 

> http://localhost:3000/

## CAPTURAS DE PANTALLA

* Se genera correctamente un nuevo token por 60 segundos.
![escenario 1](https://github.com/AyalaSaenzJorge/ProyectoTokenVirtual/blob/main/imagen1.png)


* Cuando se presiona el botón, se usa el token y se muestra el tiempo restante actualizado.
![escenario 2](https://github.com/AyalaSaenzJorge/ProyectoTokenVirtual/blob/main/imagen2.png)


* Escenario que ocurre cuando se presiona el botón, se expira el token y el servicio de generación de token deja de funcionar.
![escenario 3](https://github.com/AyalaSaenzJorge/ProyectoTokenVirtual/blob/main/imagen3.png)

* Escenario que ocurre cuando ningún servicio funciona correctamente.
![escenario 4](https://github.com/AyalaSaenzJorge/ProyectoTokenVirtual/blob/main/imagen4.png)




