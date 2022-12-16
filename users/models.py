from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        print('Se ejecuto el create_user')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        print('Se ejecuto el create_user SUPEEEEEEEER')
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        print(extra_fields)

        if extra_fields.get('is_staff') is not True:            
            raise ValueError("El superusuario necesita que is_staff = True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("el superususario necesita tener todos los permisos is_superuser=True")
        
        return self.create_user(email=email, password=password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField('Direccion de Correo', unique=True)    
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    realname = models.CharField(max_length=100, null=True, blank=True)          
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)              
    created_at = models.DateField(auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email

    # @property
    # def is_staff(self):
    #     return self.is_admin