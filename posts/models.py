"""Posts Models"""
#Django

from django.db import models

###Creamos una tabla en la BBDD ###

class User(models.Model):

        email = models.EmailField(unique=True)
        password = models.CharField(max_length=100)
        first_name= models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

        is_admin = models.BooleanField(default=False)
        bio = models.TextField(blank=True)
        birthdate = models.DateField(blank=True, null=True)
        created = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)
        country = models.CharField(max_length=100, blank=True)
        city = models.CharField(max_length=100, blank=True)
        
        ### Definimos este metodo String para devolver los valores que queremos en la consulta, sino por defecto devuelve la id del registro
        def __str__(self):
                return self.email

### Luego de crear la tabla vamos a correr el comando > py manage.py makemigrations ###
### luego de esto corremos el > py manage.py migrate ###
### Ya la tabla estará generada ###


""" para grabar datos debemos ir a > py manage.py shell ------------------------ Todo lo siguiente se ejecuta desde la consola"""

"""
###########################################################################     TAREA    ###################################################################################
from posts.models import User
user = User.objects.get(email='emanuel@gmail.com') ###para traer un solo elemento

###si queremos traer varios debemos hacer un filter y el valor que queremos que traiga

users_filt = User.objects.filter(email__endwith='@gmail.com')

###Si quremos traer todos los usuarios podemos utilizar 
users_all = Users.objects.all() 

###Si queremos actualizar varios registros de la tabla ya filtrados podemos correr el comando

users_updated = User.objects.filter(email__endswith='@gmail.com').update(is_admin=True)

###Tarea se crean las 2 tuplas de la tabla (city y country)

### realizar dos consultas
users_deleted = User.objects.filter(city='avellaneda').deleted()
###########################################################################     Fin    ###################################################################################
"""



