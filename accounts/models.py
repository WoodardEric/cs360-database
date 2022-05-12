from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    address = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=12, null=False)
    
    def __str__(self):
        return str(self.first_name + self.last_name)
    