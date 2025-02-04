from django.db import models
from django.contrib.auth.models import AbstractUser


# Extending AbstractUser model to define email as a unique field
class User(AbstractUser):
    email = models.EmailField(unique=True)