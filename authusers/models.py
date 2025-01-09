from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class AuthUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100,unique=False)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_user_groups',
        blank=True
    )


    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_user_permission',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name