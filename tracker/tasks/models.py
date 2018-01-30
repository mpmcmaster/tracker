from django.db import models

# Create your models here.
class Recipient(models.Model):
	recipient_name = models.CharField(max_length=50)
	recipient_email = models.EmailField(max_length=254, default='')
	recipient_type = models.CharField(max_length=20)

	def __str__(self):
		return self.recipient_name

class Task(models.Model):
	task_description = models.CharField(max_length=100)
	

	def __str__(self):
		return self.task_description
