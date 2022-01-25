from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	phoneNumber = models.CharField(max_length = 200,default = " ")
	profilePic = models.ImageField(upload_to='images/')
	userID = models.ForeignKey(User,on_delete = models.CASCADE,default="")



class Country(models.Model):
	country = models.CharField(max_length= 200,default ="")

	def __str__(self):
		return self.country


class State(models.Model):
	state = models.CharField(max_length =200,default = "")
	countryID = models.ForeignKey(Country,on_delete = models.CASCADE,default = "")

	def __str__(self):
		return self.state

class City(models.Model):
	city = models.CharField(max_length =200,default = "")
	stateID = models.ForeignKey(State,on_delete = models.CASCADE,default = "")

	def __str__(self):
		return self.city
