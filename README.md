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

Para correr el servidor en otro purto
```sh
python manage.py runserver <puerto>
```
