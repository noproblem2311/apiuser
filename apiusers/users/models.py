from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

