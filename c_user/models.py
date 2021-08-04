from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        if email is None:
            return Response({'Email is required field'})
        if username is None:
            return Response({'Username is required field'})
        if password is None:
            return Response({'Password is required field'})
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            ** extra_fields
        )
        if extra_fields.get('is_staff') and extra_fields.get('is_superuser') == True:
            user.is_active = True
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_active = False
            user.is_superuser = False
            user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, username, password, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password,  **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=122)
    email = models.EmailField(_('Email'), unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'