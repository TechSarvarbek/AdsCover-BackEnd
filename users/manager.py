from django.contrib.auth.models import BaseUserManager



class UsersManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
		    raise ValueError(_('Users must have a number address'))
		user = self.model(email=email, password=password, **extra_fields)
		# user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('active', True)

		if extra_fields.get('is_staff') is not True:
		    raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
		    raise ValueError(_('Superuser must have is_superuser=True.'))
		return self.create_user(email, password, **extra_fields)