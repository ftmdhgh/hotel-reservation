from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

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

    def __str__(self):
        return f'{self.f_name} {self.l_name}: {self.email}'

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    total_rooms = models.IntegerField(null=True, blank=True)
    available_rooms = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Room(models.Model):

    class RoomTypes(models.TextChoices):
        SINGLE = 'SI', _('Single')
        DOUBLE = 'DO', _('Double')
        SUITE = 'SU', _('Suite')

    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.IntegerField()
    type = models.CharField(max_length=2, choices=RoomTypes.choices, default=RoomTypes.SINGLE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.room_number}\'th room in {self.hotel.__str__()} hotel'

class Reservation(models.Model):
    class ReservationStatus(models.TextChoices):
        PENDING = 'PE', _('Pending')
        CONFIRMED = 'CO', _('Confirmed')
        CANCELLED = 'CA', _('Cancelled')

    user = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='room_reservations', on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    status = models.CharField(max_length=2, choices=ReservationStatus.choices, default=ReservationStatus.PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user.__str__()}\'s reservation in {self.room.__str__()}'

