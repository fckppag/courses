from django.db import models
import random

class Course(models.Model):
	
	title = models.CharField('Введите имя', max_length=50)
	ID_Pass = models.CharField('Введите ID', max_length=50)


	def __str__(self):
		return self.title