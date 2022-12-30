# backend-fastapi
# Instalación
Para instalar FastAPI y Uvicorn, primero debes crear un entorno virtual llamado "env" para aislar las dependencias de tu proyecto.

```
python3 -m venv env
```
Luego, activa el entorno virtual con el siguiente comando:

```
source env/bin/activate
```
Ahora, instala FastAPI y Uvicorn con el siguiente comando:

```
pip install fastapi uvicorn
```
# Ejecución
Para ejecutar la aplicación, utiliza el siguiente comando:

```
uvicorn main:app --reload
```
Con este comando, Uvicorn iniciará la aplicación y se actualizará automáticamente cada vez que se hagan cambios en el código.

# Uso
La aplicación incluye varias rutas que puedes utilizar para acceder a diferentes recursos. Por ejemplo, para acceder a la lista de rutas disponibles, puedes hacer una solicitud GET a la ruta "/rutas". También puedes acceder a una ruta específica utilizando su ID con la ruta "/rutas/{id}".

Además, la aplicación incluye varias funciones para modificar las rutas existentes, como agregar una nueva ruta con una solicitud POST a la ruta "/rutas/nueva/", actualizar una ruta existente con una solicitud PUT a la ruta "/rutas/{id}" y eliminar una ruta con una solicitud DELETE a la ruta "/rutas/{id}".