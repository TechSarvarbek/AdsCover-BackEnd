from django.db import models

from users.models import Users

class Payments(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	price = models.PositiveIntegerField()
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.user.email