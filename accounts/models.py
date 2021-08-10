from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, null=True, blank=True)
	
	phone = models.CharField(max_length=10, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	# gender = models.CharField(max_length=50, null=True, blank=True)
	pin_code = models.CharField(max_length=6,null=True,blank=True,unique=True)
	address = models.CharField(max_length=500, null=True, blank=True)
	state = models.CharField(max_length=500, null=True, blank=True)
	city = models.CharField(max_length=500, null=True, blank=True)
	Country = models.CharField(max_length=50, null=True, blank=True)

	def _str_(self):
		return self.user.username
	

     
        
#



