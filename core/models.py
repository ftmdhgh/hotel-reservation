from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password , **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        #add some validation for password
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(email, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


