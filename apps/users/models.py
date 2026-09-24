from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100) # полное имя (максимальная длина - 100)
    phone = models.CharField(max_length=20) # телефон - формат: 8(XXX)XXX-XX-XX (максимальная длина - 20)
    email = models.EmailField(unique=True) # почта (должна быть уникальная)