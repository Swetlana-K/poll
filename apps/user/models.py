from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Management der Benutzer

class User(AbstractUser):                   # Feld kann leer bleiben        
    title = models.CharField(max_length=100, null=True, help_text='Your profession')
                            # als leerer String
    bio = models.TextField(default='')
    aim = models.TextField(default='')
    # admin