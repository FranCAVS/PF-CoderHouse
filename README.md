# Indicaciones
La versión que esta aca en main en la versión final, y la que esta en master en la versión que tiene todos los commits hechos por los participantes del grupo.

# Link en YouTube de previsualizacion de la pagina:
https://www.youtube.com/watch?v=uN6G7pgGwCQ&ab_channel=FrancescoVaccaro

# PF-CoderHouse
Proyecto Final del curso de Python x CoderHouse // Pagina Web-Blog

Este proyecto final esta hecho para crear un sistema de administración de blogs y editores. Cosas que se pueden hacer:

- Crear tu propio usuario
- Crear, leer, actualizar artículos.
- Añadir una imagen para cada artículo.

# Instalación

Para el funcionamiento correcto de este proyecto:

## Verificar tu versión de python

Este proyecto fue escrito con Python 3.10.5 por lo que le se le sugiere testear el proyecto con esta versión para no tener ningún problema de compatibilidad.

## Como me fijo mi versión de Python,

En la terminal del IDLE:
```bash
> python --version
> Python 3.10.5
```
En CMD de Windows:
```bash
c:\> py --version
c:\> Python 3.10.5
```

## Instalar Dependencias

Para instalar las dependencias necesitas ejecutar `pip install`, asegúrate de que estás en la carpeta del proyecto y ahí deberías poder ver el archivo `requirements.txt`, cuando hagas un `ls` o `dir` en la terminal del IDLE:

```bash
> pip install -r requirements.txt
```
Esto último devolverá las dependencias que se necesitán para ejecutar el proyecto correctamente en la terminal.

`En algunos sistemas operativos se tiene que utilizar pip3 en vez de pip `

## Configuración de Django

Una vez que termines la instalación de las dependencias necesitas ejecutar los siguientes comandos.

### Migraciones

Iniciar la base de datos:

En la terminal del IDLE:
```bash
> python mananage.py migrate
```
En el CMD de Windows:
```bash
c:\> py mananage.py migrate
```

### Iniciar el servidor

```bash
> python mananage.py runserver
```
En el CMD de Windows:
```bash
c:\> py mananage.py runserver
```
En tu terminal correspondiente te va a aparecer la IP para poder acceder. O en tu navegador pone: localhost:8000/

para tener acceso a la aplicación.

Si todo va bien deberías poder abrir el navegador y ver la aplicación funcionando correctamente.

### Link Planilla Google de Tabla de Pruebas Unitarias
https://docs.google.com/spreadsheets/d/1zE_kGb4OuqE3liJg7P82WVGDzq3ojhACvHJVoLqiDak/edit?usp=sharing
