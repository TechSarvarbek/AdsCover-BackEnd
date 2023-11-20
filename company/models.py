from django.db import models

from users.models import Users


class Locations(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Keywords(models.Model):
	keyword = models.CharField(max_length=20)

	def __str__(self):
		return self.keyword

class Ad(models.Model):
	headline = models.CharField(max_length=30)
	description = models.TextField(max_length=80)
	ad_type = models.CharField(max_length=20, choices=[
		('google', 'Google'),
		('facebook', 'Facebook'),
		('microsoft', 'Microsoft'),
		('instagram', 'Instagram'),
		('twitter', 'Twitter')
	])
	price = models.PositiveIntegerField()

	impressions = models.IntegerField(default=0) 
	clicks = models.IntegerField(default=0) 
	click_rate = models.FloatField(default=0) 
	conversions = models.IntegerField(default=0) 
	cost = models.FloatField(default=0) 
	cpc = models.FloatField(default=0) 
	cpa = models.FloatField(default=0) 


	keywords = models.ManyToManyField(Keywords)

	def __str__(self):
		return self.headline

class Company(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
	locations = models.ManyToManyField(Locations)

	name = models.CharField(max_length=50)
	website = models.CharField(max_length=50)
	launge = models.CharField(max_length=20)
	status = models.BooleanField(default=False)
	created_at = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name

