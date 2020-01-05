from django.db import models

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	pages = models.IntegerField()

	def __str__(self):
		return self.name