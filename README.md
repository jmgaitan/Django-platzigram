# Django-platzigram

Para comprender la Logica de Django. 
entenderemos como funciona la secuencia de ejecución.
Mas información en la documentacion de Django. 


las URL son las encargas de buscar el recurso. y hacer match con la petición y relacionarlo con la vista que va a resolver esto y 
el template va a ser la forma en la que se muestran los datos.



                      Patrones de Diseño

Solucion reutilizable a problemas comunes.

model -> view -> controler ->model 

Django lo utiliza con el Model(estructura de datos)-> Template(Logica de presentación) -> View (transformacion de los datos) = framework MVC 

MVC Django.  



Clase 14: Extendiendo el modelo de Usuario

Entendiendo el modelo de Usuario de Django.

1. al momento de instalar el app de django instala una serie de tablas que vienen en settings.py/INSTALLED_APPS=[django.contrib.auth,etc]

2. para crear un usuario utiizando los modelos que nos provee django.
---------Consola--------------------
py manage.py shell
 -> from django.contrib.auth.models import User
u = User.objects.create_user(esto es para que creeemos un registro con un cifrado en la contraseña utilizando a django a nuestro favor) (user='usuario', password=' pass')

veremos si utilizamos u.password el valor del password y veremos que se encuentra cifrado en Sha256

------SQlite-------------

si vamos ahora a la tabla auth_User veremos el usuario recien registrado
 junto a los valores que tiene la tabla.

*** Si quisieramos editar el modelo o agregar campos deberiamos recurrir a la documentacion en github.com/django/django


3. Para crear un super usuario ahora utilizaremos la propiedad de manage.py createsuperuser
-----------Consola---------------
py manage.py createsuperuser
username: 
email adress:
password:
re-password:

para ver los permisos del usuario podemos ir a la URL 
localhost:8000/admin/

sin embargo debemos primero cargar en folder/urls.py

debemos importar admin
from django.contrib import 'admin'

luego agregamos el path del admin
path ('admin', admin.site.urls), y asi utilizamos el administrador django desdel el browser localhost:8000/admin/
, donde veremos 
Usuarios. 
Grupos.

en Github.com/django/django/contrib/auth/models.py

y buscamos la class User
la cual ereda de Abstractuser la cual manera el modelo del user
parecidas al modelo que utilizamos cuando creamos el modelo.



Ya que usaremos este modelo para la aplicacion de Platzigram, eliminamos lo que tenenmos cargado dentro de Platzigram/models.py
borramos las migraciones sin borrar el init.
y borramos la base de datos
