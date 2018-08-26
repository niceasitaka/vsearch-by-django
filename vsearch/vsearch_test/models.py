from django.db import models
from django.urls import reverse

# Create your models here.

class Vsearch(models.Model):
	ts = models.DateTimeField(auto_now_add=True)
	phrase = models.CharField(max_length=128)
	letters = models.CharField(max_length=32, blank=True)
	results = models.CharField(max_length=64)
	ip = models.CharField(max_length=16, null=True)
	browser_string = models.CharField(max_length=256, null=True)
	#results = models.CharField(max_length=64)

	def __str__(self):
		return self.phrase
	
	def get_absolute_url(self):
		return reverse('vsearch:result', args=(self.id,))
	