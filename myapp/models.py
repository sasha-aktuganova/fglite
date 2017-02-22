from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
	user_id = models.ForeignKey(User)
	store_name = models.CharField(max_length=30)
	store_type = models.CharField(max_length=30)
	store_hours = models.CharField(max_length=30)
	store_address = models.CharField(max_length=100)
	store_phone = models.CharField(max_length=30)

	def __str__(self):
		return self.store_name

class Menu(models.Model):
	store_id = models.ForeignKey(Store)
	menu_type = models.CharField(max_length=30)

	def __str__(self):
		return self.menu_type

class Menu_item(models.Model):
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=3)
	section = models.ManyToManyField(Menu)

	def __str__(self):
		return self.title





