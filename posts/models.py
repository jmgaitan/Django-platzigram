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

        def __str__(self):
                return self.email

### Luego de crear la tabla vamos a correr el comando > py manage.py makemigrations ###
### luego de esto corremos el > py manage.py migrate ###
### Ya la tabla estará generada ###

""" para grabar datos debemos ir a > py manage.py shell """

