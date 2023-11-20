from random import randint
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from .manager import UsersManager



class Users(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=225, validators=[MinLengthValidator(6)])
	confirmation_code = models.CharField(max_length=5, default=randint(10000, 99999))
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	telegram_name = models.CharField(max_length=30)
	referral = models.CharField(max_length=255, null=True, blank=True)
    
	created_at = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=False)
	block = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	objects = UsersManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['password',]

	def __str__(self):
		return self.email

	def save(self, *args, **kwargs):
		if self.is_superuser and not self.id:
			self.set_password(self.password)

		super().save(*args, **kwargs)