# moni-challenge

## Requerimientos del challenge

Se debe desarrollar un sitio web en el que se registran pedido de préstamos de usuarios que acceden a él.
El usuario no necesita registrarse para solicitar un préstamo.
Para definir si al usuario se le aprueba o no el préstamo usaremos una API definida debajo.

* endpoint: https://api.moni.com.ar/api/v4/scoring/pre-score/[dni]
tenés que pasarle en los headers credential: ZGpzOTAzaWZuc2Zpb25kZnNubm5u

* ejemplo: curl https://api.moni.com.ar/api/v4/scoring/pre-score/30156149 -H "credential: ZGpzOTAzaWZuc2Zpb25kZnNubm5u"

En el formulario de pedido de préstamos, el usuario debe ingresar dni, nombre y apellido, género, email y monto solicitado.

El usuario, luego de ingresar los datos, debe recibir la respuesta negativa o positiva en la misma página que ingresó sus datos.
Contemplar casos de datos ingresados con errores.

También se debe desarrollar un sitio de administración en el que se puedan ver los pedidos de préstamo, con la opción de editarlos y eliminarlos. A este sitio sólo pueden acceder usuarios administradores.

**Nota: No usar admin de Django.**

## Instalación

* Clonarse el proyecto
   ```
   git clone git@gitlab.com:vecchio/moni-challenge.git
   ```
* Crear entorno virtual, con Python 3.10
* Instalar dependencias y crear migraciones

   ```
   make dev-environment
   ```
* Crear superuser

   ```
   make create-admin-user
   ```

## Ejecución
Ejecutar comando:

```
make start
```
Dirigirse a:
```
http://127.0.0.1:8000/
```
