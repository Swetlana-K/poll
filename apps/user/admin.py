from django.contrib import admin
from apps.user import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# um das passwort zu verschlüsseln
class CustomUser(UserAdmin):
        ...

admin.site.register(models.User, CustomUser)

