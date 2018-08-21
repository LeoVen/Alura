from django.db import models

# Create your models here.

class Profile(models.Model):

	name = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	phone = models.CharField(max_length=15, null=False)