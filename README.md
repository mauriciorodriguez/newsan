## Consigna

Implementar una solución que permita guardar y listar una/s Entidad/es TODOs con 
las siguientes características:
TODO (To do, listado de tareas por hacer)
A) ID
B) DESCRIPCION (EL TODO a hacer)
C) Estado
D) Foto/Imagen/Documento adjunta a la DESCRIPCION

A implementar:
1. Listado de TODOs: METHOD GET (Respetar convenciones en la url)
2. Listado filtrado por A B y C: METHOD GET (Utilizar query parameters y respetar 
convenciones)
3. Alta del TODO: METHOD POST (Respetar convenciones en la url). Que reciba la 
foto/imagen/documento también.
4. Cambio de estado, de pendiente a resuelta

Consideraciones:
1. Construir una Solución Back End utilizando alguna de las siguientes tecnologías:
a. .NET /NodeJS/PHP
b. API REST con los servicios a consumir desde el front
c. Proyecto Angular/React/otra tecnología Front para gestionar los TODOs, que 
consuma los servicios del proyecto API REST.
2. Persistencia en DB a elección
3. Incluir el archivo de configuracion README.md en el directorio raíz del proyecto, con 
los pasos a seguir para la instalación y prueba del mismo luego del clonado del 
repositorio.
Todos los pasos para la correcta instalación del mismo deben estar especificados, por 
lo cual se aconseja seguir los lineamientos recomendados: https://el-bid.github.io/guia-de-publicacion/documents/documentacion/

*No se utilizaron las tecnologias mencionadas por el limite de tiempo, tenia 1/2 dias para presentar la solucion por lo que se acordo con la persona que realizaba el test que lo resolveria con una tecnologia conocida por mi

## Guia de usuario

Requerimientos para utilizar el software, las versiones mencionadas son las utilizadas para el proyecto

_Descargar desde la pagina_

[Python](https://www.python.org/downloads/) 3.10.2

##

_Instalar mediante consola de comandos luego de instalar python_

[Django](https://www.djangoproject.com/download/) 4.0.2
```sh
pip install Django
```
Django Cleanup 6.0.0
```sh
pip install django-cleanup
```

##

Luego de instalar los requerimientos, posicionarse en la carpeta raiz del proyecto(la que cuenta con el archivo "manage.py") mediate uso de la terminal, y correr el comando
```sh
python manage.py runserver
```
una vez que el servidor se encuentra en funcionamiento, ya se puede abrir en el navegador [http://localhost:8000/](http://localhost:8000/) y hacer uso del software.


Para detener la ejecucion del servidor
```sh
CTRL+C
```

##

Para correr el servidor en otro puerto
```sh
python manage.py runserver <puerto>
```
