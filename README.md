Aplicación "TODO SERIES"

explicación en video: https://www.youtube.com/watch?v=v_5c8ZVGCvg

Creadores: 
- Fernando Dalla Rosa
- Federico Poliseno
- Fernando Masnú

(Antes de usar realiza migraciones con el comando en git bash "python manage.py makemigrations" y luego "python manage.py migrate)

Para comenzar a utilizar la aplicación se debe realizar el comando "python manage.py runserver" en la termina git bash y luego incresar en el navegador a "localhost:8000"

TODO SERIES es un blog en donde el usuario puede recomendar diferentes series que haya visto.

se puede usar el boton "Sobre nosotros" dentro del sitio para conocer sobre la app y los creadores.

Al entrar al sitio (utilizando "localhost:8000") el usuario tiene la opción de "Iniciar sesión" y "Crear usuario".
En la página principal del sitio se pueden ver todos los blogs publicados

Una vez iniciada la sesión el usuario va a tener 2 opciones: "Cerrar sesión" o "Publicar blog"

Cuando el usuario va a publicar un blog se le pide titulo, sub titulo, cuerpo y una imagen en el fomrulario.

Una vez publicado el blog se puede utilizar el boton "Leer más" en el blog para verlo completo y con la imagen que se subió.

Si el usuario lo desea puede borrar o actualizar su blog publicado con sus correspondientes botones.

Si se entra a localhost:8000/admin se puede tener acceso a un usuario administrador que puede:
-editar usuarios
-editar posteos
-agregar usuarios
-eliminar usuarios
-crear posteos
-eliminar posteos

